# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(os.path.abspath(__file__))

UNIT_ID = "skazki1-049"
SEC = "skazki1-049-s001"

note = ("Đây là dị bản Afanasyev (№89) của truyện tích luỹ trứ danh «Репка» — bản tiếng Việt "
        "thường gọi là «Củ cải khổng lồ». Khác bản quen thuộc (ông–bà–cháu–chó–mèo–chuột), ở bản "
        "này sau con chó lại là… những «cái chân» kéo đến từng cái một cho đến cái thứ năm — chính "
        "người sưu tầm cũng ngờ chữ chép sai nên đánh dấu «но́га (?)». Mỗi lần thêm một «người kéo», "
        "cả dây chuyền lại được nhắc trọn vẹn: đó là nhịp điệu tích luỹ làm nên sức hút của truyện.")

paras = [
  ("Посеял дедка репку; пошел репку рвать, захватился за репку: тянет-потянет, вытянуть не может!",
   "Ông lão gieo một củ cải; đến kỳ ra nhổ, ông túm lấy củ cải mà kéo: kéo mãi, kéo mãi, chẳng tài nào nhổ lên được!"),
  ("Со́звал дедка бабку; бабка за дедку, дедка за репку, тянут-потянут, вытянуть не можут!",
   "Ông lão gọi bà lão tới; bà lão níu lấy ông lão, ông lão túm củ cải, cả hai cùng kéo, cùng kéo mà vẫn chẳng nhổ lên được!"),
  ("Пришла внучка; внучка за бабку, бабка за дедку, дедка за репку, тянут-потянут, вытянуть не можут!",
   "Cô cháu gái chạy đến; cháu gái níu lấy bà, bà níu lấy ông, ông túm củ cải, cùng kéo cùng kéo mà vẫn chẳng nhổ lên được!"),
  ("Пришла сучка; сучка за внучку, внучка за бабку, бабка за дедку, дедка за репку, тянут-потянут, вытянуть не можут!",
   "Con chó cái chạy đến; chó níu lấy cháu gái, cháu gái níu bà, bà níu ông, ông túm củ cải, cùng kéo cùng kéo mà vẫn chẳng nhổ lên được!"),
  ("Пришла но́га (?).",
   "Rồi một cái chân chạy đến (?)."),
  ("Но́га за сучку, сучка за внучку, внучка за бабку, бабка за дедку, дедка за репку, тянут-потянут, вытянуть не можут!",
   "Cái chân níu lấy con chó, chó níu cháu gái, cháu gái níu bà, bà níu ông, ông túm củ cải, cùng kéo cùng kéo mà vẫn chẳng nhổ lên được!"),
  ("Пришла дру́га но́га; дру́га но́га за но́гу, но́га за сучку, сучка за внучку, внучка за бабку, бабка за дедку, дедка за репку, тянут-потянут, вытянуть не можут! (и так далее до пятой но́ги).",
   "Cái chân thứ hai chạy đến; chân thứ hai níu lấy chân kia, chân kia níu con chó, chó níu cháu gái, cháu gái níu bà, bà níu ông, ông túm củ cải, cùng kéo cùng kéo mà vẫn chẳng nhổ lên được! (và cứ thế tiếp tục cho đến cái chân thứ năm)."),
  ("Пришла пя́та но́га.",
   "Cái chân thứ năm chạy đến."),
  ("Пять ног за четыре, четыре но́ги за три, три но́ги за две, две но́ги за но́гу, но́га за сучку, сучка за внучку, внучка за бабку, бабка за дедку, дедка за репку, тянут-потянут: вытянули репку!",
   "Năm chân níu lấy bốn chân, bốn chân níu ba chân, ba chân níu hai chân, hai chân níu một chân, chân ấy níu con chó, chó níu cháu gái, cháu gái níu bà, bà níu ông, ông túm củ cải, cùng kéo cùng kéo: thế là cả bọn nhổ bật được củ cải lên!"),
]

