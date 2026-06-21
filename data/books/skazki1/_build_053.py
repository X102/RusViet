# -*- coding: utf-8 -*-
"""Build unit skazki1-053 «Ведьма и Солнцева сестра» (№93) + glossary + book.json part."""
import json, os

BOOK = "/sessions/relaxed-sleepy-gauss/mnt/code/claudecode/RusViet_website/data/books/skazki1"
UID = "skazki1-053"
SID = "skazki1-053-s001"

note = ("«Mụ phù thủy và Em Gái Mặt Trời» (số 93) là một truyện cổ tích thần kỳ Nga kinh điển, "
        "mang mô-típ «chạy trốn kẻ săn đuổi»: hoàng tử Ivan câm được người giữ ngựa báo trước rằng "
        "đứa em gái sắp chào đời sẽ là phù thủy ăn thịt cả vương quốc, nên cậu bỏ trốn. Trên đường, cậu gặp "
        "những nhân vật nhân cách hóa sức mạnh thiên nhiên — thần Nhổ-Sồi (Вертодуб) và thần Dời-Núi (Вертогор) — "
        "cùng hai bà thợ khâu già mà mạng sống gắn với những vật mau tàn; về sau họ đền ơn cậu bằng cách dựng núi, "
        "rừng và mặt hồ chặn đường mụ phù thủy. Cuối cùng cậu được Em Gái Mặt Trời — hiện thân của ánh sáng và sự sống — "
        "che chở, nâng hẳn lên trời, đối lập với mụ em gái «rắn độc» của bóng tối và cái chết.")

