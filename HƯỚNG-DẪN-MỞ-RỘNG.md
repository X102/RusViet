# 🧩 Hướng dẫn mở rộng RusViet

Trang web được thiết kế **dạng module** để bạn (hoặc trợ lý AI) dễ dàng thêm nội dung
về sau mà *không phải sửa code lõi*. Dưới đây là các kịch bản thường gặp.

---

## 1) Thêm một cuốn sách ngữ pháp/giáo trình mới (từ file .docx)

Bạn cần Python 3 và thư viện `python-docx` (`pip install python-docx`).

**Bước 1.** Mở `tools/import_docx.py`, sửa 2 dòng đầu:
- `SRC = "đường-dẫn-tới-sach.docx"`
- `OUT = "site/data/books/<id-sách-mới>"`  (ví dụ `tieng-nga-co-ban`)

Script tách sách theo **Heading** của Word:
- *Heading 1/2/3* bắt đầu bằng `PHẦN n:` / `Phần n:` → **một chương**.
- *Heading 3* bắt đầu bằng `BÀI TẬP n` / `Bài n` → **một bài tập**.
- Dòng dạng `слово: nghĩa tiếng Việt` → tự động vào **từ điển**.

**Bước 2.** Chạy:
```bash
python tools/import_docx.py      # tạo book.json, glossary.json, units/*.json
python tools/build_js.py         # tạo bản .js mà web nạp
```

**Bước 3.** Mở `data/library.json` (và `library.js`) thêm 1 mục vào mảng `books`:
```json
{ "id":"tieng-nga-co-ban", "title":"Tên sách", "subtitle":"…",
  "cover":"📗", "level":"A1", "lang":"ru",
  "path":"books/tieng-nga-co-ban/book.json", "type":"grammar" }
```
Xong! Tải lại trang.

> Nếu sách không dùng Heading chuẩn của Word, chỉnh các biểu thức nhận diện
> (`re_part`, `re_ex`, `block_kind`) trong `import_docx.py`. Cấu trúc dữ liệu rất đơn giản
> (xem mục 4) nên bạn cũng có thể tự viết file JSON bằng tay.

---

## 2) Thêm truyện song ngữ Nga–Việt
Tạo một "book" kiểu mới, ví dụ `data/books/truyen-song-ngu/book.json` với các chương là
"câu chuyện", mỗi câu là một block `para`. Vì mọi từ tiếng Nga **tự động** trở thành bấm-được
(nghe + tra từ), truyện sẽ ngay lập tức có tính năng đọc & tra từ. Khai báo trong `library.json`
với `"type":"reader"`.

## 3) Thêm video / postcard / văn hoá
Các thẻ này đang nằm ở mục **“Sắp ra mắt”** (`library.json` → `comingSoon`). Để bật:
- Thêm một trang mới trong `js/app.js` (hàm `viewXxx` + một nhánh trong `route()`).
- Hoặc đơn giản hơn: tạo block kiểu mới trong `js/render.js` (ví dụ `video` → thẻ `<iframe>`,
  `image` → `<img>`), rồi thêm block đó vào dữ liệu chương.

## 4) Cấu trúc dữ liệu một chương (`units/*.json`)
```json
{
  "id":"01-nouns", "num":1, "title":"…", "vi":"Danh từ",
  "ru":"Имя существительное", "icon":"📦", "color":"#6366f1",
  "sections":[
    { "id":"01-s001", "type":"exercise"|"grammar", "num":1, "title":"…",
      "blocks":[
        {"t":"instruction","text":"Yêu cầu: …"},
        {"t":"note","text":"…"}, {"t":"model","text":"…"},
        {"t":"example","text":"…"}, {"t":"subhead","text":"…"},
        {"t":"para","text":"…"},
        {"t":"vocab","ru":"слово","vi":"nghĩa","g":"m"|"f"|"n"|null},
        {"t":"table","rows":[["ô1","ô2"], …]}
      ] }
  ]
}
```
**Quy tắc vàng:** cứ là chữ Cyrillic trong bất kỳ block nào → web tự biến thành
từ bấm-được (nghe + tra). Bạn không cần đánh dấu thủ công.

## 5) Thêm tính năng mới
Mỗi tính năng là một file trong `js/` gắn vào `window.RG`. Thêm `<script>` trong `index.html`
theo đúng thứ tự phụ thuộc, rồi gọi từ `app.js`. Lõi (`util`, `store`, `data`) không cần đụng tới.

---

## 6) ✅ Cập nhật quan trọng: đăng ký sách mới (đa sách)

Web giờ là **thư viện nhiều sách**. Khi thêm một cuốn mới, làm 3 việc:

1. **Tạo dữ liệu** bằng script trong `tools/` (xem `import_docx.py` cho sách dạng "BÀI TẬP n",
   và `import_docx_book2_syntax_example.py` cho sách dạng "Раздел / Упражнение"). Mỗi sách phải có
   **id riêng** (vd `grammar-syntax`) và **id chương/bài không trùng** với sách khác
   (parser tự thêm tiền tố như `gra-01-s001`). Mỗi chương nên có trường `sectionPrefix` để tính tiến độ.
2. **Thêm vào `data/library.json`** (mảng `books`) — và chạy `python tools/build_js.py` (hoặc script
   regen) để sinh lại các file `.js`.
3. **Thêm thẻ `<script>` tĩnh trong `index.html`** cho `book.js`, `glossary.js` và từng `units/*.js`
   của sách mới (đặt cạnh các thẻ data sẵn có). Đây là cách nạp dữ liệu chạy được khi mở bằng `file://`.

Sau đó tải lại trang → cuốn sách mới xuất hiện ở Trang chủ với từ điển/flashcard/tìm kiếm riêng.
