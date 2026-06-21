# -*- coding: utf-8 -*-
import json, os

BOOK_DIR = os.path.dirname(os.path.abspath(__file__))
UNIT_PATH = os.path.join(BOOK_DIR, "units", "skazki1-050.json")
GLOS_PATH = os.path.join(BOOK_DIR, "glossary.json")
BOOK_PATH = os.path.join(BOOK_DIR, "book.json")
REF = "skazki1-050-s001"

def strip_stress(s):
    return s.replace("́", "")

# ---- Unit JSON ----
unit = {
    "id": "skazki1-050",
    "num": 50,
    "title": "Грибы — Các loài nấm",
    "vi": "Грибы — Các loài nấm",
    "ru": "Грибы",
    "icon": "\U0001F344",   # mushroom
    "color": "#a16207",
    "sectionPrefix": "skazki1-050-s",
    "group": "Truyện № 61–100",
    "sections": [
        {
            "id": REF,
            "type": "story",
            "num": 90,
            "title": "№ 90 · Грибы — Các loài nấm",
            "blocks": [
                {"t": "note", "text": "Đây chính là «Война грибов» (Cuộc chiến của các loài nấm) — một truyện kể - đồng dao dân gian Nga rất nổi tiếng, được Afanasyev ghi lại ở dạng cực ngắn. Nấm vua boletus tự xưng thủ lĩnh, lần lượt triệu các loài nấm ra trận; mỗi loài thoái thác bằng một câu có vần đối ngay với chính tên mình (белянки–дворянки, рыжики–мужики, волнушки–стряпушки, опёнки–тонки), chỉ riêng đám nấm sữa груздь đồng lòng ra trận (грузди–дружны). Vần điệu đối đáp ấy là linh hồn của truyện — bản dịch cố giữ lối nói gọn, có nhịp; phần vần gốc được chú trong mục từ khó."},

                {"t": "para", "text": "Вздумал гриб, разгадал боровик; под дубочком сидючи, на все грибы глядючи, стал приказывать: (Một cây nấm nảy ra ý, nấm vua boletus ngẫm cho thông suốt; ngồi dưới gốc sồi non, đưa mắt nhìn khắp lượt các loài nấm, nó bèn ra lệnh:)"},

                {"t": "para", "text": "«Приходите вы, белянки, ко мне на войну». («Này các nàng nấm trắng, hãy đến đây ra trận cùng ta!»)"},
                {"t": "para", "text": "Отказалися белянки: «Мы грибовые дворянки, не идем на войну». (Đám nấm trắng từ chối: «Chúng tôi là tiểu thư quý tộc nhà nấm, không đi đánh trận đâu.»)"},

                {"t": "para", "text": "«Приходите, рыжики́, ко мне на войну». («Này các chú nấm hung, hãy đến đây ra trận cùng ta!»)"},
                {"t": "para", "text": "Отказались рыжики́: «Мы богатые мужики, неповинны на войну идти». (Đám nấm hung từ chối: «Chúng tôi là những gã trai làng giàu có, chẳng có phận sự gì phải ra trận.»)"},

                {"t": "para", "text": "«Приходите вы, волнушки, ко мне на войну». («Này các ả nấm sóng, hãy đến đây ra trận cùng ta!»)"},
                {"t": "para", "text": "Отказалися волнушки: «Мы господские стряпушки, не идем на войну». (Đám nấm sóng từ chối: «Chúng tôi là đám chị bếp hầu nhà chủ, không đi đánh trận đâu.»)"},

                {"t": "para", "text": "«Приходите вы, опенки, ко мне на войну». («Này các chú nấm gốc cây, hãy đến đây ra trận cùng ta!»)"},
                {"t": "para", "text": "Отказалися опенки: «У нас ноги очень тонки, мы нейдем на войну». (Đám nấm gốc cây từ chối: «Chân cẳng chúng tôi mảnh khảnh lắm, chúng tôi chẳng ra trận được đâu.»)"},

                {"t": "para", "text": "«Приходите, грузди, ко мне на войну». («Này các bác nấm sữa, hãy đến đây ra trận cùng ta!»)"},
                {"t": "para", "text": "«Мы, грузди, — ребятушки дружны, пойдем на войну!» («Bọn tôi, đám nấm sữa, là những chàng trai một lòng đoàn kết, bọn tôi sẽ ra trận!»)"},

                {"t": "para", "text": "Это было, как царь-горох воевал с грибами. (Chuyện ấy có từ thuở Vua Đậu đem quân đánh nhau với các loài nấm — tức là từ thời xa lơ xa lắc.)"},

                {"t": "subhead", "text": "Từ khó trong truyện"},
            ]
        }
    ]
}

