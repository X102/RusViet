# -*- coding: utf-8 -*-
import json, os

BASE = os.path.dirname(os.path.abspath(__file__))

paras = [
 ("У одного барина было много животины.",
  "Một ông địa chủ nọ có rất nhiều súc vật."),
 ("Только что он принял пять барашков, из шкурок ихних выделал овчинки и стал себе шубу шить.",
  "Vừa mới tậu về năm con cừu non, ông lột da chúng thuộc thành những tấm da cừu rồi định may cho mình một chiếc áo lông."),
 ("Призвал портного.",
  "Ông cho gọi thợ may đến."),
 ("«Ну, — бает, — сшей мне шубу».",
  "«Nào, — ông bảo, — may cho ta một chiếc áo lông.»"),
 ("Тот померил-померил; видит, что не хватит ему пол-овчинки на шубу.",
  "Bác thợ đo đi đo lại; thấy còn thiếu mất nửa tấm da cừu mới đủ may áo."),
 ("«Мало, — бает, — овчин, не хватает на клинья».",
  "«Da cừu ít quá, — bác bảo, — không đủ để chêm các miếng nối.»"),
 ("«Эвтому делу можно пособить», — бает барин и велел лакею своему у одного барана содрать шкурку с одного боку.",
  "«Việc ấy có thể chữa được», — ông địa chủ nói, rồi sai tên đầy tớ lột phăng da một bên sườn của một con cừu."),
 ("Лакей так и сделал, как барин баял.",
  "Tên đầy tớ làm y như lời ông chủ."),
 ("Только что этот баран рассерчал на барина, подозвал к себе козла.",
  "Con cừu ấy đùng đùng nổi giận với ông chủ, bèn gọi con dê đực lại."),
 ("«Пойдем, — бает, — от этакого лиходея; в лесу пока можно жить, травка есть, водицу найдем, сыты будем».",
  "«Đi thôi, — nó bảo, — bỏ cái lão ác nghiệt này đi; trong rừng còn sống được, có cỏ, kiếm được nước, no bụng chán.»"),
 ("Вот они и пошли.",
  "Thế là cả hai bỏ đi."),
 ("Пришли в лес, сладили шалашу́, и ну по ночам ночевать.",
  "Vào tới rừng, chúng dựng một túp lều, rồi cứ thế đêm đêm ngủ lại ở đó."),
 ("Живут себе да поживают да травку поедают.",
  "Cứ vậy chúng sống yên ổn, ngày ngày gặm cỏ qua ngày."),

 ("Только что у того барина жить не полюбилось не им одним.",
  "Hóa ra chẳng phải chỉ mình chúng mới chán sống ở nhà ông địa chủ ấy."),
 ("Ушли с того со двора корова да свинья, петух да гусак.",
  "Từ cái sân nhà ông, con bò cái với con lợn, con gà trống với con ngỗng đực cũng bỏ đi."),
 ("Вот они, пока было тепло, жили себе на воле, а как пришла зимушка-зима, и они стали прятаться от мороза.",
  "Khi trời còn ấm, chúng sống tự do ngoài trời, nhưng đến lúc mùa đông giá buốt kéo về, chúng bắt đầu tìm chỗ trốn rét."),
 ("Вот ходили, ходили по лесу, да и нашли шалашу́-то барана, и стали они проситься к нему: «Пусти, — бают, — нам ведь холодно».",
  "Chúng đi mãi, đi mãi trong rừng, rồi tìm ra túp lều của con cừu, bèn xin vào ở nhờ: «Cho vào với, — chúng kêu, — chúng tôi rét lắm rồi.»"),
 ("А они и знать не хотят, никого не пускают.",
  "Nhưng cừu với dê chẳng thèm để ý, không cho ai vào cả."),

 ("Вот корова подходит: «Пустите, — бает, — а не то всю вашу шалашу́ набок сворочу!»",
  "Con bò cái bước tới: «Cho vào đi, — nó bảo, — không thì tôi xô đổ nghiêng cả túp lều của các anh cho mà xem!»"),
 ("Баран видит, плохо дело, пустил её.",
  "Cừu thấy gay go, đành cho nó vào."),
 ("Подходит свинья: «Пустите, — бает, — а нет — так я всю землю изрою да таки подроюсь к вам; смотрите, вам же будет холоднее».",
  "Con lợn tiến tới: «Cho vào đi, — nó nói, — bằng không tôi sẽ ủi tung cả đất lên rồi đào ngầm chui vào chỗ các anh cho mà xem; liệu hồn, chính các anh lại càng thêm rét.»"),
 ("Делать нечего, и эту пустили.",
  "Chẳng còn cách nào, chúng cho cả nó vào."),
 ("Глядь — и гусак тоже бает: «Пустите, а не то я дыру проклюю, смотрите, вам же будет холоднее».",
  "Kìa — con ngỗng đực cũng lên tiếng: «Cho vào đi, không thì tôi mổ thủng một lỗ cho mà xem, liệu hồn, chính các anh lại càng thêm rét.»"),
 ("«Пустите, — бает и петун, — а не то всю крышу вашу обс..!»",
  "«Cho vào đi, — gà trống cũng nói, — không thì tôi ỉa vung cả mái nhà các anh lên cho coi...!»"),
 ("Что делать, пустили и этих, да и стали все они жить вместях.",
  "Biết làm sao, chúng cho nốt cả bọn này vào, thế là tất cả cùng chung sống với nhau."),

 ("Долго ль, коротко ль они жили, а однажды шли мимо их разбойники и услыхали крик да гам, подошли, послухали; не знают, что такое есть, и посылают одного своего товарища:",
  "Chúng sống với nhau lâu hay chóng chẳng rõ, nhưng một hôm có bọn cướp đi ngang qua, nghe thấy tiếng la hét om sòm; chúng lại gần, lắng tai nghe mà chẳng hiểu là cái gì, bèn sai một tên trong bọn:"),
 ("«Ступай, — бают, — а не то верёвку на шею, да и в воду!»",
  "«Vào xem đi, — chúng bảo, — không thì thừng tròng cổ rồi quẳng xuống nước cho chết!»"),
 ("Делать нечего, тот и пошёл.",
  "Chẳng còn cách nào, tên kia đành đi."),
 ("Как только взошёл, как начали его со всех сторон!",
  "Vừa mới bước vào, lập tức từ tứ phía cả bọn xông vào nện hắn tới tấp!"),
 ("Вот он, делать нечего, назад...",
  "Hắn ta hết cách, đành quay trở ra..."),
 ("«Ну, братцы, — бает, — что хотите делайте, а я уж ни за что не пойду.",
  "«Này anh em, — hắn nói, — các anh muốn làm gì tôi thì làm, chứ tôi thì có chết cũng chẳng dám vào nữa."),
 ("Этакого страха сродясь не видывал!",
  "Sinh ra đến giờ tôi chưa từng thấy nỗi khiếp đảm nào như thế!"),
 ("Только что взошёл, где ни возьмись — баба, да меня ухватом-то, да меня ухватом-то;",
  "Vừa bước vào, ở đâu nhào ra một mụ đàn bà cứ thế phang tôi bằng cái nĩa kẹp nồi, phang tôi tới tấp;"),
 ("а тут ещё барыня, да так и серчает;",
  "rồi lại còn một bà chủ nữa, cứ thế làm dữ;"),
 ("а тут, глядь, — чеботарь, да меня шилом-то, да меня шилом-то в зад;",
  "rồi kìa, một lão thợ giày cứ thế chọc dùi vào tôi, chọc dùi cả vào đít tôi;"),
 ("а тут ещё портной, да ножницами;",
  "rồi lại thêm một lão thợ may, thì cứ kéo mà xỉa;"),
 ("а тут ещё солдат со шпорами, да так на меня скинулся, что волосы у него дыбом стали;",
  "rồi lại còn một tên lính đeo đinh thúc ngựa, xông vào tôi hung tợn đến mức tóc nó dựng đứng cả lên;"),
 ("«вот я те!» — бает.",
  "«cho mày biết tay này!» — nó quát."),
 ("А там ещё, знать, ихний, на́большой: «ужо-ка я-то его!»",
  "Đằng kia hình như còn có cả tên cầm đầu của bọn chúng nữa: «để rồi ông cho mày một trận!»"),
 ("Братцы, — бает, — сробел».",
  "Anh em ơi, — hắn nói, — tôi đến vỡ mật mất.»"),
 ("«Ну, — бают разбойники, — делать нечего, уйдёмте, а то, пожалуй, и нас-то всех перевяжут!»",
  "«Thôi, — bọn cướp bảo nhau, — đành vậy, ta chuồn đi thôi, kẻo có khi cả lũ chúng ta cũng bị trói gô lại hết!»"),
 ("Ушли.",
  "Chúng bỏ đi."),

 ("А они живут пока да живут себе складно.",
  "Còn cả bọn thú vẫn sống với nhau êm thấm."),
 ("Вдруг приходят к ихней шалаше́ зверьё, да по духу и узнали, что́ там есть.",
  "Bỗng một bầy thú dữ kéo đến túp lều của chúng, đánh hơi liền biết có con gì ở trong."),
 ("«Ну-тка, — бают волку, — поди-ка ты наперёд!»",
  "«Nào, — chúng bảo con sói, — mày vào trước đi!»"),
 ("Только что тот взошёл, как те начали его катать; насилу ноги оттуда вынес.",
  "Sói vừa bước vào, cả bọn liền xúm vào nện cho nó một trận; nó chật vật lắm mới lết được chân ra khỏi đó."),
 ("Не знают, что и делать.",
  "Bầy thú chẳng biết phải làm sao."),
 ("А тута был с ними ёж; вот он: «Постойте-ка, — бает, — вот ужо-ка я попытаюсь, авось лучше будет!»",
  "Trong bọn có cả một con nhím; nó lên tiếng: «Khoan đã, — nó bảo, — để tôi thử xem, biết đâu lại hơn!»"),
 ("Вишь, он знал, что у барана-то одного бока нету.",
  "Số là nó biết tỏng con cừu thiếu mất một bên sườn."),
 ("Вот он и подкатился, да и кольни барана; как тот через всех да как прыгнет, да и драла.",
  "Thế là nó lăn tới, chích cho con cừu một cái; con cừu liền chồm qua đầu cả bọn rồi ba chân bốn cẳng bỏ chạy."),
 ("За ним и все, да так и разбежались.",
  "Cả lũ cũng chạy theo nó, thế là tan tác mỗi con một ngả."),
 ("А наместо их зверьё тута и осталось.",
  "Còn lũ thú dữ thì ở lại, chiếm luôn chỗ của chúng."),
]

