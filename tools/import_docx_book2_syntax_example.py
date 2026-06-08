# -*- coding: utf-8 -*-
import json, re, os
from docx import Document

SRC="/sessions/sleepy-epic-wozniak/mnt/uploads/ГРАММАТИКА РУССКОГО ЯЗЫКА 2.docx"
ROOT="/sessions/sleepy-epic-wozniak/mnt/outputs/site/data"
BOOK="grammar-syntax"
OUT=os.path.join(ROOT,"books",BOOK)
os.makedirs(os.path.join(OUT,"units"),exist_ok=True)

CYR=re.compile(r'[Ѐ-ӿ]'); COMB=re.compile(r'[̀-ͯ]')
LAT=re.compile(r'[A-Za-zÀ-ỹ]')
def has_cyr(s): return bool(CYR.search(s or ""))
def strip_stress(s): return COMB.sub('', s or '')
def norm_ru(s): return strip_stress(s).strip().lower().replace('ё','е')

re_ex=re.compile(r'^Упражне́?ние\s+(\d+)', re.IGNORECASE)
re_numex=re.compile(r'^(\d+)\.\s*(.+)$')

PALETTE=["#6366f1","#ec4899","#14b8a6","#f59e0b","#8b5cf6","#06b6d4","#ef4444","#10b981","#f43f5e","#0ea5e9","#a855f7","#22c55e"]
ICONS=["🔗","🧩","📐","🎯","🧭","⚙️","🪢","📎","🔧","🧱","🪄","🧮"]

def split_ru_vi(title):
    m=re.match(r'^(.*?)\s*\(([^()]*)\)\s*$', title)
    if m and has_cyr(m.group(1)): return m.group(1).strip(), m.group(2).strip()
    return title, ""

doc=Document(SRC)
units=[]; cur=None; cur_sec=None; glossary={}; pending=[]
book_title_ru=[]
STOP_VI=('giống','số ít','số nhiều','lưu ý','gợi ý','mẫu','số','cách','danh từ','tính từ','động từ')

def new_unit(ru, vi, kind='topic'):
    global cur, cur_sec
    n=len(units)+1
    uid=f"{BOOK[:3]}-{n:02d}"   # e.g. gra-01  (unique vs book1 ids)
    cur=dict(id=uid, num=n, ru=ru, vi=vi or ru, kind=kind,
             icon=ICONS[(n-1)%len(ICONS)], color=PALETTE[(n-1)%len(PALETTE)],
             sectionPrefix=uid+"-s", sections=[])
    units.append(cur); cur_sec=None

def new_section(stype, title, num=None):
    global cur_sec
    sid=f"{cur['id']}-s{len(cur['sections'])+1:03d}"
    cur_sec=dict(id=sid, type=stype, title=title, num=num, blocks=[])
    cur['sections'].append(cur_sec)

def classify(t):
    low=t.lower()
    if low.startswith(('nb','n.b')) or low.startswith('lưu ý'): return 'note'
    if t.startswith('!'): return 'note'
    if low.startswith(('образец','модель','mẫu','mô hình')): return 'model'
    if re.match(r'^[а-дabc]\)\s*', t) and len(t)<=70: return 'subhead'
    if low.startswith(('chú ý','ghi nhớ')): return 'note'
    return 'para'

def add_glossary_from(text):
    for chunk in re.split(r'[;,]', text):
        m=re.match(r'^\s*(.+?)\s*\(([^()]+)\)\s*\.?\s*$', chunk)
        if not m: continue
        ru, vi=m.group(1).strip(' .'), m.group(2).strip()
        if not has_cyr(ru) or has_cyr(vi): continue
        if not LAT.search(vi): continue
        if len(ru)>40 or len(vi)>70: continue
        if any(s in vi.lower() for s in STOP_VI): continue
        ru=re.sub(r'^[а-дabвг]\)\s*','',ru)
        key=norm_ru(ru)
        if key and 1<len(key)<=40 and key not in glossary:
            glossary[key]=dict(ru=ru, ruPlain=strip_stress(ru), vi=vi, g=None, ref=cur_sec['id'] if cur_sec else '')