# ---- Vocab (also goes to glossary) ----
vocab = [
    ("боровик", "nấm vua, nấm trắng (Boletus edulis) — được coi là «vua» của các loài nấm; ở đây là kẻ cầm đầu đòi triệu quân"),
    ("белянка", "một loài nấm trắng (Lactarius pubescens); ở đây chơi chữ với дворянка (nữ quý tộc)"),
    ("дворянка", "nữ quý tộc, tiểu thư dòng dõi"),
    ("рыжи́к", "nấm hung, nấm thông đỏ (Lactarius deliciosus); chơi chữ với мужик (gã đàn ông, trai làng)"),
    ("волнушка", "nấm sóng (Lactarius torminosus, mũ có vân tròn như sóng); chơi chữ với стряпушка"),
    ("стряпушка", "chị bếp, người nấu ăn (hầu hạ nhà chủ)"),
    ("опёнок", "nấm gốc cây, nấm mật (mọc thành chùm trên gốc cây, cuống mảnh); số nhiều опёнки — chơi chữ với тонки (mảnh khảnh)"),
    ("груздь", "nấm sữa (Lactarius resimus) — loài nấm «chắc nịch», được dân Nga coi là nấm quý; số nhiều грузди, chơi chữ với дружны (đồng lòng)"),
    ("сидючи / глядючи", "dạng phó động từ cổ (= сидя / глядя: đang ngồi / đang ngắm nhìn)"),
    ("неповинны", "không có lỗi, vô can — ở đây nghĩa «chẳng có phận sự phải» (đi đánh trận)"),
    ("нейдём", "dạng cổ/phương ngữ của «не идём» (chúng tôi không đi)"),
    ("ребятушки", "các chàng trai (dạng thân mật, trìu mến của «ребята»)"),
    ("царь-горох", "«Vua Đậu» — nhân vật tục ngữ tượng trưng thời thượng cổ xa lắc; thành ngữ «при царе Горохе» = «thời xửa thời xưa»"),
]

# ---- Load glossary, find existing ruPlain ----
glos = json.load(open(GLOS_PATH, encoding="utf-8"))
glos["entries"] = [e for e in glos["entries"] if e.get("ref") != REF]
existing = set(e.get("ruPlain", strip_stress(e["ru"])) for e in glos["entries"])

added = []
skipped = []
for ru, vi in vocab:
    plain = strip_stress(ru)
    block = {"t": "vocab", "ru": ru, "vi": vi, "g": None}
    unit["sections"][0]["blocks"].append(block)   # vocab shows in unit regardless
    if plain in existing:
        skipped.append(plain)
        continue
    glos["entries"].append({"ru": ru, "ruPlain": plain, "vi": vi, "g": None, "ref": REF})
    existing.add(plain)
    added.append(plain)

glos["count"] = len(glos["entries"])

# ---- Write unit ----
os.makedirs(os.path.dirname(UNIT_PATH), exist_ok=True)
json.dump(unit, open(UNIT_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---- Write glossary ----
json.dump(glos, open(GLOS_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ---- book.json: add part skazki1-050 ----
book = json.load(open(BOOK_PATH, encoding="utf-8"))
if not any(p["id"] == "skazki1-050" for p in book["parts"]):
    book["parts"].append({
        "id": "skazki1-050",
        "num": 50,
        "title": "Грибы — Các loài nấm",
        "vi": "Грибы — Các loài nấm",
        "ru": "Грибы",
        "icon": "\U0001F344",
        "color": "#a16207",
        "file": "units/skazki1-050.json",
        "sectionPrefix": "skazki1-050-s",
        "group": "Truyện № 61–100",
        "sectionCount": 1,
        "exerciseCount": 0,
        "grammarCount": 0,
    })
    book["parts"].sort(key=lambda p: p["num"])
json.dump(book, open(BOOK_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

print("UNIT paras:", sum(1 for b in unit["sections"][0]["blocks"] if b["t"]=="para"))
print("VOCAB in unit:", sum(1 for b in unit["sections"][0]["blocks"] if b["t"]=="vocab"))
print("glossary count now:", glos["count"])
print("added to glossary:", added)
print("skipped (dup):", skipped)
print("book parts:", len(book["parts"]))