note = ("Truyện loài vật kiểu «nhà trú đông của muông thú» (ATU 130, họ hàng gần với «Зимовье зверей» №64 và «Các nhạc công thành Bremen»): "
        "bầy gia súc chán cảnh nhà chủ liền bỏ vào rừng dựng lều, rồi hợp sức làm cả bọn cướp lẫn thú dữ khiếp vía bỏ chạy. "
        "Nét riêng của bản này là con cừu bị lột da một bên sườn — và trớ trêu thay, chính nhờ chỗ sườn trụi ấy mà con nhím tinh ranh mới chích đuổi được nó đi, để lũ thú dữ rốt cuộc chiếm lấy túp lều. "
        "Bản Afanasyev giữ nguyên lối kể dân dã, có cả câu nói tục bông đùa (để dấu lửng «обс..» theo đúng nguyên bản).")

vocab = [
 ("баять (бает)", "nói, bảo (động từ cổ/phương ngữ, = говорить)"),
 ("животина", "súc vật, gia súc (danh từ tập hợp, khẩu ngữ)"),
 ("овчина (овчинка)", "tấm da cừu đã thuộc (dùng để may áo lông)"),
 ("клин (клинья)", "miếng nối hình chêm, mảnh vải/da hình tam giác ghép thêm"),
 ("пособить", "giúp, chữa được việc (phương ngữ = помочь)"),
 ("лиходей", "kẻ ác, kẻ gây hại (từ cổ)"),
 ("шалаш (шалаша́)", "túp lều dựng bằng cành lá; bản này dùng dạng giống cái «шалаша́»"),
 ("гусак", "con ngỗng đực"),
 ("петун", "gà trống (phương ngữ = петух)"),
 ("ухват", "cái nĩa kẹp nồi (sào có chạc đôi để lấy nồi gang ra/vào lò)"),
 ("чеботарь", "thợ đóng & chữa giày (phương ngữ = сапожник)"),
 ("на́большой", "kẻ cầm đầu, thủ lĩnh, đại ca (phương ngữ)"),
 ("зверьё", "lũ thú dữ (danh từ tập hợp, sắc thái coi thường)"),
 ("дать драла (драла)", "ba chân bốn cẳng bỏ chạy, chạy biến (thành ngữ khẩu ngữ)"),
]

