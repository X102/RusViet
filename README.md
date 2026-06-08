# 📕 RusViet — Học tiếng Nga trực quan cho người Việt

Website tĩnh (static), **không cần cài đặt, không cần build**. Chỉ cần mở `index.html`
bằng trình duyệt (Chrome / Edge / Firefox / Cốc Cốc) là chạy được ngay.

**Thư viện hiện có 2 cuốn** (chọn ở Trang chủ):
- 📕 **Hình thái học** (Морфология) — 7 chương · 603 bài · ~2.000 từ vựng.
- 📗 **Cú pháp** (Синтаксис) — Раздел 1: Cụm từ (đầy đủ, 13 chương) + Раздел 2: Câu đơn (đang bổ sung, dịch từ bản gốc). Có **nút “Xem đáp án”** đối chiếu (từ Ключ к упражнениям).

Mỗi cuốn có từ điển, flashcard, tìm kiếm và tiến độ học riêng.

## ▶️ Cách mở
1. **Cách nhanh nhất:** nháy đúp vào `index.html`.
2. **Cách khuyên dùng (nếu cần)** — chạy một máy chủ tĩnh nhỏ rồi mở `http://localhost:8000`:
   ```bash
   cd thư-mục-này
   python -m http.server 8000
   ```
   (Hoặc đưa cả thư mục lên GitHub Pages / Netlify để có link chia sẻ.)

## ✨ Tính năng
- 🔊 **Nghe đọc tiếng Nga (TTS):** bấm vào *bất kỳ* từ tiếng Nga để nghe, hoặc bấm 🔊 để đọc cả câu/từ vựng. Chỉnh tốc độ & chọn giọng trong ⚙️ Cài đặt.
- 📚 **Tra từ nhanh:** bấm vào từ Nga → bảng nghĩa hiện ra (nghĩa, giống đực/cái/trung, nút nghe, nút lưu thẻ). Có trang **Từ điển** tra toàn bộ ~2.000 từ.
- 🖍️ **Highlight + ghi chú + lưu:** bôi đen đoạn văn để tô 4 màu; mỗi bài có ô **ghi chú**; đánh dấu **Đã hoàn thành** / **Lưu** ⭐. Tất cả lưu trong trình duyệt và **xuất ra file** được.
- 🃏 **Flashcard (lặp lại ngắt quãng):** ôn từ vựng theo kiểu Leitner, ưu tiên từ chưa thuộc.
- 🙈 **Chế độ tự kiểm tra:** trong mỗi bài tập, ẩn phần nghĩa tiếng Việt để tự dịch rồi bấm hiện đáp án.
- 🔎 **Tìm kiếm** từ vựng, tên bài, và (tuỳ chọn) toàn bộ nội dung.
- 🌙 **Sáng/Tối**, cỡ chữ tuỳ chỉnh, có dấu nhấn (а́), giao diện responsive cho điện thoại.
- 📈 **Tiến độ học** theo từng chương.
- 🎧 **Nghe cả bài (nghe thụ động):** đọc tự động lần lượt cả câu tiếng Nga và bản dịch tiếng Việt, tô sáng dòng đang đọc, có Tạm dừng/Tiếp/Dừng. Cần có giọng tiếng Việt (Edge/Windows) để đọc phần Việt.
- 🔑 **Mỗi bài tập đều có “Đáp án & giải thích”:** nút xem đáp án (đối chiếu Ключ ở sách Cú pháp) và liên kết tới phần lý thuyết liên quan để tự học.

> Dữ liệu cá nhân (tiến độ, highlight, ghi chú) lưu *cục bộ* trong trình duyệt của bạn
> (localStorage). Không gửi đi đâu cả. Dùng ⚙️ → **Xuất tiến độ** để sao lưu.

## 🗂️ Cấu trúc thư mục (thiết kế dạng module)
```
site/
├── index.html              # khung trang
├── css/  theme.css base.css components.css     # giao diện (sáng/tối)
├── js/                     # mỗi tính năng = 1 file, dễ thêm/bớt
│   ├── util.js store.js data.js                # lõi
│   ├── tts.js dictionary.js render.js          # đọc, tra từ, hiển thị
│   ├── highlight.js exercises.js               # tô màu, tự kiểm tra
│   ├── flashcards.js search.js                 # ôn tập, tìm kiếm
│   └── app.js                                  # điều hướng + các trang
├── data/
│   ├── library.json/.js                        # DANH MỤC sách (thêm sách ở đây)
│   └── books/grammar-morphology/
│       ├── book.json/.js                        # mục lục cuốn sách
│       ├── glossary.json/.js                     # từ điển của sách
│       └── units/01-nouns.js … 07-verbs.js      # nội dung từng chương
└── tools/                  # script Python để nhập thêm sách (.docx → dữ liệu web)
```
Mỗi cặp `.json`/`.js` chứa **cùng một nội dung**: bản `.json` để đọc/sửa cho dễ,
bản `.js` là bản trang web thực sự nạp (để chạy được khi mở bằng `file://`).

Xem `HƯỚNG-DẪN-MỞ-RỘNG.md` để biết cách thêm sách mới, truyện song ngữ, video, trò chơi…

## 🔊 Giọng đọc tiếng Nga (quan trọng)
Tính năng nghe đọc dùng **giọng có sẵn của trình duyệt/hệ điều hành** — không tốn phí, không cần API.
Chất lượng phụ thuộc giọng đang có trên máy:
- **Tốt nhất & miễn phí:** mở web bằng **Microsoft Edge** → tự có giọng Nga tự nhiên
  *“Microsoft Svetlana / Dmitry Online (Natural)”*. Web sẽ tự chọn giọng hay nhất.
- **Dùng offline:** **Windows → Cài đặt → Thời gian & ngôn ngữ → Giọng nói → Thêm giọng → Tiếng Nga** (giọng “Irina”).
- Google Chrome cũng có giọng *“Google русский”* khi có mạng.

Vào **⚙️ Cài đặt → Giọng đọc tiếng Nga** để nghe thử, đổi giọng, hoặc bấm **“✨ Giọng Nga tốt nhất”** để app tự chọn.
