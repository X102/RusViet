# -*- coding: utf-8 -*-
"""Append sections s003 (№79) + s004 (№80) to unit skazki1-044, add glossary, bump book.json."""
import json, os, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
UNIT = os.path.join(HERE, "units", "skazki1-044.json")
GLOSS = os.path.join(HERE, "glossary.json")
BOOK = os.path.join(HERE, "book.json")

def P(ru, vi):
    return {"t": "para", "text": "%s (%s)" % (ru, vi)}

# ---------------- s003 = № 79 (bản thơ dân gian / raёшный стих) ----------------
s003_note = (
    "Dị bản thứ ba — bản THƠ DÂN GIAN (raёшный стих) của cùng truyện, mở đầu bằng "
    "dòng đề ngày tháng giễu nhại công văn («Năm 1729, tháng Chín, ngày 16»). Cá Gai vẫn "
    "bịa chuyện «hồ Rostov từng cháy» để chiếm hồ, gọi Cá Rói–Cá Rô–Cá Chó làm chứng gian; "
    "quan toà lần này là Cá Bơn xứ Beloozero (Белозер-Палтос-рыба). Phần cuối là chuỗi tên "
    "người gieo vần kể cảnh làm thịt Cá Gai (Nikon/прикол, Persha/вершу, Bogdan/бог дал…), "
    "đặc sản của lối kể vần điệu Nga."
)
s003_paras = [
    ("1729 года, месяца сентября 16 числа зародился ершишко-плутишко, худая головишко, шиловатый хвост, слюноватый нос, киловатая брюшина, лихая образина, на роже кожа — как елова кора.",
     "Năm 1729, tháng Chín, ngày mười sáu, sinh ra chú Cá Gai ranh ma: cái đầu nhỏ tồi tàn, cái đuôi nhọn hoắt như dùi, cái mũi nhớt nhãi, cái bụng phình thoát vị, cái mặt mày dữ tợn, da trên mặt thì sần như vỏ cây thông."),
    ("Прижилось, прискудалось ершишку-плутишку в своем славном Кубинском озере, собрался на ветхих дровнишках с женою и детишкам, поехал в Белозерское озеро, с Белозерского в Корбозерское, с Корбозерского в Ростовское:",
     "Sống lay lắt, túng bấn nơi cái hồ Kubinskoe danh tiếng của mình, chú Cá Gai ranh ma chất mình lên chiếc xe trượt cũ nát cùng vợ con, đi tới hồ Beloozero, từ Beloozero sang hồ Korbozero, từ Korbozero sang hồ Rostov:"),
    ("«Здравствуйте, лещи, ростовские жильцы! Пустите ерша пообедать и коня покормить».",
     "«Chào các bác Cá Vền, dân cư hồ Rostov! Cho Cá Gai này vào ăn bữa cơm, cho ngựa ăn chút cỏ»."),
    ("Лещи распространились, ерша к ночи пустили.",
     "Đám Cá Vền nới lòng, cho Cá Gai vào trú đêm."),
    ("Ерш где ночь ночевал, тут и год годовал; где две ночевал, тут два года годовал; сыновей поженил, а дочерей замуж повыдал, изогнал лещов, ростовских жильцов, во мхи и болота, пропасти земные.",
     "Cá Gai trú đêm ở đâu là ở lì cả năm nơi đó; trú hai đêm ở đâu là ở lì hai năm nơi đó; nó cưới vợ cho các con trai, gả chồng cho các con gái, rồi đuổi sạch đám Cá Vền — dân cư hồ Rostov — vào rêu rong đầm lầy, vào những vực sâu lòng đất."),
    ("Три года лещи хлеба-соли не едали, три года лещи хорошей воды не пивали, три года лещи белого свету не видали; с того лещи с голоду помирали.",
     "Suốt ba năm ròng đám Cá Vền chẳng được miếng bánh hạt muối, suốt ba năm ròng chẳng được ngụm nước lành, suốt ba năm ròng chẳng thấy ánh sáng mặt trời; vì thế đám Cá Vền chết dần vì đói."),
    ("Сбиралися лещи в земскую избу, и думали думу заедино, и написали просьбу, и подавали Белозер-Палтос-рыбе:",
     "Đám Cá Vền tụ tập ở nhà việc làng, cùng nhau bàn bạc một bề, viết một lá đơn rồi dâng lên Cá Bơn xứ Beloozero (Белозер-Палтос-рыба):"),
    ("«Матушка Белозер-Палтос-рыба! Почему ершишко-плутишко, худая головишко, разжился, распоселился в нашем Ростовском озере и изогнал нас, лещов, ростовских жильцов, во мхи и болота и пропасти земные?",
     "«Thưa mẹ Cá Bơn xứ Beloozero! Cớ sao chú Cá Gai ranh ma, cái đầu nhỏ tồi tàn, lại phất lên, chiếm cứ trong hồ Rostov của chúng con mà xua đuổi chúng con — đám Cá Vền, dân cư hồ Rostov — vào rêu rong đầm lầy cùng những vực sâu lòng đất?"),
    ("Три года мы, лещи, хлеба-соли не едали, три года лещи хорошей воды не пивали, три года лещи свету белого не видали; с того мы, лещи, и с голоду помирали. Есть ли у него на это дело книги, отписи и паспорты какие?»",
     "Suốt ba năm chúng con, đám Cá Vền, chẳng được miếng bánh hạt muối, suốt ba năm chẳng được ngụm nước lành, suốt ba năm chẳng thấy ánh sáng mặt trời; vì thế chúng con chết dần vì đói. Liệu nó có giấy tờ gì cho việc này không — sổ sách, biên lai cùng giấy thông hành nào chăng?»"),
    ("И думали думу заедино щука ярославска, другая переславска, рыба-сом с большим усом: кого послать ерша позвать?",
     "Cùng nhau bàn bạc một bề có Cá Chó xứ Yaroslavl, một con Cá Chó nữa xứ Pereslavl, cùng ông Cá Nheo râu dài: biết cử ai đi gọi Cá Gai đến đây?"),
    ("Менька послать — у него губы толстые, а зубы редкие, речь не умильна, говорить с ершом не сумеет!",
     "Cử Cá Méng đi ư — nó thì môi dày, răng thưa, lời ăn tiếng nói chẳng ngọt, đối đáp với Cá Gai sao nổi!"),
    ("Придумала рыба-сом с большим усом: послать или нет за ершом гарьюса; у гарьюса губки тоненьки, платьице беленько, речь московска, походка господска.",
     "Ông Cá Nheo râu dài nghĩ ra: hay là cử Cá Hồi-Trắng (гарьюс) đi đòi Cá Gai; Cá Hồi-Trắng môi mỏng dính, áo xống trắng tinh, ăn nói giọng Mátxcơva, dáng đi quý phái."),
    ("Дали ему окуня рассыльным, карася пятисотским, семь молей, поняты́х людей. Взяли ерша, сковали, связали и на суд представили.",
     "Người ta cấp cho nó Cá Rô làm lính trạm, Cá Diếc làm ngũ-bách-trưởng, bảy con cá mại làm người chứng. Chúng bắt lấy Cá Gai, xích lại, trói lại rồi điệu ra trước toà."),
    ("Ерш пред судом стоит и с повадкой говорит: «Матушка Белозер-Палтос-рыба! Почему меня на суд повещали?»",
     "Cá Gai đứng trước toà mà ăn nói rất ngông nghênh: «Thưa mẹ Cá Bơn xứ Beloozero! Cớ sao lại gọi con ra hầu toà?»"),
    ("«Ах ты, ершишко-плутишко, худая головишко! Почему ты разжился и расселился в здешнем Ростовском озере, изогнал лещов, ростовских жильцов, во мхи и болота и пропасти земные? Три года лещи хлеба-соли не едали, три года лещи хорошей воды не пивали, три года лещи свету белого не видали, и с того лещи с голоду помирают. Есть ли у тебя на это дело книги, отписи и паспорты какие!»",
     "«À cái thằng Cá Gai ranh ma, cái đầu nhỏ tồi tàn kia! Cớ sao mày phất lên rồi chiếm cứ cái hồ Rostov nơi đây, xua đuổi đám Cá Vền — dân cư hồ Rostov — vào rêu rong đầm lầy cùng những vực sâu lòng đất? Suốt ba năm đám Cá Vền chẳng được miếng bánh hạt muối, suốt ba năm chẳng được ngụm nước lành, suốt ba năm chẳng thấy ánh sáng mặt trời, vì thế chúng chết dần vì đói. Mày có giấy tờ gì cho việc này không — sổ sách, biên lai cùng giấy thông hành nào chăng!»"),
    ("«Матушка Белозер-Палтос-рыба! В память или нет тебе пришло: когда горело наше славное Кубинское озеро, там была у ершишка избишка, в избишке были сенишки, в сенишках клетишко, в клетишке ларцишко, у ларцишка замчишко, у замчишка ключишко, — там-то были книги и отписи и паспорты, и все пригорело!",
     "«Thưa mẹ Cá Bơn xứ Beloozero! Mẹ có còn nhớ hay chăng: cái thuở cháy bùng cái hồ Kubinskoe danh tiếng của chúng con, Cá Gai con có một mái lều nhỏ, trong lều có gian chái nhỏ, trong chái có buồng kho nhỏ, trong kho có cái rương nhỏ, trên rương có ổ khoá nhỏ, nơi ổ khoá có chiếc chìa nhỏ — chính nơi ấy cất giữ sổ sách, biên lai cùng giấy thông hành, mà tất tật đã cháy thành tro!"),
    ("Да не то одно пригорело; был у батюшки дворец на семи верстах, на семи столбах, под полатями бобры, на полатях ковры — и то все пригорело!»",
     "Mà nào chỉ có thế cháy thôi đâu; cha con từng có một toà cung điện dài bảy dặm, dựng trên bảy cây cột, dưới sàn gác là lũ hải ly, trên sàn gác là thảm hoa — mà tất tật cũng cháy ráo trọi!»"),
    ("А рыба-семга позади стояла и на ерша злым голосом кричала: «Ах ты, ершишко-плутишко, худая головишко! Тридцать ты лет под порогом стоял, и сорок человек разбою держал, и много голов погубил, и много живота притопил!»",
     "Cá Hồi đứng phía sau cất cái giọng dữ dằn quát Cá Gai: «À cái thằng Cá Gai ranh ma, cái đầu nhỏ tồi tàn kia! Suốt ba mươi năm trời mày rình nấp dưới bậc cửa, cầm đầu bốn mươi tên chuyên nghề cướp bóc, hại biết bao mạng người, nhấn chìm biết bao của cải!»"),
    ("И ершу стало азартно; как с рыбою-семгою не отговориться? «Ах ты, рыба-семга, бока твои сальны! И ты, рыба-сельдь, бока твои кислы! Вас едят господа и бояра, меня мелкая чета крестьяна — бабы щей наварят и блинов напекут, щи хлебают, похваливают: рыба костлива, да уха хороша!»",
     "Cá Gai đâm nổi máu hăng; chẳng lẽ lại không cãi tay đôi với Cá Hồi? «Ê này Cá Hồi, sườn mày béo nhẫy mỡ! Còn mày nữa, Cá Trích, sườn mày chua loét! Chúng bay thì để cho các quan các ngài xơi, còn ta thì cho đám dân cày nghèo hèn — các bà nấu nồi canh chua, rán mẻ bánh blin, húp canh xì xụp mà khen lấy khen để: cá tuy lắm xương, nhưng canh thì tuyệt!»"),
    ("Тут ерш с семгой отговорился.",
     "Thế là Cá Gai cãi thắng được Cá Hồi."),
    ("Говорит Белозер-Палтос-рыба: «Окунь-рассыльный, карась-пятисотский, семь молей, поняты́х людей! Возьмите ерша».",
     "Cá Bơn xứ Beloozero phán: «Cá Rô lính trạm, Cá Diếc ngũ-bách-trưởng, bảy con cá mại làm chứng! Bắt lấy Cá Gai cho ta»."),
    ("А ерш никаких рыб не боится, ото всех рыб боронится. Собрался он, ершишко-плутишко, на свои на ветхие дровнишки с женою и детишкам и поезжает в свое славное в Кубинское озеро.",
     "Nhưng Cá Gai chẳng sợ con cá nào, nó chống đỡ được hết thảy mọi loài cá. Nó — chú Cá Gai ranh ma — lại chất mình lên chiếc xe trượt cũ nát của mình cùng vợ con mà về cái hồ Kubinskoe danh tiếng của mình."),
    ("Рыба-семга хоть на ерша злым голосом кричала, только за ершом вслед подавалась: «Ах ты, ершишко-плутишко, худая головишко! Возьми ты меня в свое славное в Кубинское озеро — Кубинского озера поглядеть и Кубинских ста́нов посмотреть».",
     "Cá Hồi tuy đã cất giọng dữ dằn quát mắng Cá Gai, vậy mà giờ lại lẽo đẽo bơi theo sau: «Ê này chú Cá Gai ranh ma, cái đầu nhỏ tồi tàn ơi! Cho ta theo về cái hồ Kubinskoe danh tiếng của ngươi với — để ngắm cái hồ Kubinskoe và xem các bến bãi xứ Kubinskoe»."),
    ("Ерш зла и лиха не помнит, рыбу-семгу за собой поводит. Рыба-семга идучи устала, в Кубинском устье вздремала и мужику в сеть попала.",
     "Cá Gai chẳng để bụng điều ác điều dữ, dẫn Cá Hồi đi theo sau mình. Cá Hồi đi đường mỏi mệt, chợp mắt nghỉ nơi cửa lạch Kubinskoe, thế rồi sa vào lưới một bác mu-gích."),
    ("Ерш назад оглянулся, а сам усмехнулся: «Слава тебе господи! Вчера рыба-семга на ерша злым голосом кричала, а сегодня мужику в сеть попала».",
     "Cá Gai ngoái lại nhìn, rồi tủm tỉm cười thầm: «Lạy Chúa tôi! Hôm qua Cá Hồi còn cất giọng dữ dằn quát Cá Gai, mà hôm nay đã sa vào lưới bác mu-gích»."),
    ("Ерш семге подивовал и сам на утренней зоре вздремал, мужику в морду попал.",
     "Cá Gai chê cười Cá Hồi, thế rồi chính nó lúc rạng đông cũng chợp mắt, liền sa vào cái đó của bác mu-gích."),
    ("Пришел Никон, заколил прикол; пришел Перша, поставил вершу; пришел Богдан, и ерша бог дал; пришел Вавила, поднял ерша на вила; пришел Пимен, ерша запи́нил; пришел Обросим, ерша оземь бросил; пришел Антон, завертел ерша в балахон; пришел Амос, ерша в клеть понес.",
     "Bác Nikon tới, đóng xuống một chiếc cọc đăng; bác Persha tới, đặt xuống một cái lờ; bác Bogdan tới, thế là trời cho được Cá Gai (Bog-dan nghĩa là «trời cho»); bác Vavila tới, xốc Cá Gai lên chiếc chĩa; bác Pimen tới, lấy chân đá hất Cá Gai; bác Obrosim tới, quật Cá Gai xuống đất; bác Anton tới, cuộn Cá Gai vào tấm áo choàng; bác Amos tới, khiêng Cá Gai vào nhà kho."),
    ("Идет Спира, около ерша стырит; Амос Спиру да по рылу. «Ах ты, Спира! Над этакой рыбой стыришь; у тебя этака рыба век в дому не бывала!»",
     "Bác Spira đi tới, cứ lượn lờ định cuỗm Cá Gai; Amos liền cho Spira một cú vào mõm. «À cái thằng Spira! Cái thứ cá thế này mà mày cũng định cuỗm; thứ cá thế này cả đời chưa từng có trong nhà mày!»"),
    ("Пришел Вася, ерша с клети слясил; пришел Петруша, ерша разрушил; пришел Савва, вынял с ерша полтора пуда сала; пришел Иуда, расклал ерша на четыре блюда; пришла Марина, ерша помыла; пришла Акулина, ерша подварила.",
     "Bác Vasya tới, lôi tuột Cá Gai khỏi nhà kho; bác Petrusha tới, mổ phanh Cá Gai; bác Savva tới, moi từ Cá Gai ra một pud rưỡi mỡ; bác Iuda tới, bày Cá Gai ra thành bốn đĩa; bà Marina tới, rửa sạch Cá Gai; bà Akulina tới, nấu Cá Gai lên."),
    ("Пришел Антипа, ерша сти́пал; пришел Алупа, ерша слу́пал; пришел Елизар, блюда облизал; пришел Влас, попучил глаз; пришла Ненила и блюда обмыла!",
     "Bác Antipa tới, vồ lấy Cá Gai; bác Alupa tới, xơi sạch Cá Gai; bác Elizar tới, liếm sạch các đĩa; bác Vlas tới, trố mắt ra nhìn; bà Nenila tới, rửa sạch các đĩa thôi!"),
]
s003_vocab = [
    ("лещ", "cá vền (bream, Abramis brama); nguyên cáo chính trong truyện"),
    ("семга", "(сёмга) cá hồi (Atlantic salmon, Salmo salar)"),
    ("палтус", "cá bơn (halibut); Белозер-Палтос-рыба = «Cá Bơn xứ Beloozero», đóng vai quan toà"),
    ("гарьюс", "(= хариус) cá hồi trắng / cá lăng trắng (grayling, Thymallus); ở đây làm sứ giả «giọng Mátxcơva»"),
    ("мень", "(менёк) cá Méng (= налим, burbot), môi dày răng thưa"),
    ("живот", "(cổ) của cải, tài sản (cũng nghĩa «bụng / mạng sống»)"),
    ("полати", "sàn gác ngủ (bệ gỗ rộng kê cao trong nhà gỗ Nga)"),
    ("бобр", "con hải ly (beaver)"),
    ("прикол", "cọc đóng xuống nước để chắn/buộc (đăng cá)"),
    ("балахон", "áo choàng rộng thùng thình"),
    ("пуд", "pud, đơn vị trọng lượng Nga cổ (~16,38 kg)"),
    ("морда", "(ở đây) cái đó/lờ đơm cá đan bằng nan (không phải nghĩa «mõm»)"),
    ("отпись", "(cổ) biên lai, giấy biên nhận / hồi báo (отписи)"),
    ("стан", "bãi/trại, nơi dừng chân (Кубинских ста́нов = các bến bãi xứ Kubinskoe)"),
]