# ---- build unit JSON ----
blocks = [{"t": "note", "text": note}]
for ru, vi in paras:
    blocks.append({"t": "para", "text": f"{ru} ({vi})"})
blocks.append({"t": "subhead", "text": "Từ khó trong truyện"})
for ru, vi in vocab:
    blocks.append({"t": "vocab", "ru": ru, "vi": vi, "g": None})

unit = {
 "id": "skazki1-032",
 "num": 32,
 "title": "Сказка про одного однобокого барана — Truyện con cừu trụi một bên sườn",
 "vi": "Сказка про одного однобокого барана — Truyện con cừu trụi một bên sườn",
 "ru": "Сказка про одного однобокого барана",
 "icon": "🐏",
 "color": "#b45309",
 "sectionPrefix": "skazki1-032-s",
 "group": "Truyện № 61–100",
 "sections": [
   {
    "id": "skazki1-032-s001",
    "type": "story",
    "num": 63,
    "title": "№ 63 · Сказка про одного однобокого барана — Truyện con cừu trụi một bên sườn",
    "blocks": blocks,
   }
 ],
}

unit_path = os.path.join(BASE, "units", "skazki1-032.json")
with open(unit_path, "w", encoding="utf-8") as f:
    json.dump(unit, f, ensure_ascii=False, indent=1)
