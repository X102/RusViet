# -*- coding: utf-8 -*-
import json, os
BASE = os.path.dirname(os.path.abspath(__file__))

def plain(s):
    return s.replace('́','').replace('й','и').replace('Й','И')

def para(t): return {"t":"para","text":t}
def note(t): return {"t":"note","text":t}

# ---------------- Section s002 : № 41 ----------------
s002_paras = [
 "Жил старик и старуха. (Ngày xưa có một ông lão và một bà lão.)",
 "У старика, у старухи не было ни сына, ни дочери, был только один серый кот. (Ông lão bà lão chẳng có lấy một mụn con trai hay con gái nào, chỉ có độc một con mèo xám.)",
 "Он их поил-кормил, носил им кунок и белок, рябчиков, тетеревей и всяких зверьков. (Chính nó nuôi nấng ông bà, tha về cho ông bà nào chồn, nào sóc, gà gô, gà rừng cùng đủ thứ muông thú.)",
 "Сделался стар серый кот. (Rồi con mèo xám trở nên già nua.)",
 "Старуха и говорит старику: «Из чего мы, старик, кота держим? Только даром на печи место занял!» (Bà lão liền bảo ông lão: «Ông này, ta nuôi con mèo làm gì cơ chứ? Nó chỉ tổ chiếm chỗ trên bệ lò sưởi một cách vô tích sự!»)",
 "— «Да куда его девать-то?» (— «Thế chứ biết tống nó đi đâu bây giờ?»)",
 "— «Посади в котомку и отнеси в остров; пускай там свою жизнь решит». (— «Ông bỏ nó vào bị rồi đem ra cồn rừng; mặc cho nó tự định đoạt số phận ở đó».)",
 "Старик отнес. (Ông lão đem nó đi.)",
 "Кот остался в острову, день голодал, другой и третий и стал плакать. (Con mèo bị bỏ lại nơi cồn rừng, nhịn đói ngày thứ nhất, rồi ngày thứ hai, thứ ba, bèn ngồi khóc.)",
 "Идет лиса и спросила кота: «О чем ты плачешь, Котай Иванович?» (Một con cáo đi tới, hỏi mèo: «Anh khóc nỗi gì vậy, Kô-tai I-va-nô-vích?»)",
 "— «Ах, лиса, как мне не плакать? Жил я у старика и старухи, поил-кормил их, стал стар, они и прогнали меня». (— «Ôi cáo ơi, ta khóc sao được kia chứ? Ta vốn ở với một ông lão bà lão, hầu hạ nuôi nấng họ, nay già rồi thì họ đuổi ta đi».)",
 "А лиса говорит: «Давай, Котай Иванович, женимся!» (Cáo bèn nói: «Này Kô-tai I-va-nô-vích, hay là ta lấy nhau đi!»)",
 "— «Куды мне жениться! Только бы свою голову пропитать; а у тебя, чай, детки есть, кормить-поить надо». (— «Ta mà cưới xin nỗi gì! Nuôi nổi cái thân ta đã là may; còn cô, hẳn là có cả đàn con, lại phải nuôi ăn nuôi uống nữa».)",
 "— «Ничего, как-нибудь прокормимся». (— «Không sao, rồi cũng xoay xở mà nuôi nhau được thôi».)",
 "Вот и вышла лиса за Котая Иваныча. (Thế là cáo lấy Kô-tai I-va-nứt làm chồng.)",
 "Однажды медведь и заяц шли мимо лисицыной норы. (Một hôm gấu và thỏ đi ngang qua hang cáo.)",
 "Увидала их лиса и закричала: «Ах ты, толстопятый медведь, и ты, косой заяц! (Cáo trông thấy chúng liền quát lên: «Ơ này, lão gấu gót bè kia, cả mày nữa, thỏ mắt lác!)",
 "Как была я вдовой, бывало, ни один из вас не проходил мимо моей норы, а как вышла замуж, то каждый день шляетесь; ишь какие дороги проторили! (Hồi ta còn góa bụa thì chẳng đứa nào trong các ngươi bén mảng qua hang ta, thế mà từ khi ta lấy chồng thì ngày nào cũng vác mặt lượn lờ; coi kìa, các ngươi giẫm thành cả lối mòn rồi đấy!)",
 "Смотрите, как бы вас Котай Иванович по шее не проводил!» (Liệu hồn, kẻo Kô-tai I-va-nô-vích lại tóm cổ tống các ngươi đi cho!»)",
 "Вот, идучи дорогой, медведь и сказал зайцу: «Чего, брат, у нее за муж такой — Котай Иванович? Ужли больше меня?» (Dọc đường đi, gấu bảo thỏ: «Này chú, chồng mụ ta là cái ngữ gì vậy — Kô-tai I-va-nô-vích ấy? Chẳng lẽ lại to lớn hơn cả ta sao?»)",
 "А заяц: «Ужли прытче меня? Пойдем-ка завтра, посмотрим на него». (Thỏ đáp: «Chẳng lẽ lại nhanh nhẹn hơn cả em? Mai ta thử tới xem mặt ngài ấy xem sao».)",
 "Пришли на другой день к лисицыной норе и видят: кот гложет целый стяг быка, а сам мурлычет: «Мало, мало!» (Hôm sau chúng tới hang cáo thì thấy: mèo đang gặm cả một tảng thịt bò, miệng kêu gừ gừ: «Ít quá, ít quá!»)",
 "— «Ну, брат, — сказал медведь зайцу, — беда наша; Котай все говорит: мало, мало! (— «Hỏng rồi chú ơi, — gấu bảo thỏ, — bọn ta nguy to; Kô-tai cứ luôn mồm: ít quá, ít quá!)",
 "Спрячемся, ты ляжь под хворост, а я взлезу на дерево». (Ta nấp đi thôi, chú nằm nép dưới đống củi khô, còn anh thì trèo lên cây».)",
 "Только уселись они по своим местам, как выбежала из-под хвороста мышь. (Vừa yên vị mỗi đứa một chỗ thì có con chuột từ dưới đống củi phóng ra.)",
 "Кот увидал ее и в ту же минуту бросился за ней к хворосту. (Mèo trông thấy nó, lập tức chồm theo về phía đống củi.)",
 "Заяц испугался, кинулся бежать; а медведь услышал тревогу, хотел повернуться, да со страстей упал с дерева и убился до смерти. (Thỏ hoảng hồn, vắt chân lên cổ bỏ chạy; còn gấu nghe động thì muốn xoay mình, nhưng vì khiếp đảm mà ngã lăn từ trên cây xuống, chết tươi.)",
 "Лиса с котом и доныне поживают да медведя поедают. (Cáo cùng mèo đến nay vẫn sống bên nhau, lại có cả thịt gấu mà chén dần.)",
]

