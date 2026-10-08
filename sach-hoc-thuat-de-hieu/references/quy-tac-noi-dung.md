# Quy tắc viết nội dung

Đọc file này trước khi viết bất kỳ chương nào.

## Mục lục
1. Giọng văn
2. Cấu trúc một cuốn sách
3. Cấu trúc một chương
4. Bốn loại hộp màu
5. Code
6. Hình minh hoạ
7. Bảng
8. Bài tập và đáp án
9. Những lỗi đã gặp về nội dung

---

## 1. Giọng văn

Mục tiêu: **giải thích dễ hiểu như cho một người hoàn toàn mới**, nhưng người đọc là **người lớn**.

- **Xưng "bạn"**. Không xưng "con", "em", "bé"; không viết "cho bé 10 tuổi", "bạn nhỏ", "như học sinh lớp 5" ở bất kỳ đâu trong sách (kể cả tiêu đề hộp, bìa, prompt mẫu). "Dễ hiểu như cho trẻ 10 tuổi" là **cách viết**, không phải **đối tượng đọc**.
- Ví dụ đời thường lấy từ **đời sống người lớn**: quán ăn, siêu thị, ngân hàng, giao hàng, văn phòng, thư ký, lễ tân, đi chợ, đặt xe. Tránh "mẹ dặn", "cô giáo", "đồ chơi", "tiền tiêu vặt".
- **Thuật ngữ chỉ dùng khi thật sự cần.** Lần đầu xuất hiện: viết tiếng Việt trước, thuật ngữ gốc trong ngoặc, giải thích ngay. Ví dụ: "**bộ nhớ đệm** (cache) — chỗ để đồ hay dùng ở gần cho nhanh".
- Câu ngắn. Mỗi đoạn một ý. Đoạn dài nhất ~5 câu.
- Đặt cho mỗi khái niệm một **"biệt danh dễ nhớ"** trong tiêu đề mục: `Adapter — "Cục chuyển đổi"`, `Cache — "Để đồ hay dùng ở gần"`.
- Luôn nói **vì sao** trước **làm thế nào**: Vấn đề → Ví dụ đời thường → Giải pháp.
- Nói rõ **đánh đổi** (được gì, mất gì) và **khi nào KHÔNG nên dùng**.
- Không cường điệu. Không hứa hẹn. Con số ước lượng thì ghi rõ "ước lượng", "xấp xỉ".
- Thông tin dễ lỗi thời (giá, tên sản phẩm, phiên bản) → viết dưới dạng nguyên tắc, kèm một câu nhắc người đọc kiểm tra lại.

## 2. Cấu trúc một cuốn sách

1. **Trang bìa** (tự sinh từ `book.yaml`).
2. **Mục lục** (tự sinh).
3. **Lời mở đầu** — chương không đánh số: `# Lời mở đầu {.unnumbered}` và **mọi mục `##` bên trong cũng phải thêm `{.unnumbered}`** (nếu không sẽ hiện "0.1", "0.2"). Gồm: sách dành cho ai, mỗi chương có gì, giải thích 4 hộp màu, cách học hiệu quả (nếu chủ đề liên quan AI: cách học cùng AI).
4. **Các Phần** (`::: {.part title="Phần I — ..."}` + `:::`), mỗi phần 2–6 chương, đi từ nền tảng → nâng cao → thực hành.
5. **Chương thực hành / tổng hợp** cuối mỗi phần lớn: ráp kiến thức thành bài toán thật, cho người đọc tự làm trước rồi mới xem lời giải.
6. **Phụ lục** — mở đầu bằng `::: {.appendix}` + `:::` (đánh số A, B, C): gợi ý đáp án, bảng thuật ngữ (thuật ngữ → nghĩa dễ hiểu), tài liệu đọc thêm.

## 3. Cấu trúc một chương

Xem `assets/chapter_template.md`. Nhịp chuẩn cho mỗi khái niệm:

1. **Câu chuyện đời thường** (hoặc hộp "Hiểu nhanh").
2. **Vấn đề**: nếu không có cách này thì sao?
3. **Giải pháp**: ý tưởng chính 1–2 câu + **hình minh hoạ**.
4. **Ví dụ code** ngắn.
5. **Khi nào dùng / khi nào không**.
6. **Hộp "Cẩn thận"** cho lỗi hay gặp (khi có).
7. **Hộp "Góc AI"** hoặc góc ứng dụng thực tế (khi hợp).
8. Cuối chương: **bảng tóm tắt** (nếu có ≥3 khái niệm) + **hộp Bài tập**.

Đánh số bài tập theo số chương thật: chương 7 → 7.1, 7.2... Lời mở đầu không đánh số nên chương đầu tiên là chương 1.

## 4. Bốn loại hộp màu

Cú pháp (luôn đặt ở cấp cao nhất, không lồng trong danh sách):

```markdown
::: {.box kind="kid" title="Hiểu nhanh qua ví dụ đời thường"}
Nội dung...
:::
```

| kind | Màu | Tiêu đề gợi ý | Dùng cho |
|---|---|---|---|
| `kid` | Xanh dương | "Hiểu nhanh qua ví dụ đời thường" | So sánh đời thường cực ngắn, không thuật ngữ |
| `ai` | Tím | "Góc AI: ..." | Ứng dụng trong AI / prompt mẫu để học cùng AI |
| `warn` | Cam | "Cẩn thận: ..." | Lỗi hay gặp, cạm bẫy |
| `ex` | Xanh lá | "Bài tập" | Bài tập cuối chương |