# (Russian sentence, Vietnamese translation)
pairs = [
 ("В некотором царстве, далеком государстве, жил-был царь с царицей, у них был сын Иван-царевич, с роду немой.",
  "Ngày xưa, ở một vương quốc nọ, tại một đất nước xa xôi, có một nhà vua sống cùng hoàng hậu; hai người sinh được một hoàng tử tên là Ivan, từ thuở lọt lòng đã câm chẳng nói được."),
 ("Было ему лет двенадцать, и пошел он раз в конюшню к любимому своему конюху.",
  "Hoàng tử lên chừng mười hai tuổi, một hôm cậu ra tàu ngựa tìm bác giữ ngựa mà cậu yêu quý."),
 ("Конюх этот сказывал ему завсегда сказки, и теперь Иван-царевич пришел послушать от него сказочки, да не то услышал.",
  "Bác giữ ngựa này xưa nay vẫn thường kể chuyện cổ tích cho cậu nghe, lần này hoàng tử Ivan cũng đến để nghe vài câu chuyện, nào ngờ lại nghe phải điều khác hẳn."),
 ("«Иван-царевич! — сказал конюх. — У твоей матери скоро родится дочь, а тебе сестра; будет она страшная ведьма, съест и отца, и мать, и всех подначальных людей; так ступай, попроси у отца что ни есть наилучшего коня — будто покататься, и поезжай отсюдова куда глаза глядят, коли хочешь от беды избавиться».",
  "«Hoàng tử Ivan ơi! — bác giữ ngựa nói. — Chẳng bao lâu nữa mẹ cậu sẽ sinh một đứa con gái, tức là em gái cậu; nó sẽ là một mụ phù thủy ghê gớm, ăn thịt cả vua cha, cả hoàng hậu, lẫn mọi bề tôi dưới trướng; vậy cậu hãy đến xin vua cha một con tuấn mã tốt nhất — làm như để đi dạo chơi — rồi phóng khỏi đây, đi đâu thì đi, nếu muốn thoát khỏi tai họa.»"),
 ("Иван-царевич прибежал к отцу и с роду впервой заговорил с ним; царь так этому возрадовался, что не стал и спрашивать: зачем ему добрый конь надобен?",
  "Hoàng tử Ivan chạy đến chỗ vua cha, lần đầu tiên trong đời mở miệng nói chuyện với người; nhà vua mừng rỡ đến mức chẳng buồn hỏi xem cậu cần con ngựa tốt để làm gì."),
 ("Тотчас приказал что ни есть наилучшего коня из своих табунов оседлать для царевича.",
  "Vua liền truyền đóng yên cương con ngựa tốt nhất trong các đàn ngựa của mình cho hoàng tử."),
 ("Иван-царевич сел и поехал куда глаза глядят.",
  "Hoàng tử Ivan lên ngựa, cứ nhằm nơi nào mắt trông thấy mà đi."),

 ("Долго-долго он ехал; наезжает на двух старых швей и просит, чтоб они взяли его с собой жить.",
  "Cậu đi mãi, đi mãi; rồi gặp hai bà thợ khâu già, bèn xin hai bà cho ở lại sống cùng."),
 ("Старухи сказали: «Мы бы рады тебя взять, Иван-царевич, да нам уж немного жить. Вот доломаем сундук иголок да изошьем сундук ниток — тотчас и смерть придет!»",
  "Hai bà lão đáp: «Chúng ta cũng muốn nhận cậu lắm, hoàng tử Ivan ạ, nhưng chúng ta chẳng còn sống được bao lâu nữa. Hễ dùng gãy hết cả hòm kim này và khâu hết cả hòm chỉ kia — thì ngay lúc ấy cái chết sẽ đến!»"),
 ("Иван-царевич заплакал и поехал дальше.",
  "Hoàng tử Ivan òa khóc rồi lại lên đường đi tiếp."),
 ("Долго-долго ехал, подъезжает к Вертодубу и просит: «Прими меня к себе!» — «Рад бы тебя принять, Иван-царевич, да мне жить остается немного. Вот как повыдерну все эти дубы с кореньями — тотчас и смерть моя!»",
  "Cậu đi mãi, đi mãi, rồi đến chỗ thần Nhổ-Sồi mà xin: «Hãy cho tôi nương nhờ với!» — «Ta cũng muốn nhận cậu lắm, hoàng tử Ivan ạ, nhưng ta chẳng còn sống được mấy nữa. Hễ ta nhổ bật hết những cây sồi này cả gốc lẫn rễ — thì ngay lúc ấy ta sẽ chết!»"),
 ("Пуще прежнего заплакал царевич и поехал все дальше да дальше.",
  "Hoàng tử càng khóc dữ hơn trước, rồi cứ thế đi mãi, đi mãi."),
 ("Подъезжает к Вертогору; стал его просить, а он в ответ: «Рад бы принять тебя, Иван-царевич, да мне самому жить немного. Видишь, поставлен я горы ворочать; как справлюсь с этими последними — тут и смерть моя!»",
  "Cậu đến chỗ thần Dời-Núi, ngỏ lời xin nương nhờ, thần đáp lại: «Ta cũng muốn nhận cậu lắm, hoàng tử Ivan ạ, nhưng chính ta cũng chẳng còn sống được bao lâu. Cậu thấy đấy, ta được giao việc dời chuyển những ngọn núi này; hễ ta làm xong mấy ngọn cuối cùng — thì ngay đó là lúc ta chết!»"),
 ("Залился Иван-царевич горькими слезами и поехал еще дальше.",
  "Hoàng tử Ivan đầm đìa nước mắt cay đắng, rồi lại đi xa hơn nữa."),

 ("Долго-долго ехал; приезжает, наконец, к Солнцевой сестрице.",
  "Cậu đi mãi, đi mãi; rồi cuối cùng cũng đến nhà bà Em Gái Mặt Trời."),
 ("Она его приняла к себе, кормила-поила, как за родным сыном ходила.",
  "Bà đón cậu vào nhà, cho ăn cho uống, chăm nom cậu như con đẻ của mình."),
 ("Хорошо было жить царевичу, а все нет-нет, да и сгрустнется: захочется узнать, что в родном дому деется?",
  "Hoàng tử sống ở đó cũng sung sướng, vậy mà thỉnh thoảng lòng vẫn chợt buồn: cậu muốn biết ở quê nhà đang xảy ra chuyện gì."),
 ("Взойдет, бывало, на высокую гору, посмотрит на свой дворец и видит, что все съедено, только стены осталися!",
  "Đôi khi cậu trèo lên một ngọn núi cao, nhìn về cung điện của mình thì thấy tất cả đã bị ăn sạch, chỉ còn trơ lại mấy bức tường!"),
 ("Вздохнет и заплачет.",
  "Cậu thở dài rồi bật khóc."),
 ("Раз этак посмотрел да поплакал — воротился, а Солнцева сестра спрашивает: «Отчего ты, Иван-царевич, нонче заплаканный?»",
  "Một lần ngắm như thế rồi khóc xong, cậu trở về, bà Em Gái Mặt Trời hỏi: «Cớ sao hôm nay mắt cậu đỏ hoe vậy, hoàng tử Ivan?»"),
 ("Он говорит: «Ветром в глаза надуло».",
  "Cậu đáp: «Gió thổi tạt vào mắt cháu đấy ạ.»"),
 ("В другой раз опять то же; Солнцева сестра взяла да и запретила ветру дуть.",
  "Lần khác lại vẫn thế; bà Em Gái Mặt Trời bèn ra lệnh cấm gió không được thổi nữa."),
 ("И в третий раз воротился Иван-царевич заплаканный; да уж делать нечего — пришлось во всем признаваться, и стал он просить Солнцеву сестрицу, чтоб отпустила его, добра мо́лодца, на родину понаведаться.",
  "Đến lần thứ ba hoàng tử Ivan trở về mắt vẫn còn ngấn lệ; chẳng còn cách nào khác — cậu đành thú thật mọi chuyện, rồi xin bà Em Gái Mặt Trời cho mình, một chàng trai trẻ, được về thăm quê nhà một chuyến."),
 ("Она его не пускает, а он ее упрашивает; наконец упросил-таки, отпустила его на родину понаведаться и дала ему на дорогу щетку, гребенку да два моложавых яблочка; какой бы ни был стар человек, а съест яблочко — вмиг помолодеет!",
  "Bà không cho đi, cậu cứ một mực nài nỉ; cuối cùng cũng năn nỉ được, bà cho cậu về thăm quê và đưa cho cậu mang theo đường một cái bàn chải, một cái lược cùng hai quả táo hồi xuân; người dù già đến đâu, hễ ăn một quả táo ấy — là tức thì trẻ lại!"),

 ("Приехал Иван-царевич к Вертогору, всего одна гора осталась; он взял свою щетку и бросил во чисто́ поле: откуда ни взялись — вдруг выросли из земли высокие-высокие горы, верхушками в небо упираются; и сколько тут их — видимо-невидимо!",
  "Hoàng tử Ivan đến chỗ thần Dời-Núi, chỉ còn vẻn vẹn một ngọn núi nữa; cậu lấy cái bàn chải của mình ném ra giữa cánh đồng quang: chẳng biết từ đâu ra — bỗng từ dưới đất mọc lên những ngọn núi cao ngất, đỉnh chạm tới tận trời; nhiều vô số kể, nhìn không xuể!"),
 ("Вертогор обрадовался и весело принялся за работу.",
  "Thần Dời-Núi mừng rỡ, hớn hở bắt tay vào việc."),
 ("Долго ли, коротко ли — приехал Иван-царевич к Вертодубу, всего три дуба осталося; он взял гребенку и кинул во чисто́ поле: откуда что́ — вдруг зашумели, поднялись из земли густые дубовые леса, дерево дерева толще!",
  "Đi lâu hay chóng chẳng rõ — hoàng tử Ivan đến chỗ thần Nhổ-Sồi, chỉ còn vẻn vẹn ba cây sồi; cậu lấy cái lược ném ra giữa cánh đồng quang: chẳng biết từ đâu — bỗng rì rào dậy lên, từ dưới đất trồi lên những cánh rừng sồi rậm rạp, cây nọ to hơn cây kia!"),
 ("Вертодуб обрадовался, благодарствовал царевичу и пошел столетние дубы выворачивать.",
  "Thần Nhổ-Sồi mừng rỡ, cảm tạ hoàng tử rồi đi nhổ những cây sồi trăm tuổi."),
 ("Долго ли, коротко ли — приехал Иван-царевич к старухам, дал им по яблочку; они съели, вмиг помолодели и подарили ему хусточку: как махнешь хусточкой — станет позади целое озеро!",
  "Đi lâu hay chóng chẳng rõ — hoàng tử Ivan đến chỗ hai bà lão, biếu mỗi bà một quả táo; hai bà ăn vào, tức thì trẻ lại, rồi tặng cậu một chiếc khăn tay: hễ vung chiếc khăn lên — là phía sau hiện ra cả một mặt hồ!"),

 ("Приезжает Иван-царевич домой.",
  "Hoàng tử Ivan về tới nhà."),
 ("Сестра выбежала, встретила его, приголубила: «Сядь, — говорит, — братец, поиграй на гуслях, а я пойду — обед приготовлю».",
  "Cô em gái chạy ra đón, vuốt ve mơn trớn anh: «Anh ngồi xuống đi, — cô bảo, — gảy đàn gusli chơi đi anh, còn em thì đi sửa soạn bữa cơm.»"),
 ("Царевич сел и бренчит на гуслях; выполз из норы мышонок и говорит ему человеческим голосом: «Спасайся, царевич, беги скорее! Твоя сестра ушла зубы точить».",
  "Hoàng tử ngồi xuống gảy tưng tưng cây đàn gusli; từ trong hang một chú chuột nhắt bò ra, cất tiếng người mà bảo cậu: «Chạy đi, hoàng tử ơi, mau chạy trốn đi! Em gái cậu đã đi mài răng rồi đấy.»"),
 ("Иван-царевич вышел из горницы, сел на коня и поскакал назад; а мышонок по струнам бегает гусли бренчат, а сестра и не ведает, что братец ушел.",
  "Hoàng tử Ivan ra khỏi gian phòng, lên ngựa phi ngược trở lại; còn chú chuột nhắt cứ chạy trên các sợi dây đàn nên gusli vẫn tưng tưng vang, do đó cô em chẳng hề hay biết anh mình đã đi mất."),
 ("Наточила зубы, бросилась в горницу, глядь — нет ни души, только мышонок в нору скользнул.",
  "Mài răng xong, mụ lao vào gian phòng, nhìn quanh — chẳng còn một bóng người, chỉ có chú chuột nhắt vừa lẩn tọt vào hang."),
 ("Разозлилась ведьма, так и скрипит зубами, и пустилась в погоню.",
  "Mụ phù thủy nổi cơn thịnh nộ, nghiến răng ken két, rồi lao đi đuổi theo."),

 ("Иван-царевич услыхал шум, оглянулся — вот-вот нагонит сестра; махнул хусточкой — и стало глубокое озеро.",
  "Hoàng tử Ivan nghe tiếng động ầm ầm, ngoảnh lại — em gái sắp đuổi kịp đến nơi; cậu vung chiếc khăn tay lên — thế là hiện ra một mặt hồ sâu thẳm."),
 ("Пока ведьма переплыла озеро, Иван-царевич далеко уехал.",
  "Trong lúc mụ phù thủy bơi qua hồ, hoàng tử Ivan đã chạy được xa."),
 ("Понеслась она еще быстрее... вот уж близко!",
  "Mụ lại lao đi nhanh hơn nữa... kìa đã gần lắm rồi!"),
 ("Вертодуб угадал, что царевич от сестры спасается, и давай вырывать дубы да валить на дорогу; целую гору накидал!",
  "Thần Nhổ-Sồi đoán ra hoàng tử đang chạy trốn em gái, liền ra sức nhổ những cây sồi quật ngả chắn ngang đường; chất thành cả một ngọn núi!"),
 ("Нет ведьме проходу!",
  "Mụ phù thủy hết đường mà qua!"),
 ("Стала она путь прочищать, грызла-грызла, насилу продралась, а Иван-царевич уж далеко.",
  "Mụ bèn dọn lối, gặm mãi, gặm mãi, mãi mới len qua được, mà hoàng tử Ivan thì đã đi xa."),
 ("Бросилась догонять, гнала-гнала, еще немножко... и уйти нельзя!",
  "Mụ lại lao theo, đuổi mãi, đuổi mãi, chỉ chút nữa thôi... là cậu không thoát được!"),
 ("Вертогор увидал ведьму, ухватился за самую высокую гору и повернул ее как раз на дорогу, а на ту гору поставил другую.",
  "Thần Dời-Núi trông thấy mụ phù thủy, bèn ôm lấy ngọn núi cao nhất xoay đặt chắn ngay giữa đường, rồi chồng thêm một ngọn núi khác lên trên ngọn ấy."),
 ("Пока ведьма карабкалась да лезла, Иван-царевич ехал да ехал и далеко очутился.",
  "Trong lúc mụ phù thủy bám víu trèo leo, hoàng tử Ivan cứ đi mãi, đi mãi, đến được nơi thật xa."),

 ("Перебралась ведьма через горы и опять погнала за братом...",
  "Mụ phù thủy vượt được qua núi rồi lại lao đi đuổi theo anh trai..."),
 ("Завидела его и говорит: «Теперь не уйдешь от меня!»",
  "Vừa trông thấy cậu, mụ nói: «Lần này thì mày đừng hòng thoát khỏi tay tao!»"),
 ("Вот близко, вот нагонит!",
  "Kìa đã gần, kìa sắp đuổi kịp đến nơi!"),
 ("В то самое время подскакал Иван-царевич к теремам Солнцевой сестрицы и закричал: «Солнце, Солнце! Отвори оконце».",
  "Vừa đúng lúc ấy, hoàng tử Ivan phi ngựa tới tòa lầu của bà Em Gái Mặt Trời mà kêu lớn: «Mặt Trời ơi, Mặt Trời! Hãy mở cửa sổ cho tôi!»"),
 ("Солнцева сестрица отворила окно, и царевич вскочил в него вместе с конем.",
  "Bà Em Gái Mặt Trời mở cửa sổ, hoàng tử cùng cả con ngựa nhảy vọt qua đó vào trong."),
 ("Ведьма стала просить, чтоб ей выдали брата головою; Солнцева сестра ее не послушала и не выдала.",
  "Mụ phù thủy đòi phải nộp đầu anh trai cho mụ trị tội; bà Em Gái Mặt Trời chẳng nghe lời mụ, nhất quyết không giao."),
 ("Тогда говорит ведьма: «Пусть Иван-царевич идет со мной на весы, кто кого перевесит! Если я перевешу — так я его съем, а если он перевесит — пусть меня убьет!»",
  "Mụ phù thủy bèn nói: «Vậy thì để hoàng tử Ivan cùng tôi lên bàn cân, xem ai nặng hơn ai! Nếu tôi nặng hơn — thì tôi sẽ ăn thịt cậu ta, còn nếu cậu ta nặng hơn — thì cứ để cậu ta giết tôi!»"),
 ("Пошли; сперва сел на весы Иван-царевич, а потом и ведьма полезла: только ступила ногой, как Ивана-царевича вверх и подбросило, да с такою силою, что он прямо попал на небо, к Солнцевой сестре в терема; а ведьма-змея осталась на земле.",
  "Họ cùng đi; trước hết hoàng tử Ivan ngồi lên một bên cân, rồi mụ phù thủy mới trèo lên: vừa đặt chân lên thì hoàng tử Ivan bị hất bổng lên cao, mạnh đến nỗi cậu bay thẳng lên trời, vào tòa lầu của bà Em Gái Mặt Trời; còn mụ phù thủy rắn độc thì ở lại dưới mặt đất."),
]