# ---------------- s004 = № 80 (bản văn xuôi «Список с судного дела») ----------------
s004_note = (
    "Dị bản thứ tư — bản VĂN XUÔI nổi tiếng «Hồ sơ vụ án» (Список с судного дела), nhại y "
    "khuôn lối công văn xử kiện chốn nha môn Nga thế kỷ XVII–XVIII bằng thứ tiếng nha lại cổ. "
    "Cá Vền (истец/nguyên cáo) kiện Cá Gai chiếm hồ Rostov; quan toà là đức Cá Tầm, Cá Tầm-Trắng "
    "(белуга) và Cá Bạch-Ngư. Cá Gai khôn lỏi chối tội, vu cho mọi nhân chứng đều là «họ hàng nhà "
    "giàu»; rốt cuộc vẫn bị xử thua, bị kết án đánh roi rồi treo phơi nắng — nhưng nó nhổ vào mặt "
    "quan toà rồi phóng vào bụi rậm trốn mất. Đây là một trong những áng văn trào phúng dân gian "
    "sớm nhất của văn học Nga."
)
s004_paras = [
    ("Список с судного дела слово в слово, как был суд у Леща с Ершом:",
     "Bản sao hồ sơ vụ án, chép lại từng chữ một, ghi cảnh Cá Vền kiện nhau với Cá Gai trước toà:"),
    ("«Рыбам господам: великому Осетру и Белуге, Белой-рыбице, бьет челом Ростовского озера сынчишко боярской Лещ с товарищи.",
     "«Kính dâng các ngài cá: đức Cá Tầm vĩ đại cùng Cá Tầm-Trắng (Белуга) và Cá Bạch-Ngư, nay có Cá Vền — đứa con nhà quý tộc quèn của hồ Rostov — cùng các bạn hữu xin dập đầu kêu thỉnh."),
    ("Жалоба, господа, нам на злого человека на Ерша Щетинника и на ябедника.",
     "Thưa các ngài, chúng con có đơn kiện kẻ ác là Cá Gai họ Lông-Cứng, quân chuyên vu vạ mách lẻo."),
    ("В прошлых, господа, годах было Ростовское озеро за нами; а тот Ерш, злой человек, Щетинников наследник, лишил нас Ростовского озера, наших старых жиров; расплодился тот Ерш по рекам и по озерам; он собою мал, а щетины у него аки лютые рогатины, и он свидится с нами на стану — и теми острыми своими щетинами подкалывает наши бока и прокалывает нам ребра, и суется по рекам и по озерам, аки бешеная собака, путь свой потеряв.",
     "Thưa các ngài, những năm trước hồ Rostov vốn thuộc về chúng con; thế mà tên Cá Gai, kẻ ác kia, dòng dõi nhà Lông-Cứng, đã cướp mất hồ Rostov của chúng con, cướp mất những bãi kiếm ăn xưa cũ; tên Cá Gai ấy sinh sôi nảy nở khắp các sông các hồ; thân nó tuy bé, mà gai trên mình nó cứ như những ngọn giáo hung tợn, hễ giáp mặt chúng con ở bãi nghỉ là lại lấy gai nhọn chọc vào sườn, đâm thủng cả xương sườn chúng con, rồi cứ xông xáo khắp sông khắp hồ như một con chó dại lạc cả đường về."),
    ("А мы, господа христиански, лукавством жить не умеем, а браниться и тягаться с лихими людьми не хотим, а хотим быть оборонены вами, праведными судьями».",
     "Còn chúng con, thưa các ngài, là dân lương thiện ngoan đạo, chẳng biết sống bằng mánh khoé, cũng chẳng muốn cãi cọ kiện tụng với phường gian ác, chỉ mong được các ngài — những vị quan toà công minh — chở che bênh vực»."),
    ("Судьи спрашивали ответчика Ерша: «Ты, Ерш, истцу Лещу отвечаешь ли?»",
     "Các quan toà hỏi bị cáo Cá Gai: «Này Cá Gai, ngươi có đối đáp gì với nguyên cáo Cá Vền không?»"),
    ("Ответчик Ерш рече: «Отвечаю, господа, за себя и за товарищев своих в том, что то Ростовское озеро было старина дедов наших, а ныне наше, и он, Лещ, жил у нас в суседстве на дне озера, а на свет не выхаживал.",
     "Bị cáo Cá Gai thưa rằng: «Con xin đáp, thưa các ngài, đáp thay cho cả con lẫn các bạn hữu của con, rằng hồ Rostov ấy xưa nay vốn là của ông cha chúng con, mà nay vẫn là của chúng con, còn hắn, Cá Vền, vốn sống cạnh nhà chúng con dưới đáy hồ, chẳng mấy khi ngoi lên mặt nước thấy ánh sáng."),
    ("А я, господа, Ерш, божиею милостию, отца своего благословением и матерними молитвами не смутщик, не вор, не тать и не разбойник, в приводе нигде не бывал, воровского у меня ничего не вынимывали; человек я доброй, живу я своею силою, а не чужою;",
     "Còn con đây, thưa các ngài, là Cá Gai, nhờ ơn Chúa, nhờ phúc lành của cha và lời cầu nguyện của mẹ, con chẳng phải quân gây rối, chẳng phải kẻ trộm, chẳng phải đứa đạo chích hay tên cướp, chưa từng bị giải lên cửa quan nơi nào, người ta chưa từng moi ra ở con thứ gì là của ăn cắp; con là người lương thiện, sống bằng sức mình chứ chẳng nhờ sức kẻ khác;"),
    ("знают меня на Москве и в иных великих городах князи и бояря, стольники и дворяня, жильцы московские, дьяки и подьячие, и всяких чинов люди, и покупают меня дорогою ценою и варят меня с перцом и с шафраном, и ставят пред собою честно, и многие добрые люди кушают с похмелья и, кушавши, поздравляют».",
     "ở Mátxcơva và các thành lớn khác, từ các vương công, boyar, các quan thị-thiện, quý tộc, dân cư kinh thành, các quan thư-lại, viên-lại cho đến đủ mọi hạng phẩm trật, ai cũng biết tiếng con; họ mua con với giá đắt, đem nấu con với hạt tiêu và nghệ tây, rồi trịnh trọng bày con ra trước mặt, và nhiều bậc quân tử lúc say rượu váng đầu đem con ra ăn cho giã rượu, ăn xong còn tấm tắc khen ngon»."),
    ("Судьи спрашивали истца Леща: «Ты, Лещ, чем его уличаешь?» Истец Лещ рече: «Уличаю его божиею правдою да вами, праведными судьями».",
     "Các quan toà hỏi nguyên cáo Cá Vền: «Này Cá Vền, ngươi lấy gì làm bằng chứng buộc tội hắn?» Nguyên cáo Cá Vền thưa: «Con buộc tội hắn bằng lẽ phải của Chúa và bằng chính các ngài, những vị quan toà công minh»."),
    ("Судьи спрашивали истца Леща: «Кому у тебя ведомо про Ростовское озеро и о реках и о востоках и на кого шлешься?» Истец Лещ рече: «Шлюся я, господа, из виноватых на добрых людей разных городов и области;",
     "Các quan toà lại hỏi nguyên cáo Cá Vền: «Còn ai biết rõ chuyện hồ Rostov, chuyện các sông các nguồn nước, và ngươi xin viện ai ra làm chứng?» Nguyên cáo Cá Vền thưa: «Thưa các ngài, là kẻ bị hàm oan, con xin viện ra những người lương thiện ở các thành các vùng khác nhau;"),
    ("есть, господа, человек доброй, живет в немецкой области под Иваном-городом в реке Нарве, по имени рыба Сиг, да другой, господа, человек доброй, живет в Новгородской области в реке Волхове, по имени рыба Лодуга».",
     "thưa các ngài, có một người lương thiện sống ở vùng người Đức, gần thành Ivangorod, trên sông Narva, tên là Cá Sig; lại có một người lương thiện khác sống ở vùng Novgorod, trên sông Volkhov, tên là Cá Loduga»."),
    ("Спрашивали ответчика Ерша: «Ты, Ерш, шлешься ли на лещову правду, на таковых людей?» И ответчик Ерш рече: «Слатися, господа, нам на таковых людей не уметь; Сиг и Лодуга — люди богатые, животами прожиточны, а Лещ такой же человек заводной, шлемся в послушество».",
     "Các quan toà hỏi bị cáo Cá Gai: «Này Cá Gai, ngươi có chịu nhận những người ấy ra làm chứng cho lẽ phải của Cá Vền không?» Bị cáo Cá Gai thưa: «Thưa các ngài, những người như thế con đâu dám viện ra; Cá Sig với Cá Loduga là hạng giàu có, của cải dư dật, còn Cá Vền cũng là phường khá giả như vậy, chúng con xin được viện người khác ra làm chứng»."),
    ("И судьи спрашивали ответчика Ерша: «Почему у тебя такие люди недрузья и какая у тебя с ними недружба?» Ответчик Ерш рече: «Господа мои судьи! Недружбы у нас с ними никакой не было, а слатися на них не смеем — для того что Сиг и Лодуга люди великие, а Лещ такой же человек заводной; они хотят нас, маломочных людей, испродать напрасно».",
     "Các quan toà hỏi bị cáo Cá Gai: «Cớ sao những người ấy lại là kẻ chẳng ưa ngươi, ngươi với họ có mối bất hoà gì?» Bị cáo Cá Gai thưa: «Thưa các quan toà của con! Giữa chúng con với họ chẳng có mối bất hoà nào, nhưng con không dám viện họ ra — bởi Cá Sig với Cá Loduga là bậc quyền quý, mà Cá Vền cũng là phường khá giả như thế; họ chỉ chực đem bọn con — những kẻ thấp cổ bé họng — ra bán đứng một cách oan uổng»."),
    ("Судьи спрашивали истца Леща: «Еще кому у тебя ведомо Ростовское озеро и о реках и о востоках, и на кого шлешься?» Истец Лещ рече: «Шлюсь я, господа, из виноватых есть человек доброй, живет в Переславском озере, рыба Сельдь».",
     "Các quan toà lại hỏi nguyên cáo Cá Vền: «Còn ai nữa biết rõ hồ Rostov, chuyện các sông các nguồn nước, và ngươi xin viện thêm ai ra làm chứng?» Nguyên cáo Cá Vền thưa: «Thưa các ngài, kẻ bị hàm oan này xin viện ra: có một người lương thiện sống ở hồ Pereslavl, tên là Cá Trích»."),
    ("Судьи спрашивали ответчика Ерша: «Ты, Ерш, шлешься ли на лещовую правду?» Ответчик же Ерш рече: «Сиг, и Лодуга, и Сельдь с племяни, а Лещ такой же человек заводной: в суседстве имаются, где судятся — едят и пьют вместе, про нас не молвят».",
     "Các quan toà hỏi bị cáo Cá Gai: «Này Cá Gai, ngươi có chịu nhận người ấy ra làm chứng cho lẽ phải của Cá Vền không?» Bị cáo Cá Gai lại thưa: «Cá Sig, Cá Loduga với Cá Trích đều là họ hàng thân thích, mà Cá Vền cũng là phường khá giả như vậy: chúng đều là chỗ láng giềng quen biết, hễ ra toà thì lại ăn cùng mâm uống cùng chén, chẳng đời nào nói nửa lời thật về bọn con»."),
    ("И судьи послали пристава Окуня и велели взять с собою в понятых Мня, приказали взять в правде переславскую Сельдь.",
     "Thế là các quan toà phái viên mõ toà Cá Rô đi, dặn dẫn theo Cá Méng làm người chứng, truyền đòi Cá Trích xứ Pereslavl ra làm chứng cho công minh."),
    ("Пристав же Окунь емлет в понятых Мня, и Мень Окуню-приставу сулит посулы великие и рече: «Господине Окуне! Аз не гожуся в понятых быть: брюхо у меня велико — ходить не смогу, а се глаза малы — далеко не вижу, а се губы толсты — перед добрыми людьми говорить не умею».",
     "Viên mõ toà Cá Rô bèn chọn Cá Méng làm người chứng, nhưng Cá Méng hứa đút lót cho mõ toà Cá Rô những món hậu hĩnh mà rằng: «Thưa ngài Cá Rô! Con chẳng kham nổi việc làm chứng đâu: bụng con thì to — đi đứng chẳng nổi, mắt con thì nhỏ — chẳng nhìn được xa, môi con thì dày — trước mặt người lương thiện con ăn nói chẳng nên lời»."),
    ("Пристав же Окунь емлет в понятых Головля и Язя. И Окунь поставил в правде переславскую Сельдь.",
     "Viên mõ toà Cá Rô bèn chọn Cá Chày và Cá Ide làm người chứng. Rồi Cá Rô đưa được Cá Trích xứ Pereslavl ra làm chứng cho công minh."),
    ("И судьи спрашивали в правде у переславской Сельди: «Сельдь, скажи ты нам про Леща, и про Ерша, и промеж ими про Ростовское озеро». Сельдь же рече в правде: «Леща с товарищи знают; Лещ человек доброй, христианин божий, живет своею, а не чужою; а Ерш, господа, злой человек Щетинник».",
     "Các quan toà hỏi nhân chứng Cá Trích xứ Pereslavl: «Này Cá Trích, hãy nói cho chúng ta nghe về Cá Vền, về Cá Gai, và về cái hồ Rostov ở giữa hai bên». Cá Trích bèn khai thật: «Cá Vền cùng các bạn hữu thì ai cũng biết; Cá Vền là người lương thiện, con chiên ngoan đạo của Chúa, sống bằng sức mình chứ chẳng nhờ kẻ khác; còn Cá Gai, thưa các ngài, là kẻ ác họ Lông-Cứng»."),
    ("«...знаешь ли его?» Осетр же рече: «Аз, господа, не в правде и не в послушестве, а впрямь скажу: слышал про того Ерша, что сварят его в ухе, а столько не едят, сколько расплюют.",
     "«...ngươi có biết hắn không?» Cá Tầm bèn thưa: «Thưa các ngài, con xin nói không phải với tư cách nhân chứng tuyên thệ, mà nói thẳng cho thật: con có nghe về tên Cá Gai ấy — rằng đem nó nấu canh thì ăn được bao nhiêu, mà nhổ phun xương ra còn nhiều hơn bấy nhiêu."),
    ("Да еще, господа, вам скажу божиею правдою о своей обиде: когда я шел из Волги-реки к Ростовскому озеру и к рекам жировать и он меня встретил на устье Ростовского озера и нарече мя братом;",
     "Mà thưa các ngài, con xin lấy lẽ phải của Chúa kể thêm về nỗi oan ức của chính con: khi con từ sông Volga bơi tới hồ Rostov và các sông để kiếm ăn cho béo, thì hắn gặp con ngay nơi cửa hồ Rostov và gọi con là anh em;"),
    ("а я лукавства его не ведал, а спрошать про него, злого человека, никого не лучилось, и он меня вопроси: «Братец Осетр, где идеши?» И аз ему поведал: «Иду к Ростовскому озеру и к рекам жировать».",
     "con nào hay biết mưu mô gian xảo của hắn, mà hỏi dò về cái kẻ ác ấy thì lại chẳng gặp được ai, thế rồi hắn hỏi con: «Anh Cá Tầm ơi, anh đi đâu đấy?» Con bèn kể cho hắn: «Tôi đi tới hồ Rostov và các sông để kiếm ăn cho béo»."),
    ("И рече ми Ерш: «Братец Осетр, когда аз шел Волгою-рекою, тогда аз был толще тебя и до́ле, бока мои терли у Волги-реки берега, очи мои были аки полная чаша, хвост же мой был аки большой судовой парус; а ныне, братец Осетр, видишь ты и сам, каков я стал скуден, иду из Ростовского озера».",
     "Cá Gai bèn bảo con: «Anh Cá Tầm ơi, hồi tôi còn xuôi sông Volga, tôi từng to hơn anh, dài hơn anh, hai sườn tôi cọ sát cả vào bờ sông Volga, đôi mắt tôi như cái chén đầy, còn cái đuôi tôi thì như cánh buồm lớn của thuyền lớn; thế mà nay, anh Cá Tầm ơi, chính anh cũng thấy đấy, tôi đã ra nông nỗi tiều tụy thế này, đang phải bỏ hồ Rostov mà đi»."),
    ("Аз же, господа, слышав такое его прелестное слово, и не пошел в Ростовское озеро к рекам жировать; дружину свою и детей голодом поморил, а сам от него вконец погинул.",
     "Thưa các ngài, nghe những lời đường mật dối trá ấy của hắn, con đã không tới hồ Rostov và các sông kiếm ăn nữa; thế là con để cả đàn tuỳ tùng và con cái mình chết đói, mà bản thân con cũng vì hắn mà khốn cùng đến nơi."),
    ("Да еще вам, господа, скажу: тот же Ерш обманул меня, Осетра, старого мужика, и приведе меня к неводу, и рече ми: «Братец Осетр, пойдем в невод; есть там рыбы много». И я его нача посылати напредь.",
     "Mà con xin thưa thêm với các ngài: cũng chính tên Cá Gai ấy đã lừa con — Cá Tầm, một lão già — dẫn con đến chỗ tấm lưới vét mà bảo: «Anh Cá Tầm ơi, ta chui vào lưới đi; trong đó lắm cá lắm». Con bèn giục hắn chui vào trước."),
    ("И он, Ерш, мне рече: «Братец Осетр, коли меньшей брат ходит напредь большего?» И я на его, господа, прелестное слово положился и в невод пошел, обратился в невод да увяз, а невод что боярский двор — идти ворота широки, а выйти узки.",
     "Hắn, Cá Gai, liền bảo con: «Anh Cá Tầm ơi, đời nào em út lại đi trước bậc đàn anh?» Thưa các ngài, con cả tin lời đường mật của hắn nên chui vào lưới, vừa quay mình trong lưới là đã mắc kẹt cứng, mà cái lưới ấy chẳng khác gì phủ đệ nhà quan — cổng vào thì rộng thênh, cổng ra thì hẹp rí."),
    ("А тот Ерш за невод выскочил в ечею, а сам мне насмехался: «Ужели ты, братец, в неводу рыбы наелся!» А как меня поволокли вон из воды, и тот Ерш нача прощатися: «Братец, братец Осетр! Прости, не поминай лихом».",
     "Còn tên Cá Gai thì luồn qua mắt lưới mà vọt ra ngoài, lại còn nhạo báng con: «Thế nào, anh ơi, đã chén no cá trong lưới chưa nào!» Đến khi người ta lôi xềnh xệch con ra khỏi nước, thì tên Cá Gai ấy lại bắt đầu từ biệt: «Anh ơi, anh Cá Tầm ơi! Thứ lỗi cho em, đừng giận em mà nhớ đến điều dữ»."),
    ("А как меня мужики на берегу стали бить дубинами по голове и я нача стонать, и он, Ерш, рече ми: «Братец Осетр, терпи Христа ради!»",
     "Đến lúc đám mu-gích trên bờ lấy chày nện vào đầu con khiến con bắt đầu rên la, thì hắn, Cá Gai, bảo con: «Anh Cá Tầm ơi, ráng chịu vì Chúa Ki-tô đi!»"),
    ("Конец судного дела. Судьи слушали судного дела и приговорили: Леща с товарищи оправить, а Ерша обвинить.",
     "Hết hồ sơ vụ án. Các quan toà nghe xong hồ sơ bèn tuyên án: xử Cá Vền cùng các bạn hữu trắng án, còn Cá Gai thì kết tội."),
    ("И выдали истцу Лещу того Ерша головою и велели казнить торговою казнию — бити кнутом и после кнута повесить в жаркие дни против солнца за его воровство и за ябедничество.",
     "Rồi toà giao nộp tên Cá Gai cho nguyên cáo Cá Vền toàn quyền định đoạt, truyền hành hình nó theo lối «hình phạt chốn chợ» — đánh bằng roi da, đánh roi xong thì đem treo phơi giữa nắng những ngày oi bức, đối mặt mặt trời, để trừng cái tội trộm cắp và vu cáo của nó."),
    ("А у судного дела сидели люди добрые: дьяк был Сом с большим усом, а доводчик Карась, а список с судного дела писал Вьюн, а печатал Рак своей заднею клешнею, а у печати сидел Вандыш переславский.",
     "Ngồi xử vụ án này có những người tử tế: quan thư-lại là Cá Nheo râu dài, viên trát-lại là Cá Diếc, bản sao hồ sơ vụ án do Cá Chạch chép, đóng dấu là con Tôm bằng cái càng sau của mình, còn coi giữ ấn triện là Cá Mại xứ Pereslavl."),
    ("Да на того же Ерша выдали правую грамоту, где его застанут в своих вотчинах, тут его без суда казнить.",
     "Lại còn cấp cho bên thắng một tờ trát hợp lệ về tên Cá Gai ấy: hễ bắt gặp nó trên lãnh địa của ai thì cứ ngay tại đó hành hình nó, chẳng cần xét xử gì nữa."),
    ("Речет Ерш судьям: «Господа судьи! Судили вы не по правде, судили по мзде. Леща с товарищи оправили, а меня обвинили». Плюнул Ерш судьям в глаза и скочил в хворост: только того Ерша и видели.",
     "Cá Gai nói với các quan toà: «Thưa các quan toà! Các ngài xử chẳng theo lẽ phải, các ngài xử theo của đút. Cá Vền cùng các bạn hữu thì được trắng án, còn con thì bị kết tội». Cá Gai nhổ toẹt vào mắt các quan toà rồi phóng tọt vào bụi rậm: thế là từ đó chẳng còn ai thấy tăm hơi tên Cá Gai ấy nữa."),
]
s004_vocab = [
    ("белуга", "cá tầm trắng / cá tầm beluga (Huso huso); một trong các quan toà"),
    ("белорыбица", "cá bạch ngư (Stenodus leucichthys), loài cá tầm-trắng quý"),
    ("сиг", "cá trắng (whitefish, Coregonus); nhân chứng «người Đức»"),
    ("лодуга", "(= ряпушка ладожская) một loài cá trắng nhỏ hồ Ladoga"),
    ("вьюн", "cá chạch (weatherfish, Misgurnus fossilis); ở đây làm người chép án"),
    ("вандыш", "(phương ngữ) cá mại / cá vụn nhỏ phơi khô (xứ Pereslavl)"),
    ("бить челом", "(cổ) dập đầu kêu xin, đệ đơn thỉnh cầu lên quan/vua"),
    ("ябедник", "kẻ vu cáo, quân chuyên mách lẻo kiện cáo bậy"),
    ("истец", "nguyên cáo (bên đứng đơn kiện)"),
    ("ответчик", "bị cáo (bên bị kiện)"),
    ("пристав", "viên mõ toà, sai dịch áp giải/đòi người ra toà"),
    ("доводчик", "(cổ) viên trát-lại / điều tra ở cửa quan"),
    ("мзда", "của đút lót, của hối lộ"),
    ("вотчина", "lãnh địa cha truyền con nối (thái ấp thế tập)"),
    ("тать", "(cổ) kẻ trộm"),
    ("прелестный", "(cổ) dụ dỗ, lừa mị, dối trá (прелестное слово = lời đường mật gian trá)"),
]