s002_vocab = [
 ("куница (кунок)", "chồn (chồn nâu); «кунок» là dạng phương ngữ của «куниц» (số nhiều cách 2)"),
 ("рябчик", "gà gô rừng — loài chim nhỏ họ trĩ, thịt ngon"),
 ("остров (в остров)", "nghĩa cổ: cồn/khoảnh rừng đứng lẻ giữa đồng, không phải «đảo» trên nước"),
 ("котомка", "cái bị, tay nải đeo vai"),
 ("толстопятый", "«gót bè, gót dày» — biệt danh trêu con gấu"),
 ("шляться", "lượn lờ, lê la, vác mặt đi rông"),
 ("проторить (дороги проторили)", "đi mãi thành lối mòn, giẫm mở thành đường"),
 ("по шее проводить", "tóm cổ tống ra ngoài, đuổi thẳng cổ (thành ngữ)"),
 ("прыткий (прытче)", "nhanh nhẹn, lẹ làng; «прытче» = nhanh hơn"),
 ("стяг (стяг быка)", "tảng thịt lớn, nửa con bò xẻ dọc (từ cổ)"),
 ("глодать (гложет)", "gặm, nhằn (xương, thịt)"),
 ("хворост", "củi khô, cành khô rụng nhặt trong rừng"),
 ("со страстей", "vì khiếp đảm, vì sợ hãi quá (страсти = nỗi kinh hoàng, từ cổ)"),
 ("доныне", "cho đến nay, đến tận bây giờ (từ cổ)"),
]

