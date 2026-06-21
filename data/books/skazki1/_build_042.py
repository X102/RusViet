# -*- coding: utf-8 -*-
"""Build unit skazki1-042 «Золотая рыбка» (№75) + update glossary.json + book.json."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))

UID = "skazki1-042"
SEC = "skazki1-042-s001"

note = ("Truyện «Cá vàng» — bản truyện cổ dân gian Nga mà sau này thi hào Pushkin dựa vào để viết "
        "«Truyện ông lão đánh cá và con cá vàng» (1833). Mô-típ «điều ước leo thang» (ATU 555 «Ông lão, "
        "bà lão và con cá»): con cá thần đền ơn ông lão hiền lành bằng những điều ước mỗi lúc một quá quắt "
        "theo lòng tham không đáy của bà lão — từ bánh mì, máng giặt, nhà mới, lên bà phủ, rồi hoàng hậu, "
        "rồi đòi làm Chúa tể biển cả — để rồi mất sạch, trở về túp lều rách cũ. Truyện mở đầu bằng công thức "
        "cổ tích quen thuộc «На море на океане, на острове на Буяне» (hòn đảo Bu-i-an thần thoại), và câu gọi "
        "cá «Стань в море хвостом, ко мне головой» lặp lại như một điệp khúc.")

# (ru, vi) — từng câu / lượt thoại
pairs = [
 ("На море на океане, на острове на Буяне стояла небольшая ветхая избушка; в той избушке жили старик да старуха.",
  "Ngày xửa ngày xưa, ngoài biển khơi đại dương, trên hòn đảo Bu-i-an, có một túp lều nhỏ cũ nát; trong túp lều ấy có hai ông bà già sinh sống."),
 ("Жили они в великой бедности; старик сделал сеть и стал ходить на́ море да ловить рыбу: тем только и добывал себе дневное пропитание.",
  "Hai ông bà sống trong cảnh nghèo khó cùng cực; ông lão đan một tấm lưới rồi ngày ngày ra biển đánh cá: chỉ nhờ thế mà kiếm được miếng ăn qua ngày."),
 ("Раз как-то закинул старик свою сеть, начал тянуть, и показалось ему так тяжело, как доселева никогда не бывало: еле-еле вытянул.",
  "Một bận nọ, ông lão quăng lưới xuống biển rồi bắt đầu kéo, thấy nặng trĩu chưa từng nặng đến thế bao giờ: phải gắng hết sức mới lôi được lên."),
 ("Смотрит, а сеть пуста; всего-навсего одна рыбка попалась, зато рыбка не простая — золотая.",
  "Nhìn vào thì lưới trống không; vỏn vẹn chỉ mắc được mỗi một con cá, nhưng đó chẳng phải cá thường — mà là cá vàng."),
 ("Возмолилась ему рыбка человечьим голосом: «Не бери меня, старичок! Пусти лучше в сине море; я тебе сама пригожусь: что пожелаешь, то и сделаю».",
  "Con cá cất tiếng người van xin ông lão: «Đừng bắt con, ông lão ơi! Ông hãy thả con về biển xanh thì hơn; rồi tự con sẽ có ích cho ông: ông ước gì, con liền làm cho nấy.»"),
 ("Старик подумал-подумал и говорит: «Мне ничего от тебя не надобно: ступай гуляй в море!»",
  "Ông lão nghĩ đi nghĩ lại rồi bảo: «Ta chẳng cần gì ở ngươi cả: thôi ngươi cứ về vùng vẫy ngoài biển đi!»"),
 ("Бросил золотую рыбку в воду и воротился домой.",
  "Ông thả con cá vàng xuống nước rồi quay về nhà."),
 ("Спрашивает его старуха: «Много ли поймал, старик?»",
  "Bà lão hỏi ông: «Ông đánh được nhiều cá không, ông lão?»"),
 ("«Да всего-навсего одну золотую рыбку, и ту бросил в море; крепко она возмолилась: отпусти, говорила, в сине море; я тебе в пригоду стану: что пожелаешь, все сделаю!",
  "«Chỉ vỏn vẹn được mỗi một con cá vàng, mà ta cũng thả về biển rồi; nó van xin ta thống thiết lắm: thả con về biển xanh đi, nó bảo; rồi con sẽ giúp ích cho ông: ông muốn gì con cũng làm được tất!"),
 ("Пожалел я рыбку, не́ взял с нее выкупу, даром на волю пустил».",
  "Ta thương con cá, chẳng đòi nó chuộc gì, cứ thế thả nó về tự do không công.»"),
 ("«Ах ты, старый черт! Попалось тебе в руки большое счастье, а ты и владать не сумел».",
  "«Ôi cái lão già khốn kiếp! Vận may lớn rơi vào tay mà lão chẳng biết giữ lấy gì cả.»"),
 ("Озлилась старуха, ругает старика с утра до вечера, не дает ему спокоя:",
  "Bà lão nổi đoá, chửi mắng ông từ sáng đến tối, chẳng để ông yên lúc nào:"),
 ("«Хоть бы хлеба у ней выпросил! Ведь скоро сухой корки не будет; что жрать-то станешь?»",
  "«Ít ra cũng phải xin nó lấy ít bánh mì chứ! Chẳng mấy chốc đến mẩu bánh khô cũng không còn; rồi lấy gì mà tọng vào mồm hả?»"),
 ("Не выдержал старик, пошел к золотой рыбке за хлебом; пришел на́ море и крикнул громким голосом:",
  "Ông lão không chịu nổi nữa, bèn đi tìm con cá vàng xin bánh; ra đến biển, ông cất tiếng gọi to:"),
 ("«Рыбка, рыбка! Стань в море хвостом, ко мне головой».",
  "«Cá ơi, cá hỡi! Quay đuôi ra biển, chĩa đầu vào ta.»"),
 ("Рыбка приплыла к берегу: «Что тебе, старик, надо?»",
  "Con cá bơi vào bờ: «Ông lão cần gì thế?»"),
 ("«Старуха осерчала, за хлебом прислала».",
  "«Bà lão nhà ta nổi giận, sai ta đến xin bánh mì.»"),
 ("«Ступай домой, будет у вас хлеба вдоволь».",
  "«Ông cứ về nhà đi, bánh mì nhà ông sẽ có thừa thãi.»"),
 ("Воротился старик: «Ну что, старуха, есть хлеб?»",
  "Ông lão trở về: «Thế nào, bà nó, có bánh chưa?»"),
 ("«Хлеба-то вдоволь; да вот беда: корыто раскололось, не в чем белье мыть; ступай к золотой рыбке, попроси, чтоб новое дала».",
  "«Bánh thì thừa thãi rồi; nhưng khổ nỗi: cái máng giặt nứt toác mất rồi, chẳng có gì mà giặt giũ; ông đến chỗ cá vàng, xin nó cho cái máng mới đi.»"),
 ("Пошел старик на́ море: «Рыбка, рыбка! Стань в море хвостом, ко мне головой».",
  "Ông lão lại ra biển: «Cá ơi, cá hỡi! Quay đuôi ra biển, chĩa đầu vào ta.»"),
 ("Приплыла золотая рыбка: «Что тебе надо, старик?»",
  "Con cá vàng bơi tới: «Ông lão cần gì nào?»"),
 ("«Старуха прислала, новое корыто просит».",
  "«Bà lão sai ta đến, xin một cái máng giặt mới.»"),
 ("«Хорошо, будет у вас и корыто».",
  "«Được thôi, nhà ông sẽ có cả máng giặt.»"),
 ("Воротился старик, — только в дверь, а старуха опять на него накинулась:",
  "Ông lão trở về, — vừa bước qua cửa, bà lão đã lại xông vào mắng nhiếc:"),
 ("«Ступай, — говорит, — к золотой рыбке, попроси, чтоб новую избу построила; в нашей жить нельзя, того и смотри что развалится!»",
  "«Ông đi đi, — bà bảo, — đến chỗ cá vàng, xin nó dựng cho một ngôi nhà mới; nhà mình chẳng ở được nữa, chỉ chực sập đến nơi rồi!»"),
 ("Пошел старик на́ море: «Рыбка, рыбка! Стань в море хвостом, ко мне головой».",
  "Ông lão lại ra biển: «Cá ơi, cá hỡi! Quay đuôi ra biển, chĩa đầu vào ta.»"),
 ("Рыбка приплыла, стала к нему головой, в море хвостом и спрашивает: «Что тебе, старик, надо?»",
  "Con cá bơi tới, chĩa đầu vào ông, quay đuôi ra biển rồi hỏi: «Ông lão cần gì thế?»"),
 ("«Построй нам новую избу; старуха ругается, не дает мне спокою; не хочу, говорит, жить в старой избушке: она того и смотри вся развалится!»",
  "«Hãy dựng cho vợ chồng ta một ngôi nhà mới; bà lão cứ chửi rủa, chẳng để ta yên; bà bảo không muốn ở trong túp lều cũ nữa: nó chỉ chực đổ sập cả đến nơi rồi!»"),
 ("«Не тужи, старик! Ступай домой да молись богу, все будет сделано».",
  "«Đừng buồn phiền, ông lão! Cứ về nhà cầu nguyện Trời, mọi sự sẽ thành.»"),
 ("Воротился старик — на его дворе стоит изба новая, дубовая, с вырезными узорами.",
  "Ông lão trở về — giữa sân đã sừng sững một ngôi nhà mới, dựng bằng gỗ sồi, chạm trổ hoa văn."),
 ("Выбегает к нему навстречу старуха, пуще прежнего сердится, пуще прежнего ругается:",
  "Bà lão chạy ra đón ông, còn giận dữ hơn trước, còn chửi rủa dữ hơn trước:"),
 ("«Ах ты, старый пес! Не умеешь ты счастьем пользоваться.",
  "«Ôi cái lão chó già kia! Lão chẳng biết hưởng phúc gì cả."),
 ("Выпросил избу и, чай, думаешь — дело сделал!",
  "Xin được cái nhà, lão chắc lại tưởng thế là xong việc rồi chứ gì!"),
 ("Нет, ступай-ка опять к золотой рыбке да скажи ей: не хочу я быть крестьянкою, хочу быть воеводихой, чтоб меня добрые люди слушались, при встречах в пояс кланялись».",
  "Không đâu, lão lại đến chỗ cá vàng mà bảo nó: ta chẳng muốn làm đàn bà nhà quê nữa, ta muốn làm bà phủ, để người ta phải nghe lời ta, hễ gặp thì cúi gập người chào.»"),
 ("Пошел старик на́ море, говорит громким голосом: «Рыбка, рыбка! Стань в море хвостом, ко мне головой».",
  "Ông lão ra biển, cất tiếng gọi to: «Cá ơi, cá hỡi! Quay đuôi ra biển, chĩa đầu vào ta.»"),
 ("Приплыла рыбка, стала в море хвостом, к нему головой: «Что тебе, старик, надо?»",
  "Con cá bơi tới, quay đuôi ra biển, chĩa đầu vào ông: «Ông lão cần gì thế?»"),
 ("Отвечает старик: «Не дает мне старуха спокою, совсем вздурилась: не хочет быть крестьянкою, хочет быть воеводихой».",
  "Ông lão đáp: «Bà lão chẳng để ta yên, đâm ra dở hơi hẳn rồi: chẳng muốn làm đàn bà nhà quê, lại đòi làm bà phủ.»"),
 ("«Хорошо, не тужи! Ступай домой да молись богу, все будет сделано».",
  "«Được thôi, đừng buồn phiền! Cứ về nhà cầu nguyện Trời, mọi sự sẽ thành.»"),
 ("Воротился старик, а вместо избы каменный дом стоит, в три этажа выстроен;",
  "Ông lão trở về, thì chỗ ngôi nhà gỗ nay đã là một toà nhà đá, xây cao ba tầng;"),
 ("по́ двору прислуга бегает, на кухне повара стучат, а старуха в дорогом парчовом платье на высоких креслах сидит да приказы отдает.",
  "khắp sân kẻ hầu người hạ chạy ngược xuôi, dưới bếp đầu bếp băm chặt rộn ràng, còn bà lão thì vận áo gấm đắt tiền, ngồi chễm chệ trên chiếc ghế bành cao mà sai bảo ra lệnh."),
 ("«Здравствуй, жена!» — говорит старик.",
  "«Chào bà nó!» — ông lão nói."),
 ("«Ах ты, невежа этакой! Как смел обозвать меня, воеводиху, своею женою?",
  "«À cái đồ thô lỗ kia! Sao lão dám gọi ta, bà phủ đây, là vợ lão hả?"),
 ("Эй, люди! Взять этого мужичонка на конюшню и отодрать плетьми как можно больнее».",
  "Bay đâu! Lôi cái lão nhà quê quèn này ra tàu ngựa mà quật roi cho thật đau vào!»"),
 ("Тотчас прибежала прислуга, схватила старика за шиворот и потащила в конюшню;",
  "Lập tức bọn người hầu chạy ùa tới, túm gáy ông lão lôi xềnh xệch ra tàu ngựa;"),
 ("начали конюхи угощать его плетьми, да так угостили, что еле на ноги поднялся.",
  "đám giữ ngựa bắt đầu nện roi cho ông một trận, nện đến mức ông gắng lắm mới gượng đứng dậy nổi."),
 ("После того старуха поставила старика дворником; велела дать ему метлу, чтоб двор убирал, а кормить и поить его на кухне.",
  "Sau đó bà lão đặt ông lão làm phu quét sân; sai đưa cho ông một cây chổi để quét dọn ngoài sân, còn ăn uống thì cho xuống bếp."),
 ("Плохое житье старику: целый день двор убирай, а чуть где нечисто — сейчас на конюшню!",
  "Đời ông lão khốn khổ: cả ngày phải quét sân, hễ chỗ nào bẩn một tí — là lập tức bị điệu ra tàu ngựa!"),
 ("«Экая ведьма! — думает старик. — Далось ей счастье, а она как свинья зарылась, уж и за мужа меня не считает!»",
  "«Cái mụ phù thuỷ này! — ông lão nghĩ bụng. — Phúc lành đến tay mụ, mà mụ vùi đầu hưởng như con lợn, đến chồng cũng chẳng còn coi ta ra gì nữa!»"),
 ("Ни много, ни мало прошло времени, придокучило старухе быть воеводихой, потребовала к себе старика и приказывает:",
  "Chẳng nhiều chẳng ít, một thời gian trôi qua, bà lão đâm chán cảnh làm bà phủ, bèn đòi ông lão đến rồi ra lệnh:"),
 ("«Ступай, старый черт, к золотой рыбке, скажи ей: не хочу я быть воеводихой, хочу быть царицею».",
  "«Đi đi, cái lão già khốn kiếp, đến chỗ cá vàng mà bảo nó: ta chẳng muốn làm bà phủ nữa, ta muốn làm hoàng hậu.»"),
 ("Пошел старик на́ море: «Рыбка, рыбка! Стань в море хвостом, ко мне головой».",
  "Ông lão ra biển: «Cá ơi, cá hỡi! Quay đuôi ra biển, chĩa đầu vào ta.»"),
 ("Приплыла золотая рыбка: «Что тебе, старик, надо?»",
  "Con cá vàng bơi tới: «Ông lão cần gì thế?»"),
 ("«Да что, вздурилась моя старуха пуще прежнего: не хочет быть воеводихой, хочет быть царицею».",
  "«Khổ lắm, bà lão nhà ta dở chứng còn hơn trước: chẳng muốn làm bà phủ nữa, lại đòi làm hoàng hậu.»"),
 ("«Не тужи! Ступай домой да молись богу, все будет сделано».",
  "«Đừng buồn phiền! Cứ về nhà cầu nguyện Trời, mọi sự sẽ thành.»"),
 ("Воротился старик, а вместо прежнего дома высокий дворец стоит под золотою крышею;",
  "Ông lão trở về, thì chỗ toà nhà cũ nay đã là một cung điện nguy nga dưới mái vàng;"),
 ("кругом часовые ходят да ружьями выкидывают; позади большой сад раскинулся, а перед самым дворцом — зеленый луг; на лугу войска собраны.",
  "xung quanh lính canh đi đi lại lại, bồng súng diễu giáo; phía sau trải rộng một khu vườn lớn, còn ngay trước cung điện là một bãi cỏ xanh; trên bãi cỏ quân lính tập hợp đông nghịt."),
 ("Старуха нарядилась царицею, выступила на балкон с генералами да с боярами и начала делать тем войскам смотр и развод:",
  "Bà lão ăn vận như hoàng hậu, bước ra ban công cùng các tướng lĩnh và các quan đại thần, rồi bắt đầu duyệt binh và điều quân:"),
 ("барабаны бьют, музыка гремит, солдаты «ура» кричат!",
  "trống trận thì thùng, nhạc nổi vang trời, quân lính hô vang «ура»!"),
 ("Ни много, ни мало прошло времени, придокучило старухе быть царицею, велела разыскать старика и представить пред свои очи светлые.",
  "Chẳng nhiều chẳng ít, một thời gian trôi qua, bà lão lại đâm chán cảnh làm hoàng hậu, bèn sai đi tìm ông lão về trình diện trước long nhan sáng láng của mình."),
 ("Поднялась суматоха, генералы суетятся, бояре бегают: «Какой-такой старик?»",
  "Thế là rộn cả lên, các tướng lĩnh nháo nhào, các quan đại thần chạy ngược xuôi: «Lão già nào cơ chứ?»"),
 ("Насилу нашли его на заднем дворе, повели к царице.",
  "Mãi mới tìm thấy ông ở sân sau, bèn dẫn đến trước hoàng hậu."),
 ("«Слушай, старый черт! — говорит ему старуха.",
  "«Nghe đây, cái lão già khốn kiếp! — bà lão bảo ông."),
 ("Ступай к золотой рыбке да скажи ей: не хочу быть царицею, хочу быть морскою владычицей, чтобы все моря и все рыбы меня слушались».",
  "Đến chỗ cá vàng mà bảo nó: ta chẳng muốn làm hoàng hậu nữa, ta muốn làm Chúa tể biển cả, để hết thảy biển khơi và hết thảy loài cá phải nghe lời ta.»"),
 ("Старик было отнекиваться; куда тебе! коли не пойдешь — голова долой!",
  "Ông lão toan chối từ; nào có được! Không đi thì — mất đầu như chơi!"),
 ("Скрепя сердце пошел старик на́ море, пришел и говорит: «Рыбка, рыбка! Стань в море хвостом, ко мне головой».",
  "Ông lão đành nén lòng ra biển, đến nơi gọi: «Cá ơi, cá hỡi! Quay đuôi ra biển, chĩa đầu vào ta.»"),
 ("Золотой рыбки нет как нет! Зовет старик в другой раз — опять нету!",
  "Cá vàng tuyệt chẳng thấy đâu! Ông lão gọi lần thứ hai — vẫn chẳng có!"),
 ("Зовет в третий раз — вдруг море зашумело, взволновалося; то было светлое, чистое, а тут совсем почернело.",
  "Gọi đến lần thứ ba — biển bỗng gầm gào, sóng cuộn dữ dội; mặt biển vốn trong veo sáng tỏ, giờ tối sầm đen kịt."),
 ("Приплывает рыбка к берегу: «Что тебе, старик, надо?»",
  "Con cá bơi vào bờ: «Ông lão cần gì thế?»"),
 ("«Старуха еще пуще вздурилася; уж не хочет быть царицею, хочет быть морскою владычицей, над всеми водами властвовать, над всеми рыбами повелевать».",
  "«Bà lão nhà ta còn dở hơi hơn nữa; chẳng thèm làm hoàng hậu nữa rồi, lại đòi làm Chúa tể biển cả, thống trị hết thảy mọi vùng nước, sai khiến hết thảy mọi loài cá.»"),
 ("Ничего не сказала старику золотая рыбка, повернулась и ушла в глубину моря.",
  "Con cá vàng chẳng nói với ông lão một lời, quay mình lặn sâu xuống lòng biển."),
 ("Старик воротился назад, смотрит и глазам не верит:",
  "Ông lão quay về, nhìn mà chẳng tin nổi vào mắt mình nữa:"),
 ("дворца как не бывало, а на его месте стоит небольшая ветхая избушка, а в избушке сидит старуха в изодранном сарафане.",
  "cung điện biến đâu mất tăm, chỗ ấy lại là túp lều nhỏ cũ nát, còn trong lều là bà lão ngồi đó trong chiếc áo xa-ra-phan rách bươm."),
 ("Начали они жить по-прежнему, старик опять принялся за рыбную ловлю;",
  "Hai ông bà lại sống như xưa, ông lão lại quay về với nghề chài lưới;"),
 ("только как часто ни закидывал сетей в море, не удалось больше поймать золотой рыбки.",
  "có điều dù quăng lưới xuống biển bao nhiêu lần đi nữa, ông cũng chẳng còn bắt được con cá vàng nào nữa."),
]

# Từ khó (ru có dấu trọng âm, ruPlain bỏ dấu) — đã đối soát tránh trùng glossary
vocab = [
 ("ве́тхий", "ветхий", "cũ nát, mục nát, ọp ẹp (nhà cửa, đồ vật lâu năm)"),
 ("доселе́ва", "доселева", "(cổ = доселе) từ trước tới nay, cho đến tận lúc ấy"),
 ("возмоли́ться", "возмолиться", "van xin thống thiết, khẩn cầu, nài nỉ"),
 ("вы́куп", "выкуп", "tiền chuộc, vật chuộc (взять выкуп — đòi tiền chuộc)"),
 ("влада́ть", "владать", "(cổ/phương ngữ = владеть) nắm giữ, làm chủ, biết tận dụng"),
 ("осерча́ть", "осерчать", "nổi giận, phật ý, đâm cáu (từ dân dã)"),
 ("воеводи́ха", "воеводиха", "bà phủ — vợ của воевода (quan trấn thủ, thống lĩnh một vùng)"),
 ("парчо́вый", "парчовый", "bằng gấm, dệt gấm (парча — vải gấm thêu kim tuyến)"),
 ("коню́шня", "конюшня", "tàu ngựa, chuồng ngựa (xưa cũng là nơi đánh đòn người ở)"),
 ("дво́рник", "дворник", "phu quét sân, người gác cổng & quét dọn"),
 ("придоку́чить", "придокучить", "(từ докучать) đâm chán ngấy, phát ngán, sinh nhàm"),
 ("влады́чица", "владычица", "nữ chúa tể, bà chúa (морская владычица — Chúa tể biển cả)"),
 ("вздури́ться", "вздуриться", "đâm dở hơi, hoá rồ, giở chứng càn rỡ"),
 ("неве́жа", "невежа", "kẻ thô lỗ, đồ vô lễ, người cộc cằn bất lịch sự"),
 ("отне́киваться", "отнекиваться", "chối quanh, một mực từ chối, thoái thác"),
 ("скрепя́ се́рдце", "скрепя сердце", "(thành ngữ) nén lòng, đành lòng, miễn cưỡng làm việc gì"),
 ("Буя́н", "буян", "đảo Bu-i-an — hòn đảo thần thoại trong cổ tích Nga (công thức mở truyện)"),
]

# ---- build unit JSON ----
blocks = [{"t": "note", "text": note}]
for ru, vi in pairs:
    blocks.append({"t": "para", "text": "%s (%s)" % (ru, vi)})
blocks.append({"t": "subhead", "text": "Từ khó trong truyện"})
for ru, plain, vi in vocab:
    blocks.append({"t": "vocab", "ru": ru, "vi": vi, "g": None})

unit = {
 "id": UID,
 "num": 42,
 "title": "Золотая рыбка — Cá vàng",
 "vi": "Золотая рыбка — Cá vàng",
 "ru": "Золотая рыбка",
 "icon": "🐟",
 "color": "#b45309",
 "sectionPrefix": "skazki1-042-s",
 "group": "Truyện № 61–100",
 "sections": [
  {
   "id": SEC,
   "type": "story",
   "num": 75,
   "title": "№ 75 · Золотая рыбка — Cá vàng",
   "blocks": blocks,
  }
 ],
}

unit_path = os.path.join(HERE, "units", "skazki1-042.json")
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
     "id": UID, "num": 42,
     "title": "Золотая рыбка — Cá vàng",
     "vi": "Золотая рыбка — Cá vàng",
     "ru": "Золотая рыбка",
     "icon": "🐟", "color": "#b45309",
     "file": "units/skazki1-042.json",
     "sectionPrefix": "skazki1-042-s",
     "group": "Truyện № 61–100",
     "sectionCount": 1, "exerciseCount": 0, "grammarCount": 0,
    }
    b["parts"].append(part)
    b["parts"].sort(key=lambda p: p["num"])
    json.dump(b, open(bpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("book.json: added part", UID, "| total parts:", len(b["parts"]))