def make_section(sid, num, title, note, paras, vocab):
    blocks = [{"t": "note", "text": note}]
    for ru, vi in paras:
        blocks.append(P(ru, vi))
    blocks.append({"t": "subhead", "text": "Từ khó trong truyện"})
    for ru, vi in vocab:
        blocks.append({"t": "vocab", "ru": ru, "vi": vi, "g": None})
    return {"id": sid, "type": "story", "num": num, "title": title, "blocks": blocks}

s003 = make_section("skazki1-044-s003", 79,
    "№ 79 · Сказка о Ерше Ершовиче, сыне Щетинникове — Truyện Cá Gai Ershovich (bản 3, thơ)",
    s003_note, s003_paras, s003_vocab)
s004 = make_section("skazki1-044-s004", 80,
    "№ 80 · Сказка о Ерше Ершовиче, сыне Щетинникове — Truyện Cá Gai Ershovich (bản 4, hồ sơ vụ án)",
    s004_note, s004_paras, s004_vocab)

# ---- 1) Update unit file ----
unit = json.load(open(UNIT, encoding="utf-8"))
existing_ids = {s["id"] for s in unit["sections"]}
for sec in (s003, s004):
    if sec["id"] in existing_ids:
        raise SystemExit("ERROR: section already exists: " + sec["id"])