vocab = [
 ("немой", "câm, không nói được (от рождения немой = câm bẩm sinh)"),
 ("конюх", "người giữ ngựa, mã phu (kẻ trông coi tàu ngựa)"),
 ("завсегда", "từ cổ / khẩu ngữ = всегда — luôn luôn, xưa nay vẫn thế"),
 ("подначальные люди", "những kẻ dưới quyền, bề tôi dưới trướng (подначальный = thuộc quyền cai quản)"),
 ("Вертодуб и Вертогор", "tên hai nhân vật thần thoại nhân cách hóa sức mạnh thiên nhiên: Вертодуб «kẻ nhổ/vặn cây sồi» (вертеть + дуб), Вертогор «kẻ dời/xoay núi» (вертеть + гора)"),
 ("ворочать", "xoay chuyển, dời, lật (vật nặng); горы ворочать = dời non lấp bể"),
 ("моложавый", "vốn nghĩa «trông trẻ hơn tuổi»; ở đây моложавые яблочки = táo hồi xuân, ăn vào thì trẻ lại"),
 ("хусточка", "phương ngữ (gốc Nam Nga / Ukraina) = платочек — chiếc khăn tay nhỏ"),
 ("видимо-невидимо", "thành ngữ: nhiều vô số kể, nhiều không sao đếm xuể"),
 ("гусли", "đàn gusli — nhạc cụ dây cổ truyền của người Nga, gảy bằng ngón tay"),
 ("бренчать", "gảy tưng tưng, khảy lạch cạch (chơi đàn một cách lơ đãng, vu vơ)"),
 ("горница", "gian phòng trên / phòng sạch, phòng khách trong nhà gỗ Nga"),
 ("приголубить", "vuốt ve, âu yếm, vỗ về (ở đây là cử chỉ giả lả của mụ phù thủy)"),
 ("выдать головою", "thành ngữ cổ: nộp ai đó để mặc cho trừng phạt / giết, giao nộp hoàn toàn"),
 ("перевесить", "nặng cân hơn, làm nghiêng cán cân về phía mình"),
]

