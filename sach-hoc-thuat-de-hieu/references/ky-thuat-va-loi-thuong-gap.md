# Kỹ thuật dựng sách và lỗi thường gặp

## Đường ống (pipeline)

```
*.md (một nguồn duy nhất)
   │  pandoc + scripts/filter.lua
   ├──► sach.tex ──xelatex×2──► sach.pdf
   └──► sach.docx (style từ reference.docx do make_reference_docx.py sinh)
img/*.png  ◄── scripts/diagrams.py (Graphviz + Matplotlib)
```

`filter.lua` chuyển các khối đặc biệt cho từng định dạng:

| Markdown | LaTeX | Word |
|---|---|---|
| `::: {.box kind="kid" title="..."}` | `tcolorbox` màu, có tiêu đề, tự ngắt trang | Đoạn tiêu đề nền màu + đoạn nội dung viền trái, nền nhạt |
| `::: {.part title="..."}` | Trang "Phần" riêng + mục lục cấp Part | Trang riêng, style PartTitle |
| `::: {.appendix}` | `\appendix` → "Phụ lục A, B..." | Chương không số, thêm "Phụ lục A." |
| `# Chương` | Chương mới (book class) | Ngắt trang trước Heading 1 |

## Phông chữ (tiếng Việt)

| Vai trò | PDF (XeLaTeX) | Word |
|---|---|---|
| Thân bài | TeX Gyre Pagella | Cambria |
| Tiêu đề | TeX Gyre Heros | Arial |
| Code | **Liberation Mono** | Consolas |
| Ký hiệu ★ ✗ | DejaVu Sans (qua `newunicodechar`) | — |

Kiểm tra phông mới có đủ dấu: tạo file tex nhỏ chứa `ả ấ ầ Ỏ ố ữ ặ ỹ đ Đ`, chạy xelatex, `grep Missing *.log`.

## Lỗi đã gặp và cách sửa

| Triệu chứng | Nguyên nhân | Cách sửa |
|---|---|---|
| `LaTeX Error: File 'lmodern.sty' not found` | Template pandoc mặc định nạp lmodern | Thêm `-V fontfamily=fontspec` |
| PDF thiếu chữ có dấu trong code (log: `Missing character ... DejaVu Sans Mono`) | DejaVu Sans Mono không có ký tự tiếng Việt dựng sẵn | Dùng `Liberation Mono` (hoặc FreeMono) |
| Ô trống thay cho emoji 🟢📧 | Phông không có emoji | Không dùng emoji; dùng ★ (đã map phông) hoặc chữ `[Email]` |
| Bìa Word ra ký tự `���` | Tiêu đề truyền qua `-M title=...` trên dòng lệnh, locale không phải UTF-8 | Đặt metadata trong file YAML; chạy với `LANG=C.UTF-8` |
| Mục lục Word trống khi mở | Word chưa cập nhật trường TOC | Bình thường: bấm Yes khi Word hỏi, hoặc chuột phải → Update Field. LibreOffice khi render thử cũng hiện trống |
| Trang trắng thừa trước mỗi "Phần" | `\cleardoublepage` | Dùng `\clearpage` trong `\mypart` (đã sửa trong header.tex) |
| Lời mở đầu hiện "Chương 1" hoặc mục "0.1" | Thiếu `{.unnumbered}` | Thêm cho `#` và mọi `##` trong lời mở đầu |
| Sơ đồ chữ quá nhỏ trong PDF | Sơ đồ quá rộng (nhiều khối nối hàng ngang) | `rankdir="TB"` hoặc chia 2 hàng `{{rank=same; ...}}` |
| `SyntaxError: f-string` khi vẽ Graphviz | Ngoặc nhọn Graphviz trong f-string | Viết đôi `{{ }}` |
| Hình không hiện trong PDF | xelatex chạy trong thư mục build không có `img/` | build_book.py tự tạo symlink `build/img` |
| Hình không hiện trong Word | pandoc không tìm thấy | `--resource-path <thư mục sách>` (đã có trong build_book.py) |
| Dòng code dài tràn lề PDF | — | Đã bật `fvextra breaklines`; vẫn nên giữ dòng ≤ 85 ký tự |
| Cảnh báo `The term Table has no translation defined` | pandoc thiếu bản dịch tiếng Việt cho chữ "Table" | Vô hại, bỏ qua |

## Kiểm tra trực quan (bắt buộc)

1. `diagrams.contact_sheet("img", "/tmp/sheet.jpg")` → xem tất cả hình.
2. `check_book.py <sách> --preview build/sach.pdf --pages 1-18` → xem trang.
3. Mở 2–3 trang ở độ phân giải ~70 dpi (`pdftoppm -jpeg -r 70 -f N -l N`) để soi chữ có dấu, hộp màu, code.
4. Word: chuyển sang PDF bằng LibreOffice (`soffice --headless --convert-to pdf`) rồi xem trang bìa + một trang có hộp màu và code.

## Giao file cho người dùng

- Đặt tên file không dấu, dùng gạch dưới: `Ten_Sach.pdf`, `Ten_Sach.docx`, `Ten_Sach.tex`.
- File `.tex` cần thư mục `img/` để dịch lại → gửi kèm `Ten_Sach_LaTeX_kem_hinh.zip` (gồm .tex + img/).
- Nhắc người dùng: dịch lại bằng `xelatex` **hai lần**; cần các phông TeX Gyre Pagella, TeX Gyre Heros, Liberation Mono, DejaVu Sans.