unit["sections"].extend([s003, s004])
json.dump(unit, open(UNIT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("unit sections now:", [s["id"] for s in unit["sections"]])

# ---- 2) Update glossary (dedup by accent-stripped, lowercased ru) ----
def norm(s):
    return s.replace("́", "").replace("̀", "").lower().strip()

gloss = json.load(open(GLOSS, encoding="utf-8"))
have = {norm(e["ru"]) for e in gloss["entries"]}
added = 0
for sid, vocab in (("skazki1-044-s003", s003_vocab), ("skazki1-044-s004", s004_vocab)):
    for ru, vi in vocab:
        if norm(ru) in have:
            print("  skip dup glossary:", ru)
            continue
        gloss["entries"].append({
            "ru": ru,
            "ruPlain": ru.replace("́", "").replace("̀", ""),
            "vi": vi,
            "g": None,
            "ref": sid,
        })
        have.add(norm(ru))
        added += 1
gloss["count"] = len(gloss["entries"])
json.dump(gloss, open(GLOSS, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("glossary added:", added, "-> total", gloss["count"])

# ---- 3) Update book.json sectionCount for skazki1-044 ----
book = json.load(open(BOOK, encoding="utf-8"))
for p in book["parts"]:
    if p.get("id") == "skazki1-044":
        p["sectionCount"] = 4
        print("book.json skazki1-044 sectionCount ->", p["sectionCount"])
json.dump(book, open(BOOK, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("DONE")
