# -*- coding: utf-8 -*-
import json, re, os
from docx import Document
from docx.oxml.ns import qn
from docx.text.paragraph import Paragraph
from docx.table import Table

SRC = "/sessions/sleepy-epic-wozniak/mnt/uploads/Bí kíp ngữ pháp toàn thư tập 1.docx"
ROOT = "/sessions/sleepy-epic-wozniak/mnt/outputs/site/data"
OUT = os.path.join(ROOT, "books", "grammar-morphology")
os.makedirs(os.path.join(OUT, "units"), exist_ok=True)

CYR = re.compile(r'[Ѐ-ӿ]')
COMB = re.compile(r'[̀-ͯ]')
def has_cyr(s): return bool(CYR.search(s or ""))
def strip_stress(s): return COMB.sub('', s or '')
def norm_ru(s): return strip_stress(s).strip().lower().replace('ё','е')

PART_META = {
 1: dict(slug="01-nouns",      vi="Danh từ",  ru="Имя существительное", icon="\U0001F4E6", color="#6366f1"),
 2: dict(slug="02-adjectives", vi="Tính từ",  ru="Имя прилагательное",  icon="\U0001F3A8", color="#ec4899"),
 3: dict(slug="03-pronouns",   vi="Đại từ",   ru="Местоимение", icon="\U0001F464", color="#14b8a6"),
 4: dict(slug="04-numerals",   vi="Số từ",    ru="Имя числительное", icon="\U0001F522", color="#f59e0b"),
 5: dict(slug="05-adverbs",    vi="Trạng từ", ru="Наречие", icon="⚡", color="#8b5cf6"),
 6: dict(slug="06-particles",  vi="Tiểu từ",  ru="Частицы", icon="\U0001F527", color="#06b6d4"),
 7: dict(slug="07-verbs",      vi="Động từ",  ru="Глагол", icon="\U0001F3C3", color="#ef4444"),
}
re_part = re.compile(r'^(?:PHẦN|Phần)\s+(\d+)\s*[:\.]', re.IGNORECASE)
re_ex   = re.compile(r'^(?:BÀI TẬP|Bài tập|Bài)\s*(\d+)', re.IGNORECASE)

def block_kind(text, bold, italic):
    t = text.strip(); low = t.lower()
    if low.startswith('yêu cầu'): return 'instruction'
    if low.startswith('mục đích'): return 'goal'
    if low.startswith(('lưu ý','chú ý','ghi nhớ')): return 'note'
    if low.startswith(('mẫu','mô hình')): return 'model'
    if low.startswith('ví dụ'): return 'example'
    if low.startswith(('từ vựng','đáp án','gợi ý','hướng dẫn','phần a','phần b','phần c','chủ đề','cấu trúc','quy tắc','phân biệt','mục')):
        return 'subhead'
    m = re.match(r'^\s*(?:\d+[\.\)]\s*)?(.+?)\s*:\s*(.+)$', t)
    if m and has_cyr(m.group(1)) and m.group(2).strip() and len(m.group(1)) <= 60:
        return 'vocab'
    if t.endswith(':') and has_cyr(t) and len(t) <= 80: return 'subhead'
    if italic: return 'example'
    return 'para'

def make_para(p):
    runs = [r for r in p.runs if r.text]
    bold = bool(runs) and all((r.bold or not r.text.strip()) for r in runs)
    italic = any(r.italic for r in runs)
    return p.text.strip(), bold, italic

doc = Document(SRC); body = doc.element.body
parts = []; cur_part = None; cur_section = None; cur_gender = None; glossary = {}

def new_section(stype, title, num=None):
    global cur_section, cur_gender
    cur_gender = None
    sid = f"{cur_part['num']:02d}-s{len(cur_part['sections'])+1:03d}"
    cur_section = dict(id=sid, type=stype, title=title, num=num, blocks=[])
    cur_part['sections'].append(cur_section)

def new_part(num, title):
    global cur_part
    meta = PART_META.get(num, dict(slug=f"{num:02d}-part", vi=title, ru="", icon="\U0001F4D8", color="#64748b"))
    cur_part = dict(num=num, title=title, **meta, sections=[]); parts.append(cur_part)

GEN = [('мужско','m'),('женск','f'),('средн','n')]

