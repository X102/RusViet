# -*- coding: utf-8 -*-
"""Build unit skazki1-043 «Жадная старуха» (№76). Chỉ sửa data/books/skazki1/**."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
UID = "skazki1-043"
SEC = "skazki1-043-s001"

note = ("Truyện ngụ ngôn dân gian «Bà lão tham lam» (kiểu ATU 555 «Ông lão, bà lão và "
        "con cá» — họ hàng với «Cá vàng» №75 và «Người đánh cá và vợ» của anh em Grimm). "
        "Thay cho con cá thần là một cây cổ thụ biết nói đền ơn ông lão; lòng tham của bà lão "
        "leo thang không ngừng — từ giàu có, lên xã trưởng, quan địa chủ, đại tá, tướng quân, "
        "vua, rồi đòi làm cả thần thánh — để cuối cùng cả hai bị biến thành gấu chạy vào rừng. "
        "Mỗi nấc thang quyền lực lại đi kèm một câu giễu «велико ли дело» (to tát gì) và một "
        "mối lo sợ kẻ trên đè kẻ dưới, vẽ nên bức biếm họa về tham vọng vô độ.")

pairs = [
 ("Жил старик со старухою; пошел в лес дрова рубить.",
  "Ngày xưa có một ông lão sống với bà lão; một hôm ông vào rừng đốn củi."),
 ("Сыскал старое дерево, поднял топор и стал рубить.",
  "Ông tìm được một cây cổ thụ, giơ rìu lên và bắt đầu chặt."),
 ("Говорит ему дерево: «Не руби меня, мужичок! Что тебе надо, все сделаю».",
  "Cây bèn nói với ông: «Đừng chặt ta, ông lão ơi! Ông cần gì, ta sẽ làm cho nấy.»"),
 ("— «Ну, сделай, чтобы я богат был».",
  "— «Thế thì hãy làm cho ta được giàu có đi.»"),
 ("— «Ладно; ступай домой, всего у тебя вдоволь будет».",
  "— «Được thôi; ông cứ về nhà đi, rồi thứ gì ông cũng có dư dả.»"),
 ("Воротился старик домой — изба новая, словно чаша полная, денег куры не клюют, хлеба на десятки лет хватит, а что коров, лошадей, овец — в три дня не сосчитать!",
  "Ông lão trở về nhà — nhà gỗ mới tinh, của nả đầy ăm ắp như chén đầy, tiền nhiều đến gà mổ chẳng xuể, lúa mì đủ ăn mấy chục năm, còn bò, ngựa, cừu thì ba ngày cũng đếm không xuể!"),
 ("«Ах, старик, откуда все это?» — спрашивает старуха.",
  "«Ơ kìa ông lão, đâu ra lắm thế này?» — bà lão hỏi."),
 ("«Да вот, жена, я такое дерево нашел — что ни пожелай, то и сделает».",
  "«Thì đấy bà nó ạ, tôi tìm được một cái cây như thế đấy — hễ ước gì là nó làm cho nấy.»"),
 ("Пожили с месяц; приелось старухе богатое житье, говорит старику:",
  "Sống được chừng một tháng; bà lão đâm chán cảnh giàu sang, bèn bảo ông lão:"),
 ("«Хоть живем мы богато, да что в этом толку, коли люди нас не почитают!",
  "«Tuy mình sống giàu có thật đấy, nhưng phỏng có ích gì khi người ta chẳng nể trọng mình!"),
 ("Захочет бурмистр, и тебя и меня на работу погонит; а придерется, так и палками накажет.",
  "Lão xã trưởng muốn là lùa cả ông lẫn tôi đi làm xâu; mà hễ kiếm cớ thì còn lấy gậy đánh phạt nữa."),
 ("Ступай к дереву, проси, чтоб ты бурмистром был».",
  "Ông hãy đến chỗ cái cây, xin cho ông được làm xã trưởng đi.»"),
 ("Взял старик топор, пошел к дереву и хочет под самый корень рубить.",
  "Ông lão cầm rìu, đi đến chỗ cái cây và toan chặt sát tận gốc."),
 ("«Что тебе надо?» — спрашивает дерево.",
  "«Ông cần gì?» — cây hỏi."),
 ("«Сделай, чтобы я бурмистром был».",
  "«Hãy làm cho ta được làm xã trưởng.»"),
 ("— «Хорошо, ступай с богом!»",
  "— «Được, ông cứ về đi, cầu Chúa phù hộ!»"),
 ("Воротился домой, а его уж давно солдаты дожидают:",
  "Ông về đến nhà thì bọn lính đã chực sẵn từ lâu:"),
 ("«Где ты, — закричали, — старый черт, шатаешься?",
  "«Mày đi đâu — chúng quát lên — lão quỷ già, lê la ở xó nào thế?"),
 ("Отводи скорей нам квартиру, да чтоб хорошая была. Ну-ну, поворачивайся!»",
  "Mau xếp chỗ trọ cho bọn ta, mà phải chỗ tử tế đấy. Nào nào, nhanh tay lên!»"),
 ("А сами тесаками его по горбу да по горбу.",
  "Rồi chúng cứ lấy đốc gươm mà nện vào lưng ông, hết cái này đến cái khác."),
 ("Видит старуха, что и бурмистру не всегда честь, и говорит старику:",
  "Bà lão thấy làm xã trưởng cũng chẳng phải lúc nào cũng được nể vì, bèn bảo ông lão:"),
 ("«Что за корысть быть бурмистровой женою!",
  "«Làm vợ xã trưởng thì bõ bèn gì!"),
 ("Вот тебя солдаты прибили, а уж о барине и говорить нечего: что захочет, то и сделает.",
  "Ông thì bị lính nó đánh, còn quan địa chủ thì khỏi phải nói: muốn gì được nấy."),
 ("Ступай-ка ты к дереву да проси, чтоб сделало тебя барином, а меня барыней».",
  "Ông hãy đến chỗ cái cây mà xin cho ông thành quan địa chủ, còn tôi thành bà lớn.»"),
 ("Взял старик топор, пошел к дереву, хочет опять рубить; дерево спрашивает:",
  "Ông lão cầm rìu, đi đến chỗ cái cây, lại toan chặt; cây hỏi:"),
 ("«Что тебе надо, старичок?»",
  "«Ông cần gì, ông lão?»"),
 ("— «Сделай меня барином, а старуху барыней».",
  "— «Hãy làm cho ta thành quan địa chủ, còn bà lão nhà ta thành bà lớn.»"),
 ("— «Хорошо, ступай с богом!»",
  "— «Được, ông cứ về đi, cầu Chúa phù hộ!»"),
 ("Пожила старуха в барстве, захотелось ей большего, говорит старику:",
  "Bà lão sống trong cảnh quan sang được ít lâu, lại muốn hơn nữa, bèn bảo ông lão:"),
 ("«Что за корысть, что я барыня!",
  "«Làm bà lớn thì bõ bèn gì!"),
 ("Вот кабы ты был полковником, а я полковницей — иное дело, все бы нам завидовали».",
  "Giá mà ông làm đại tá, còn tôi làm phu nhân đại tá — thì lại khác, ai nấy đều phải thèm muốn ganh tị với mình.»"),
 ("Погнала старика снова к дереву; взял он топор, пришел и собирается рубить.",
  "Bà lại giục ông lão đến chỗ cái cây; ông cầm rìu, đến nơi và sắp sửa chặt."),
 ("Спрашивает его дерево: «Что тебе надобно?»",
  "Cây hỏi ông: «Ông cần gì?»"),
 ("— «Сделай меня полковником, а старуху полковницей».",
  "— «Hãy làm cho ta thành đại tá, còn bà lão nhà ta thành phu nhân đại tá.»"),
 ("— «Хорошо, ступай с богом!»",
  "— «Được, ông cứ về đi, cầu Chúa phù hộ!»"),
 ("Воротился старик домой, а его полковником пожаловали.",
  "Ông lão về đến nhà thì đã được phong làm đại tá."),
 ("Прошло несколько времени, говорит ему старуха: «Велико ли дело — полковник!",
  "Ít lâu sau, bà lão lại bảo ông: «Đại tá thì to tát gì!"),
 ("Генерал захочет, под арест посадит.",
  "Tướng quân muốn là tống ông vào ngục như chơi."),
 ("Ступай к дереву, проси, чтобы сделало тебя генералом, а меня генеральшею».",
  "Ông hãy đến chỗ cái cây, xin cho ông thành tướng quân, còn tôi thành phu nhân tướng quân.»"),
 ("Пошел старик к дереву, хочет топором рубить.",
  "Ông lão đi đến chỗ cái cây, toan vung rìu chặt."),
 ("«Что тебе надобно?» — спрашивает дерево.",
  "«Ông cần gì?» — cây hỏi."),
 ("«Сделай меня генералом, а старуху генеральшею».",
  "«Hãy làm cho ta thành tướng quân, còn bà lão nhà ta thành phu nhân tướng quân.»"),
 ("— «Хорошо, иди с богом!»",
  "— «Được, ông cứ đi đi, cầu Chúa phù hộ!»"),
 ("Воротился старик домой, а его в генералы произвели.",
  "Ông lão về đến nhà thì đã được thăng làm tướng quân."),
 ("Опять прошло несколько времени, наскучило старухе быть генеральшею, говорит она старику: «Велико ли дело — генерал!",
  "Lại ít lâu trôi qua, bà lão đâm chán cảnh làm phu nhân tướng quân, bèn bảo ông lão: «Tướng quân thì to tát gì!"),
 ("Государь захочет, в Сибирь сошлет.",
  "Đức vua muốn là đày đi Xi-bia như chơi."),
 ("Ступай к дереву, проси, чтобы сделало тебя царем, а меня царицею».",
  "Ông hãy đến chỗ cái cây, xin cho ông thành vua, còn tôi thành hoàng hậu.»"),
 ("Пришел старик к дереву, хочет топором рубить.",
  "Ông lão đến chỗ cái cây, toan vung rìu chặt."),
 ("«Что тебе надобно?» — спрашивает дерево.",
  "«Ông cần gì?» — cây hỏi."),
 ("«Сделай меня царем, а старуху царицею».",
  "«Hãy làm cho ta thành vua, còn bà lão nhà ta thành hoàng hậu.»"),
 ("— «Хорошо, иди с богом!»",
  "— «Được, ông cứ đi đi, cầu Chúa phù hộ!»"),
 ("Воротился старик домой, а за ним уж послы приехали: «Государь-де помер, тебя на его место выбрали».",
  "Ông lão về đến nhà thì sứ giả đã tới đón: «Đức vua băng hà rồi, người ta đã chọn ông lên thay ngôi.»"),
 ("Не много пришлось старику со старухой нацарствовать; показалось старухе мало быть царицею, позвала старика и говорит ему: «Велико ли дело — царь!",
  "Ông lão với bà lão chẳng được trị vì bao lâu; bà lão thấy làm hoàng hậu vẫn còn ít, bèn gọi ông lão đến mà bảo: «Làm vua thì to tát gì!"),
 ("Бог захочет, смерть нашлет, и запрячут тебя в сырую землю.",
  "Chúa Trời muốn là gieo cái chết xuống, rồi người ta vùi ông xuống lòng đất ẩm lạnh."),
 ("Ступай-ка ты к дереву да проси, чтобы сделало нас богами».",
  "Ông hãy đến chỗ cái cây mà xin cho vợ chồng mình thành thần thánh đi.»"),
 ("Пошел старик к дереву.",
  "Ông lão đi đến chỗ cái cây."),
 ("Как услыхало оно эти безумные речи, зашумело листьями и в ответ старику молвило: «Будь же ты медведем, а твоя жена медведицей».",
  "Cây vừa nghe những lời điên rồ ấy, liền xào xạc lá rồi đáp lại ông lão: «Vậy thì ông hãy hóa thành gấu đực, còn vợ ông hóa thành gấu cái!»"),
 ("В ту ж минуту старик обратился медведем, а старуха медведицей, и побежали в лес.",
  "Ngay phút ấy, ông lão biến thành gấu đực, bà lão biến thành gấu cái, rồi cả hai chạy biến vào rừng."),
]

# Từ khó (ru có dấu trọng âm, ruPlain bỏ dấu) — đã đối soát glossary
vocab = [
 ("бурми́стр", "бурмистр", "xã trưởng, lý trưởng — người được địa chủ cử ra cai quản, đốc thúc nông nô"),
 ("теса́к", "тесак", "đoản đao, dao quắm; gươm ngắn lính tráng đeo bên hông (тесаками по горбу — lấy đốc gươm nện vào lưng)"),
 ("горб", "горб", "cái lưng, bướu lưng (по горбу — nện vào lưng)"),
 ("придра́ться", "придраться", "kiếm cớ bắt bẻ, vạch lá tìm sâu, gây sự"),
 ("коры́сть", "корысть", "cái lợi, mối hời (что за корысть — phỏng được ích gì, bõ bèn gì)"),
 ("ба́рин", "барин", "ông lớn, quan địa chủ (chủ đất, quý tộc)"),
 ("ба́рыня", "барыня", "bà lớn, bà chủ (vợ địa chủ, quý bà)"),
 ("пожа́ловать", "пожаловать", "ban thưởng, phong (chức tước) — полковником пожаловали: được phong làm đại tá"),
 ("произвести́", "произвести", "thăng cấp, phong hàm (в генералы произвели: được thăng làm tướng)"),
 ("нацарствова́ться", "нацарствоваться", "trị vì cho thỏa, làm vua một thời (не много нацарствовать — chẳng trị vì được bao lâu)"),
 ("запря́тать", "запрятать", "vùi giấu, giấu kĩ, tống vào (запрячут в сырую землю — vùi xuống đất)"),
 ("сыра́я земля́", "сырая земля", "đất ẩm, lòng đất lạnh — lối nói uyển ngữ chỉ nấm mồ"),
 ("прие́сться", "приесться", "đâm chán ngấy, phát ngán (приелось житьё — chán cảnh sống)"),
 ("сыска́ть", "сыскать", "(cổ = найти) tìm được, kiếm thấy"),
 ("почита́ть", "почитать", "kính trọng, nể vì, coi trọng"),
]

# ---- build unit JSON ----
blocks = [{"t": "note", "text": note}]
for ru, vi in pairs:
    blocks.append({"t": "para", "text": "%s (%s)" % (ru, vi)})
blocks.append({"t": "subhead", "text": "Từ khó trong truyện"})
for ru, plain, vi in vocab:
    blocks.append({"t": "vocab", "ru": ru, "vi": vi, "g": None})

unit = {
 "id": UID, "num": 43,
 "title": "Жадная старуха — Bà lão tham lam",
 "vi": "Жадная старуха — Bà lão tham lam",
 "ru": "Жадная старуха",
 "icon": "🐻", "color": "#7c2d12",
 "sectionPrefix": "skazki1-043-s",
 "group": "Truyện № 61–100",
 "sections": [
  {"id": SEC, "type": "story", "num": 76,
   "title": "№ 76 · Жадная старуха — Bà lão tham lam",
   "blocks": blocks},
 ],
}
unit_path = os.path.join(HERE, "units", "skazki1-043.json")
json.dump(unit, open(unit_path, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote", unit_path, "| paras:", len(pairs), "| vocab:", len(vocab))

# ---- update glossary.json ----
gpath = os.path.join(HERE, "glossary.json")
g = json.load(open(gpath, encoding="utf-8"))
have = {e["ruPlain"] for e in g["entries"]}
added = 0
for ru, plain, vi in vocab:
    if plain in have:
        print("  skip dup:", plain); continue
    g["entries"].append({"ru": ru, "ruPlain": plain, "vi": vi, "g": None, "ref": SEC})
    have.add(plain); added += 1
g["count"] = len(g["entries"])
json.dump(g, open(gpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("glossary: +%d entries -> count=%d" % (added, g["count"]))

# ---- update book.json ----
bpath = os.path.join(HERE, "book.json")
b = json.load(open(bpath, encoding="utf-8"))
if any(p["id"] == UID for p in b["parts"]):
    print("book.json already has", UID)
else:
    part = {
     "id": UID, "num": 43,
     "title": "Жадная старуха — Bà lão tham lam",
     "vi": "Жадная старуха — Bà lão tham lam",
     "ru": "Жадная старуха",
     "icon": "🐻", "color": "#7c2d12",
     "file": "units/skazki1-043.json",
     "sectionPrefix": "skazki1-043-s",
     "group": "Truyện № 61–100",
     "sectionCount": 1, "exerciseCount": 0, "grammarCount": 0,
    }
    b["parts"].append(part)
    b["parts"].sort(key=lambda p: p["num"])
    json.dump(b, open(bpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("book.json: added part", UID, "| total parts:", len(b["parts"]))