print("WROTE", unit_path, "paras:", len(paras), "vocab:", len(vocab))

# ---- patch book.json ----
bpath = os.path.join(BASE, "book.json")
book = json.load(open(bpath, encoding="utf-8"))
ids = [p["id"] for p in book["parts"]]
if "skazki1-032" in ids:
    print("part already exists, skipping add")
else:
    book["parts"].append({
        "id": "skazki1-032",
        "num": 32,
        "title": "Сказка про одного однобокого барана — Truyện con cừu trụi một bên sườn",
        "vi": "Сказка про одного однобокого барана — Truyện con cừu trụi một bên sườn",
        "ru": "Сказка про одного однобокого барана",
        "icon": "🐏",
        "color": "#b45309",
        "file": "units/skazki1-032.json",
        "sectionPrefix": "skazki1-032-s",
        "group": "Truyện № 61–100",
        "sectionCount": 1,
        "exerciseCount": 0,
        "grammarCount": 0,
    })
    with open(bpath, "w", encoding="utf-8") as f:
        json.dump(book, f, ensure_ascii=False, indent=1)
    print("PATCHED book.json -> parts:", len(book["parts"]))

# ---- append glossary ----
gpath = os.path.join(BASE, "glossary.json")
gl = json.load(open(gpath, encoding="utf-8"))
existing = set()
for e in gl["entries"]:
    existing.add(e["ru"].lower())
    existing.add(e.get("ruPlain", "").lower())

def plain(s):
    return s.replace("́", "").replace("̀", "")

added = 0
for ru, vi in vocab:
    rp = plain(ru)
    if ru.lower() in existing or rp.lower() in existing:
        print("  skip dup:", ru)
        continue
    gl["entries"].append({"ru": ru, "ruPlain": rp, "vi": vi, "g": None, "ref": "skazki1-032-s001"})
    existing.add(ru.lower()); existing.add(rp.lower())
    added += 1
gl["count"] = len(gl["entries"])
with open(gpath, "w", encoding="utf-8") as f:
    json.dump(gl, f, ensure_ascii=False, indent=1)
print("GLOSSARY added:", added, "new count:", gl["count"])