for p in doc.paragraphs:
    s=p.style.name; t=p.text.strip()
    if not t: continue
    if s=='Title': book_title_ru.append(t); continue
    if s=='Heading 1':
        up=t.upper()
        if 'LỜI NÓI ĐẦU' in up: new_unit('Введение','Lời nói đầu','intro'); continue
        if 'ПОВТОРЕНИЯ' in up or 'ÔN TẬP' in up: new_unit('Материал для повторения','Ôn tập — Раздел 1','review'); continue
        if up.startswith('РАЗДЕЛ') or 'СЛОВОСОЧЕТАНИЕ' in up:
            pending.append(dict(t='subhead', text=t)); continue
        # other H1
        new_unit(*split_ru_vi(t)); continue
    if s=='Heading 2':
        ru,vi=split_ru_vi(t)
        if cur is None or cur.get('kind')=='intro' or norm_ru(ru)!=norm_ru(cur['ru']):
            new_unit(ru,vi,'topic')
            if pending: 
                new_section('grammar','Giới thiệu'); cur_sec['blocks'].extend(pending); pending=[]
        # else: consecutive duplicate -> merge (ignore)
        continue
    if s=='Heading 3':
        if cur is None: new_unit('Словосочетание','Cụm từ','topic')
        m=re_ex.match(t)
        if m:
            new_section('exercise', t, num=int(m.group(1)))
        else:
            m2=re_numex.match(t)
            if m2:
                new_section('exercise', f"Bài {m2.group(1)}", num=int(m2.group(1)))
                cur_sec['blocks'].append(dict(t='instruction', text=m2.group(2).strip()))
            else:
                new_section('exercise', t)
        continue
    # Normal
    if cur is None: new_unit('Словосочетание','Cụm từ','topic')
    if cur_sec is None: new_section('grammar', cur['vi'])
    kind=classify(t)
    if cur_sec['type']=='exercise' and kind=='para' and not any(b['t']=='instruction' for b in cur_sec['blocks']) and not has_cyr(t):
        kind='instruction'
    blk=dict(t=kind, text=t); cur_sec['blocks'].append(blk)
    if has_cyr(t): add_glossary_from(t)

# disambiguate duplicate display titles
from collections import Counter
seen=Counter()
for u in units:
    base=u['vi']; seen[base]+=1
    if seen[base]>1: u['vi']=f"{base} ({seen[base]})"

# write
book=dict(id=BOOK,
    title="Ngữ pháp tiếng Nga — Cú pháp",
    subtitle="Грамматика русского языка. Часть 2: Синтаксис (Cú pháp)",
    lang="ru", uiLang="vi", level="B1–C1", cover="📗",
    description="Ngữ pháp tiếng Nga qua bài tập và chú giải — Phần 2: Cú pháp. Раздел 1: Cụm từ (словосочетание) — hợp dạng, điều khiển, giới từ, tiếp hợp, kèm lời giải song ngữ.",
    parts=[])
for u in units:
    fn=u['id']+".json"
    unit=dict(id=u['id'],num=u['num'],title=u['vi'],vi=u['vi'],ru=u['ru'],
              icon=u['icon'],color=u['color'],sectionPrefix=u['sectionPrefix'],sections=u['sections'])
    json.dump(unit, open(os.path.join(OUT,"units",fn),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
    n_ex=sum(1 for s in u['sections'] if s['type']=='exercise')
    n_gr=sum(1 for s in u['sections'] if s['type']!='exercise')
    book['parts'].append(dict(id=u['id'],num=u['num'],title=u['vi'],vi=u['vi'],ru=u['ru'],
        icon=u['icon'],color=u['color'],file=f"units/{fn}",sectionPrefix=u['sectionPrefix'],
        sectionCount=len(u['sections']),exerciseCount=n_ex,grammarCount=n_gr))
json.dump(book, open(os.path.join(OUT,"book.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=1)
gloss=sorted(glossary.values(), key=lambda e:e['ruPlain'].lower())
json.dump(dict(count=len(gloss),entries=gloss), open(os.path.join(OUT,"glossary.json"),"w",encoding="utf-8"), ensure_ascii=False, indent=1)

print("UNITS:",len(units))
for u in units:
    n_ex=sum(1 for s in u['sections'] if s['type']=='exercise')
    print(f"  {u['id']} ex={n_ex:>3} sec={len(u['sections']):>3}  {u['vi'][:52]}")
print("GLOSSARY:",len(gloss))
print("total sections:",sum(len(u['sections']) for u in units),
      "blocks:",sum(len(s['blocks']) for u in units for s in u['sections']))