# (ru_display, vi, add_to_glossary)
vocab = [
  ("репка", "củ cải (dạng thân mật của «репа»; bản tiếng Việt quen gọi «củ cải khổng lồ»)", True),
  ("посеять", "gieo, trồng (hạt giống)", True),
  ("дедка", "ông lão (dạng thân mật của «дед» — ông)", True),
  ("бабка", "bà lão (dạng thân mật của «баба» — bà)", True),
  ("внучка", "cháu gái", False),  # đã có sẵn trong glossary
  ("сучка", "con chó cái (dạng thân mật của «сука»)", True),
  ("но́га", "cái chân, bàn chân — ở dị bản này là chi tiết kỳ lạ; người sưu tầm đánh dấu «(?)» vì ngờ chữ chép sai", True),
  ("захвати́ться (за)", "túm chặt, bám lấy", True),
  ("созва́ть", "gọi đến, gọi tới giúp", True),
  ("вы́тянуть", "nhổ lên, kéo bật lên được", True),
  ("тяну́ть-потяну́ть", "kéo mãi kéo mãi (lối nói láy dân gian)", True),
  ("мо́жут", "dạng phương ngữ/cổ của «могут» (có thể) — Afanasyev giữ nguyên giọng kể địa phương", True),
  ("дру́га / пя́та", "dạng rút gọn phương ngữ của «другая / пятая» (cái kia / cái thứ năm)", True),
]

blocks = [{"t": "note", "text": note}]
for ru, vi in paras:
    blocks.append({"t": "para", "text": "%s (%s)" % (ru, vi)})
blocks.append({"t": "subhead", "text": "Từ khó trong truyện"})
for ru, vi, _add in vocab:
    blocks.append({"t": "vocab", "ru": ru, "vi": vi, "g": None})

unit = {
  "id": UNIT_ID,
  "num": 49,
  "title": "Репка — Củ cải",
  "vi": "Репка — Củ cải",
  "ru": "Репка",
  "icon": "🥕",
  "color": "#d97706",
  "sectionPrefix": "skazki1-049-s",
  "group": "Truyện № 61–100",
  "sections": [
    {
      "id": SEC,
      "type": "story",
      "num": 89,
      "title": "№ 89 · Репка — Củ cải",
      "blocks": blocks,
    }
  ],
}

unit_path = os.path.join(BASE, "units", "skazki1-049.json")
with open(unit_path, "w", encoding="utf-8") as f:
    json.dump(unit, f, ensure_ascii=False, indent=1)
print("WROTE unit:", unit_path, "| paras:", len(paras), "| vocab:", len(vocab))

# ---- glossary ----
def strip_accent(s):
    return s.replace("́", "").replace("̀", "")

gpath = os.path.join(BASE, "glossary.json")
g = json.load(open(gpath, encoding="utf-8"))
before = len(g["entries"])
added = 0
for ru, vi, add in vocab:
    if not add:
        continue
    plain = strip_accent(ru)
    g["entries"].append({"ru": ru, "ruPlain": plain, "vi": vi, "g": None, "ref": SEC})
    added += 1
g["count"] = len(g["entries"])
with open(gpath, "w", encoding="utf-8") as f:
    json.dump(g, f, ensure_ascii=False, indent=1)
print("GLOSSARY:", before, "->", g["count"], "(+%d new)" % added)

# ---- book.json: add part skazki1-049 ----
bpath = os.path.join(BASE, "book.json")
b = json.load(open(bpath, encoding="utf-8"))
ids = {p["id"] for p in b["parts"]}
if UNIT_ID in ids:
    print("BOOK: part already exists, skipping add")
else:
    part = {
      "id": UNIT_ID, "num": 49,
      "title": "Репка — Củ cải", "vi": "Репка — Củ cải", "ru": "Репка",
      "icon": "🥕", "color": "#d97706",
      "file": "units/skazki1-049.json",
      "sectionPrefix": "skazki1-049-s",
      "group": "Truyện № 61–100",
      "sectionCount": 1, "exerciseCount": 0, "grammarCount": 0,
    }
    b["parts"].append(part)
    b["parts"].sort(key=lambda p: p.get("num", 0))
    with open(bpath, "w", encoding="utf-8") as f:
        json.dump(b, f, ensure_ascii=False, indent=1)
    print("BOOK: added part skazki1-049; parts now", len(b["parts"]))
