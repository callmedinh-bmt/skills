---
name: sach-hoc-thuat-de-hieu
description: Tạo sách / tài liệu học thuật tiếng Việt chi tiết, giải thích cực kỳ dễ hiểu bằng ví dụ đời thường, có hình minh hoạ tự vẽ, hộp màu (giải thích nhanh, góc AI, cẩn thận, bài tập), code mẫu, bài tập 3 mức và phụ lục đáp án — xuất đồng thời LaTeX (.tex), PDF và Word (.docx) cùng phong cách. Dùng skill này bất cứ khi nào người dùng muốn "tạo sách", "giáo trình", "tài liệu học", "tài liệu học thuật", "ebook", "cẩm nang", "khoá học dạng tài liệu" về một chủ đề (lập trình, thiết kế hệ thống, AI, kinh tế, khoa học...), muốn "giải thích dễ hiểu", "có ví dụ và bài tập", hoặc yêu cầu xuất ra LaTeX + PDF + DOCX — kể cả khi họ không nhắc tên skill.
---

# Sách học thuật dễ hiểu (LaTeX + PDF + DOCX)

Skill này tạo một cuốn sách hoàn chỉnh từ **một nguồn Markdown duy nhất**, rồi dựng ra ba định dạng giống nhau về nội dung và phong cách:

- **PDF** dàn trang kiểu sách (XeLaTeX): bìa màu, mục lục, trang "Phần", tiêu đề chương có số, hộp màu tự ngắt trang, code tô màu, hình có chú thích đánh số.
- **DOCX** với style riêng: tiêu đề màu, hộp màu bằng viền + nền đoạn, bảng có viền, code nền xám.
- **TEX** để người dùng tự chỉnh và dịch lại.

## Các file trong skill

| File | Dùng khi |
|---|---|
| `references/quy-tac-noi-dung.md` | **Đọc trước khi viết.** Giọng văn, cấu trúc sách/chương, hộp màu, code, hình, bài tập |
| `references/ky-thuat-va-loi-thuong-gap.md` | Khi dựng file hoặc gặp lỗi (phông, mã hoá, hình, trang trắng...) |
| `assets/chapter_template.md` | Khung một chương — sao chép rồi điền |
| `assets/book.yaml`, `assets/chapters.txt` | Mẫu cấu hình bìa và thứ tự chương |
| `assets/vi-du-sach-mau/` | Một cuốn sách mẫu hoàn chỉnh nhỏ (đã kiểm tra dựng thành công) — xem để biết cú pháp thật |
| `assets/header.tex`, `assets/titlepage.tex` | Phong cách PDF (không cần sửa) |
| `scripts/diagrams.py` | Vẽ hình minh hoạ đồng bộ màu (Graphviz/Matplotlib) |
| `scripts/build_book.py` | Dựng .tex + .pdf + .docx trong một lệnh |
| `scripts/check_book.py` | Kiểm tra bản thảo + ảnh xem trước trang PDF |
| `scripts/filter.lua`, `scripts/make_reference_docx.py` | Được build_book.py gọi tự động |

## Quy trình

### Bước 1 — Làm rõ yêu cầu (hỏi gọn, tối đa 1–3 câu)

Nếu người dùng chưa nói, hỏi: **chủ đề và phạm vi**, **trình độ người đọc**, **ngôn ngữ code** (nếu có code). Còn lại tự quyết định hợp lý.

Ghi nhớ: "giải thích như cho trẻ 10 tuổi" là **cách viết** (đơn giản, ví dụ đời thường), **không** phải đối tượng đọc. Không được viết "cho bé", "10 tuổi", "bạn nhỏ" trong sách; xưng "bạn".

### Bước 2 — Lập dàn ý trước khi viết

- Chia thành các **Phần** (nền tảng → nâng cao → ứng dụng/thực hành), mỗi phần 2–6 chương.
- Ghi số chương cố định ngay từ đầu (lời mở đầu không đánh số) để tham chiếu "xem chương X" và số bài tập "X.1" luôn đúng.
- Liệt kê hình minh hoạ dự kiến cho từng chương.