# ---------------- Section s003 : № 42 ----------------
s003_paras = [
 "В некотором царстве, в некотором государстве жил в дремучих лесах могучий кот. (Ở một vương quốc nọ, trong một xứ sở kia, giữa rừng già rậm rạp có một con mèo dũng mãnh.)",
 "Медведь, волк, олень, лиса и заяц собрались совет держать, как бы могучего, сильного кота к себе на пир позвать. (Gấu, sói, hươu, cáo và thỏ họp nhau bàn bạc, xem làm cách nào mời được con mèo hùng mạnh, dũng mãnh ấy tới dự tiệc với mình.)",
 "Наготовили всякого добра и стали думать: кому идти за котом. (Chúng sửa soạn đủ thứ ngon lành rồi ngồi tính: ai sẽ đi mời mèo đây.)",
 "«Ну, ступай ты, медведь!» («Nào, bác gấu, bác đi đi!»)",
 "Медведь начал отговариваться: «Я мохнат и косолап, куда мне! Пускай волк пойдет». (Gấu liền thoái thác: «Tôi thì lông lá xù xì, chân lại vòng kiềng, đi sao được! Để sói đi thì hơn».)",
 "А волк говорит: «Я неповоротлив, он меня не послушает; лучше пусть олень идет!» (Sói bảo: «Tôi vụng về chậm chạp, nó chẳng thèm nghe tôi đâu; tốt hơn là để hươu đi!»)",
 "Олень тоже отказывается: «Я пуглив-боязлив, не сумею ответ держать; кот, пожалуй, за то меня смерти предаст. (Hươu cũng chối: «Tôi vốn nhút nhát rụt rè, chẳng biết ăn nói thưa gửi ra sao; lỡ ra mèo lại vì thế mà đem giết tôi mất.)",
 "Иди ты, шустрая, — говорит лисе, — ты и собой хороша и оборотлива». (Chị đi đi, chị lanh lợi, — hươu bảo cáo, — chị vừa xinh đẹp lại vừa khôn khéo».)",
 "— «У меня хвост длинен, не смогу скоро бежать; пускай идет заяц!» — отвечает лиса. (— «Đuôi tôi dài, chẳng chạy nhanh được; thôi để thỏ đi!» — cáo đáp.)",
 "Тут все стали складывать на зайца: «Ступай, косой! Не бойся. (Thế là cả bọn xúm vào dồn việc cho thỏ: «Đi đi, chú thỏ lác! Đừng sợ.)",
 "Ты поворотлив и на ногу скор; коли он на тебя вскинется, ты сейчас от него уйдешь». (Mày nhanh nhảu, chân lại lẹ; nó mà chồm tới thì mày tót đi ngay được».)",
 "Заяц — делать нечего — побежал к коту; прибежал, поклонился пониже ног котовых и стал звать его на пир, на беседу. (Thỏ — chẳng còn cách nào khác — đành chạy đến chỗ mèo; tới nơi, nó cúi rạp mình dưới chân mèo mà mời mèo đến dự tiệc, dự cuộc vui.)",
 "Исправил все по наказу и пустился назад бежать, сколько сил хватает. (Làm trọn mọi điều y như lời dặn xong, thỏ ba chân bốn cẳng chạy về, dồn hết bao nhiêu sức vào chân.)",
 "Явился к своим товарищам и говорит: «Ну, набрался страху! (Về tới chỗ bè bạn, nó kể: «Chao ôi, một phen hú vía!)",
 "Сам-то кот бурый, шерсть на нем стоит дыбом, а хвост так по земле и волочится!» (Con mèo ấy lông nâu sậm, lông dựng đứng cả lên, còn cái đuôi thì cứ lê quét cả mặt đất!»)",
 "Тут звери стали прятаться кто куда: медведь взобрался на дерево, волк залез в кусты, лиса зарылась в землю, а олень с зайцем совсем ушли... (Thế là lũ thú mỗi con nấp một nơi: gấu trèo tót lên cây, sói chui vào bụi rậm, cáo vùi mình xuống đất, còn hươu với thỏ thì chạy đi biệt tăm...)",
]

s003_endnote = "Ghi chú của Afanasyev: «Окончание — то же, что и в предшествующей сказке» (Đoạn kết — giống hệt như ở truyện trước), tức như dị bản №41: mèo bé nhỏ mà ăn ngấu nghiến, chê «ít quá» khiến cả đám muông thú nấp rình phải khiếp vía bỏ chạy."

s003_vocab = [
 ("дремучий (дремучих лесах)", "(rừng) rậm rạp, âm u, hoang vu"),
 ("могучий", "hùng mạnh, dũng mãnh, đầy sức mạnh"),
 ("совет держать", "họp bàn, bàn bạc, hội ý (lối nói cổ)"),
 ("наготовить", "chuẩn bị/làm sẵn thật nhiều thứ"),
 ("отговариваться", "thoái thác, kiếm cớ chối từ"),
 ("мохнатый (мохнат)", "lông lá xù xì, rậm lông"),
 ("косолапый (косолап)", "chân vòng kiềng, đi chữ bát (biệt danh con gấu)"),
 ("неповоротливый (неповоротлив)", "vụng về, chậm chạp, ì ạch"),
 ("пуглив-боязлив", "nhút nhát rụt rè, hay sợ hãi (cặp từ láy nghĩa)"),
 ("ответ держать", "ăn nói thưa gửi, đối đáp, chịu trách nhiệm trả lời (lối cổ)"),
 ("предать смерти (смерти предаст)", "đem giết, xử tử (lối trang trọng)"),
 ("шустрый (шустрая)", "lanh lợi, nhanh nhảu, tháo vát"),
 ("оборотливый (оборотлива)", "khôn khéo, biết xoay xở, tháo vát"),
 ("наказ (по наказу)", "lời dặn dò, lời sai bảo (từ cổ)"),
 ("волочиться", "lê lết, kéo lê (trên mặt đất)"),
]