Mật độ hợp lý: 2–5 hộp mỗi chương. Đừng để hai hộp cùng loại đứng sát nhau.

## 5. Code

- **Hỏi người dùng muốn ngôn ngữ nào** nếu chưa rõ. Mặc định theo ngữ cảnh (sách OOP/pattern → Java hoặc ngôn ngữ người dùng làm việc).
- Một ngôn ngữ chính cho cả sách. Chỉ đổi khi ngôn ngữ chính **không phù hợp tự nhiên** (mô tả công cụ AI → JSON; truy vấn → SQL; cấu hình → YAML) và nói rõ lý do trong văn bản.
- Tên biến/hàm: tiếng Việt không dấu theo **quy ước của ngôn ngữ đó** (Java: `traLoi`, `NhaMayThongBao`; Python: `tra_loi`). **Mọi nơi nhắc tên trong văn bản, bài tập, đáp án, và hình minh hoạ phải khớp** — chạy `check_book.py --lang ...` để bắt chỗ sót.
- Ngắn: 10–30 dòng, tối đa ~40. Dòng ≤ 85 ký tự (dài hơn sẽ bị ngắt xấu trong PDF).
- Comment tiếng Việt cho dòng quan trọng; kết quả in ra ghi ở comment cuối dòng (`// 510`).
- Kiểu "CHƯA TỐT / TỐT HƠN" trong cùng một khối rất hiệu quả cho nguyên tắc thiết kế.
- Được lược `import` và `main` để gọn — nói rõ điều này một lần ở Lời mở đầu.
- **Chạy thử** các đoạn tự chứa được (Java 21 chạy được `java File.java` không cần biên dịch) để chắc comment kết quả là đúng.
- Không đặt emoji trong code (phông mono không có).
- Khi viết lại code từ ngôn ngữ này sang ngôn ngữ khác: cập nhật cả đoạn văn nhắc đến cú pháp riêng (`@decorator`, `yield`, `copy.deepcopy`...) và **thêm ví dụ quen thuộc của hệ sinh thái mới** (Java: `BufferedReader` là Decorator, `Comparator` là Strategy, Spring cho DI...).

## 6. Hình minh hoạ

- Mỗi chương ít nhất 1 hình; khái niệm có cấu trúc (luồng, tầng, trạng thái, so sánh) thì nên có hình.
- Cú pháp: `![Chú thích đầy đủ một câu](img/ten.png){width=85%}` — width 70–100% tuỳ độ rộng hình.
- Vẽ bằng `scripts/diagrams.py` (Graphviz) để đồng bộ màu; hình tự do dùng matplotlib (`setup_matplotlib`, `mpl_save`).
- Chữ trong hình bằng tiếng Việt có dấu, ngắn (≤ 4 dòng mỗi khối).
- Sau khi vẽ: tạo `contact_sheet` và **nhìn** — sơ đồ nào quá rộng (chữ bé) thì đổi `rankdir="TB"` hoặc chia hàng.
- Bìa có thể dùng một hình đẹp nhất của sách (`cover_image`).

## 7. Bảng

- Dùng cho so sánh (A vs B), tóm tắt cuối chương, bảng thuật ngữ, lộ trình học.
- Pipe table Markdown; dòng đầu là tiêu đề. Ô ngắn gọn (≤ 15 từ).
- Bảng tóm tắt pattern/khái niệm nên có cột "Một câu để nhớ" và "Ví dụ đời thường".

## 8. Bài tập và đáp án

- 3–5 bài mỗi chương, 3 mức: `★` dễ (nhắc lại, tự cho ví dụ), `★★` vừa (code nhỏ, phân tích), `★★★` khó (thiết kế mở, đánh đổi, có thể nhờ AI phản biện).
- Bài tập phải **cụ thể**: có số liệu, tình huống, yêu cầu đầu ra rõ.
- Phụ lục A: gợi ý đáp án cho bài có đáp án xác định (tính toán, code ngắn, ghép đôi). Bài thiết kế mở: đưa tiêu chí tự kiểm tra.
- **Tự kiểm tra mọi phép tính** trong đáp án.

## 9. Những lỗi đã gặp về nội dung

| Lỗi | Cách tránh |
|---|---|
| Viết "cho bé 10 tuổi" khi người dùng chỉ muốn **cách giải thích** đơn giản | Xưng "bạn", ví dụ người lớn; dùng `--forbid` khi kiểm tra |
| Đổi ngôn ngữ code nhưng văn bản/bài tập/hình vẫn dùng tên cũ | `check_book.py --lang` + rà hình minh hoạ |
| Lời mở đầu hiện "0.1, 0.2" | Thêm `{.unnumbered}` cho mọi `##` trong lời mở đầu |
| Tham chiếu "xem chương X" sai số | Lập dàn ý chương trước khi viết; rà lại tham chiếu sau cùng |
| Chỉ liệt kê đề mục mà không có nội dung | Mỗi mục phải có: vấn đề, ví dụ, giải pháp, code/hình, khi nào dùng |