### Bước 3 — Viết nội dung

Tạo thư mục sách (ví dụ `/home/claude/book/`) gồm `book.yaml`, `chapters.txt`, các file `.md`, thư mục `img/`.

Theo `references/quy-tac-noi-dung.md` và `assets/chapter_template.md`. Tóm tắt:

- Mỗi khái niệm: **Vấn đề → Ví dụ đời thường → Giải pháp + hình → Code ngắn → Khi nào dùng/không dùng**.
- 2–5 hộp màu mỗi chương; cuối chương có bảng tóm tắt (nếu hợp) và **hộp Bài tập** 3 mức ★/★★/★★★.
- Có thể chia nhiều chương mỗi file `.md`. Phụ lục bắt đầu bằng `::: {.appendix}` + `:::`.
- Sách dài: viết lần lượt từng file, không cố viết một lần.

### Bước 4 — Vẽ hình minh hoạ

```python
import sys; sys.path.insert(0, "<skill>/scripts")
from diagrams import dot, cluster, B, G, O, P, R, Y, GR, contact_sheet
dot("img/vong_lap.png", f'''
  a [label="Suy nghĩ", {P}];  b [label="Hành động", {B}];  c [label="Quan sát", {G}];
  a -> b -> c -> a;
''', rankdir="TB")
contact_sheet("img", "/tmp/sheet.jpg")   # rồi XEM ảnh này
```

Sơ đồ nào chữ bé (quá rộng) → đổi `rankdir="TB"` hoặc chia hàng. Không dùng emoji.

### Bước 5 — Kiểm tra bản thảo

```bash
python3 <skill>/scripts/check_book.py <thư_mục_sách> --lang java --forbid "10 tuổi" "cho bé" "bạn nhỏ"
```

Sửa hết các vấn đề được báo (hình thiếu, emoji, cụm từ cấm, code sai ngôn ngữ, tên snake_case trong văn bản khi dùng Java, chương thiếu hình/bài tập).

### Bước 6 — Dựng file

```bash
python3 <skill>/scripts/build_book.py <thư_mục_sách> --name Ten_Sach_Khong_Dau
```

Kết quả nằm trong `<thư_mục_sách>/build/`. Script in số lỗi LaTeX và số ký tự thiếu phông — **cả hai phải bằng 0**.

### Bước 7 — Xem bằng mắt (bắt buộc)

```bash
python3 <skill>/scripts/check_book.py <thư_mục_sách> --preview <thư_mục_sách>/build/Ten_Sach.pdf --pages 1-18
```

Xem ảnh `build/preview/pages.jpg`, rồi phóng to 2–3 trang (code, bảng, hộp màu). Với DOCX: chuyển sang PDF bằng LibreOffice và xem trang bìa + một trang nội dung. Chi tiết và cách sửa lỗi: `references/ky-thuat-va-loi-thuong-gap.md`.

### Bước 8 — Giao file

Sao chép vào `/mnt/user-data/outputs/`: `.pdf`, `.docx`, `.tex`, và **zip gồm .tex + img/** (vì .tex cần hình để dịch lại). Gọi `present_files`. Nhắn ngắn gọn: cấu trúc sách, số trang, lưu ý cập nhật mục lục trong Word (bấm Yes khi Word hỏi), dịch lại LaTeX bằng xelatex hai lần.

## Khi người dùng yêu cầu sửa

- **Sửa nội dung/giọng văn**: sửa file `.md`, chạy lại Bước 5–8. Dùng `--forbid` để chắc chắn cụm từ cũ đã hết.
- **Đổi ngôn ngữ code**: viết lại từng khối code; cập nhật **cả** văn bản quanh code, tên hàm trong bài tập, đáp án, và chữ trong hình. Chạy thử các đoạn tự chứa. Kiểm tra bằng `--lang`.
- **Đổi màu/phông**: màu ở đầu `assets/header.tex` (cblue, cpurple, corange, cgreen, cdark) và `BOXES` trong `make_reference_docx.py`; phông xem bảng phông trong file tham khảo kỹ thuật (phải có đủ dấu tiếng Việt).