blocks = [{"t": "note", "text": note}]
for ru, vi in pairs:
    blocks.append({"t": "para", "text": "%s (%s)" % (ru, vi)})
blocks.append({"t": "subhead", "text": "Từ khó trong truyện"})
for ru, vi in vocab:
    blocks.append({"t": "vocab", "ru": ru, "vi": vi, "g": None})

unit = {
 "id": UID,
 "num": 53,
 "title": "Ведьма и Солнцева сестра — Mụ phù thủy và Em Gái Mặt Trời",
 "vi": "Ведьма и Солнцева сестра — Mụ phù thủy và Em Gái Mặt Trời",
 "ru": "Ведьма и Солнцева сестра",
 "icon": "🧙‍♀️",
 "color": "#7e22ce",
 "sectionPrefix": "skazki1-053-s",
 "group": "Truyện № 61–100",
 "sections": [
  {
   "id": SID,
   "type": "story",
   "num": 93,
   "title": "№ 93 · Ведьма и Солнцева сестра — Mụ phù thủy và Em Gái Mặt Trời",
   "blocks": blocks,
  }
 ],
}

# write unit
upath = os.path.join(BOOK, "units", UID + ".json")
with open(upath, "w", encoding="utf-8") as f:
    json.dump(unit, f, ensure_ascii=False, indent=1)