def build_section(sid, num, title, opennote, paras, vocab, endnote=None):
    blocks = [note(opennote)]
    blocks += [para(p) for p in paras]
    if endnote:
        blocks.append(note(endnote))
    blocks.append({"t":"subhead","text":"Từ khó trong truyện"})
    for ru, vi in vocab:
        blocks.append({"t":"vocab","ru":ru,"vi":vi,"g":None})
    return {"id":sid,"type":"story","num":num,"title":title,"blocks":blocks}

note41 = ("Dị bản dân gian của «Mèo và cáo» (ATU 103), kể gọn hơn bản №40. Ở đây con mèo "
 "tên Kô-tai I-va-nô-vích vốn sống với hai ông bà lão, săn chồn sóc gà rừng nuôi họ; về già "
 "bị bỏ ra cồn rừng, gặp cáo rồi nên duyên. Cáo lại mượn oai chồng để nạt gấu và thỏ; cả hai "
 "rình xem, mèo vồ chuột trong đống củi khiến thỏ bỏ chạy còn gấu khiếp vía ngã cây mà chết. "
 "(Tên nhân vật: mèo = Kô-tai I-va-nô-vích / Kô-tai I-va-nứt.)")

note42 = ("Dị bản thứ hai, mở đầu bằng công thức cổ tích «Ở một vương quốc nọ…». Một con mèo "
 "«dũng mãnh» sống giữa rừng già; muông thú họp bàn cử người đi mời mèo dự tiệc, con nào cũng "
 "thoái thác đùn đẩy cho đến khi dồn cả vào thỏ. Thỏ về tả con mèo dữ tợn khiến cả bọn nháo nhác "
 "đi trốn; Afanasyev ghi đoạn kết giống hệt dị bản №41.")

s002 = build_section("skazki1-021-s002", 41, "№ 41 · Кот и лиса — Mèo và cáo",
                      note41, s002_paras, s002_vocab)
s003 = build_section("skazki1-021-s003", 42, "№ 42 · Кот и лиса — Mèo và cáo",
                      note42, s003_paras, s003_vocab, endnote=s003_endnote)

# ---- update unit file ----
unit_path = os.path.join(BASE,"units","skazki1-021.json")
unit = json.load(open(unit_path,encoding="utf-8"))
have = {s["id"] for s in unit["sections"]}
for sec in (s002,s003):
    if sec["id"] in have:
        unit["sections"] = [x for x in unit["sections"] if x["id"]!=sec["id"]]
    unit["sections"].append(sec)
json.dump(unit, open(unit_path,"w",encoding="utf-8"), ensure_ascii=False, indent=1)
print("unit sections:", [s["id"] for s in unit["sections"]])

# ---- update glossary ----
gpath = os.path.join(BASE,"glossary.json")
g = json.load(open(gpath,encoding="utf-8"))
existing = {(e["ruPlain"].lower(), e["ref"]) for e in g["entries"]}
existing_words = {e["ruPlain"].lower() for e in g["entries"]}
added = 0
def add_vocab(vocab, ref):
    global added
    for ru, vi in vocab:
        head = ru.split(" (")[0].strip()
        if plain(head).lower() in existing_words:
            print("  skip (exists):", head)
            continue
        g["entries"].append({"ru":ru,"ruPlain":plain(ru),"vi":vi,"g":None,"ref":ref})
        existing_words.add(plain(head).lower())
        added += 1
add_vocab(s002_vocab, "skazki1-021-s002")
add_vocab(s003_vocab, "skazki1-021-s003")
g["count"] = len(g["entries"])
json.dump(g, open(gpath,"w",encoding="utf-8"), ensure_ascii=False, indent=1)
print("glossary count:", g["count"], "added:", added)

# ---- update book.json sectionCount ----
bpath = os.path.join(BASE,"book.json")
b = json.load(open(bpath,encoding="utf-8"))
for p in b["parts"]:
    if p["id"]=="skazki1-021":
        p["sectionCount"]=len(unit["sections"])
        print("book sectionCount skazki1-021 ->", p["sectionCount"])
json.dump(b, open(bpath,"w",encoding="utf-8"), ensure_ascii=False, indent=1)
print("DONE")