for child in body.iterchildren():
    if child.tag == qn('w:p'):
        p = Paragraph(child, doc); text = p.text.strip()
        if not text: continue
        style = p.style.name if p.style else 'Normal'
        is_heading = style.startswith('Heading') or style == 'Title'
        mp = re_part.match(text)
        if is_heading and mp and (cur_part is None or int(mp.group(1)) > cur_part['num']):
            new_part(int(mp.group(1)), text); continue
        if is_heading and ('ĐỘNG TỪ' in text.upper()) and ('NGỮ PHÁP' in text.upper()) and (cur_part is None or cur_part['num'] != 7):
            new_part(7, "PHẦN 7: ĐỘNG TỪ (Глагол)"); new_section('grammar', text); continue
        if cur_part is None:
            if is_heading and ('DANH TỪ' in text.upper()): new_part(1, text)
            continue
        if is_heading:
            me = re_ex.match(text)
            if me: new_section('exercise', text, num=int(me.group(1)))
            else: new_section('grammar', text)
            continue
        if cur_section is None: new_section('grammar', cur_part['title'])
        t, bold, italic = make_para(p); kind = block_kind(t, bold, italic)
        low = t.lower()
        for key,g in GEN:
            if key in low and (t.endswith(':') or '(' in t): cur_gender = g
        if kind == 'vocab':
            m = re.match(r'^\s*(?:\d+[\.\)]\s*)?(.+?)\s*:\s*(.+)$', t)
            ru, vi = m.group(1).strip(), m.group(2).strip()
            cur_section['blocks'].append(dict(t='vocab', ru=ru, vi=vi, g=cur_gender))
            key = norm_ru(ru)
            if key and key not in glossary and len(key) <= 40:
                glossary[key] = dict(ru=ru, ruPlain=strip_stress(ru), vi=vi, g=cur_gender, ref=cur_section['id'])
        else:
            blk = dict(t=kind, text=t)
            if bold: blk['b'] = 1
            cur_section['blocks'].append(blk)
    elif child.tag == qn('w:tbl'):
        if cur_part is None or cur_section is None: continue
        tbl = Table(child, doc)
        rows = [[c.text.strip() for c in r.cells] for r in tbl.rows]
        if rows: cur_section['blocks'].append(dict(t='table', rows=rows))

book = dict(id="grammar-morphology",
    title="Ngữ pháp tiếng Nga — Hình thái học",
    subtitle="Giải bài tập ngữ pháp tiếng Nga (Морфология)",
    lang="ru", uiLang="vi", level="A2–B2", cover="\U0001F4D5",
    description="Tuyển tập bài tập ngữ pháp tiếng Nga theo hình thái học: danh từ, tính từ, đại từ, số từ, trạng từ, tiểu từ và động từ — kèm lời giải và từ vựng song ngữ.",
    parts=[])

for part in parts:
    fname = f"{part['slug']}.json"
    unit = dict(id=part['slug'], num=part['num'], title=part['title'], vi=part['vi'],
                ru=part['ru'], icon=part['icon'], color=part['color'], sections=part['sections'])
    with open(os.path.join(OUT, "units", fname), "w", encoding="utf-8") as f:
        json.dump(unit, f, ensure_ascii=False, indent=1)
    n_ex = sum(1 for s in part['sections'] if s['type']=='exercise')
    n_gr = sum(1 for s in part['sections'] if s['type']=='grammar')
    book['parts'].append(dict(id=part['slug'], num=part['num'], title=part['title'], vi=part['vi'],
        ru=part['ru'], icon=part['icon'], color=part['color'], file=f"units/{fname}",
        sectionCount=len(part['sections']), exerciseCount=n_ex, grammarCount=n_gr))

with open(os.path.join(OUT, "book.json"), "w", encoding="utf-8") as f:
    json.dump(book, f, ensure_ascii=False, indent=1)
gloss = sorted(glossary.values(), key=lambda e: e['ruPlain'].lower())
with open(os.path.join(OUT, "glossary.json"), "w", encoding="utf-8") as f:
    json.dump(dict(count=len(gloss), entries=gloss), f, ensure_ascii=False, indent=1)

library = dict(title="Thư viện tiếng Nga",
    books=[dict(id=book['id'], title=book['title'], subtitle=book['subtitle'], cover=book['cover'],
                level=book['level'], lang="ru", path=f"books/{book['id']}/book.json", type="grammar")],
    comingSoon=[dict(title="Truyện song ngữ Nga–Việt", cover="\U0001F4D6", type="reader"),
                dict(title="Postcard & Văn hoá Nga", cover="\U0001F5BC️", type="culture"),
                dict(title="Video bài giảng", cover="\U0001F3AC", type="video"),
                dict(title="Trò chơi từ vựng", cover="\U0001F3AE", type="game")])
with open(os.path.join(ROOT, "library.json"), "w", encoding="utf-8") as f:
    json.dump(library, f, ensure_ascii=False, indent=1)

print("PARTS:", len(parts))
for p in parts:
    n_ex = sum(1 for s in p['sections'] if s['type']=='exercise')
    print(f"  Part {p['num']:>2} {p['vi']:<9} sections={len(p['sections']):>4} ex={n_ex:>4}  ({p['title'][:42]})")
print("GLOSSARY:", len(gloss))
print("TOTAL sections:", sum(len(p['sections']) for p in parts),
      "blocks:", sum(len(s['blocks']) for p in parts for s in p['sections']))