print("wrote", upath, "para count =", len(pairs), "vocab =", len(vocab))

# glossary
gpath = os.path.join(BOOK, "glossary.json")
g = json.load(open(gpath, encoding="utf-8"))
have = {e["ru"].lower() for e in g["entries"]}
added = 0
for ru, vi in vocab:
    if ru.lower() in have:
        print("  skip (dup):", ru); continue
    g["entries"].append({"ru": ru, "ruPlain": ru, "vi": vi, "g": None, "ref": SID})
    have.add(ru.lower()); added += 1
g["count"] = len(g["entries"])
with open(gpath, "w", encoding="utf-8") as f:
    json.dump(g, f, ensure_ascii=False, indent=1)
print("glossary now", g["count"], "(+%d)" % added)

# book.json part
bpath = os.path.join(BOOK, "book.json")
b = json.load(open(bpath, encoding="utf-8"))
if any(p["id"] == UID for p in b["parts"]):
    print("part already exists, skipping add")
else:
    b["parts"].append({
        "id": UID,
        "num": 53,
        "title": "Ведьма и Солнцева сестра — Mụ phù thủy và Em Gái Mặt Trời",
        "vi": "Ведьма и Солнцева сестра — Mụ phù thủy và Em Gái Mặt Trời",
        "ru": "Ведьма и Солнцева сестра",
        "icon": "🧙‍♀️",
        "color": "#7e22ce",
        "file": "units/skazki1-053.json",
        "sectionPrefix": "skazki1-053-s",
        "group": "Truyện № 61–100",
        "sectionCount": 1,
        "exerciseCount": 0,
        "grammarCount": 0,
    })
    with open(bpath, "w", encoding="utf-8") as f:
        json.dump(b, f, ensure_ascii=False, indent=1)
    print("added part skazki1-053; total parts =", len(b["parts"]))
