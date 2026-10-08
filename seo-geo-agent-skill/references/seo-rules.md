# SEO Rules

## A. Crawl & Index

### SEO-T01 — Crawlability
Severity mặc định: P0/P1

Kiểm tra:
- robots.txt
- auth wall
- blocked resources
- internal discovery

Google phải có đường hợp lệ để truy cập page muốn index.

### SEO-T02 — Indexability
Severity: P0

Kiểm tra:
- meta robots noindex
- X-Robots-Tag
- canonical conflict
- status code

### SEO-T03 — HTTP status
Severity: P0/P1

- 200: page hợp lệ
- 3xx: redirect có chủ đích
- 4xx: không tồn tại/không truy cập
- 5xx: server error

Tránh redirect loop/chain dài.

### SEO-T04 — Sitemap
Severity: P1/P2

Sitemap nên chứa URL canonical quan trọng và được cập nhật.

Sitemap hỗ trợ discovery nhưng không bảo đảm index.

### SEO-T05 — Canonical
Severity: P0/P1

Mỗi nội dung nên có URL canonical hợp lý.

Sai thường gặp:
- canonical mọi page về homepage;
- canonical locale về locale khác;
- canonical về URL 404;
- HTTP/HTTPS mismatch;
- canonical khác nội dung.

### SEO-T06 — URL
Severity: P2

URL nên:
- ổn định;
- dễ đọc;
- mô tả nội dung;
- tránh ID ngẫu nhiên khi không cần.

### SEO-T07 — Duplicate content
Severity: P1/P2

Giảm nhiều URL có nội dung giống nhau bằng:
- redirect;
- canonical;
- hợp nhất nội dung.

### SEO-T08 — JS rendering
Severity: P1/P2

Nội dung/link quan trọng phải xuất hiện theo cách crawler có thể render và hiểu.

Không block JS/CSS thiết yếu khỏi crawler.

---

## B. Site Architecture

### SEO-A01 — Logical hierarchy

Ưu tiên cấu trúc:

```text
Home
└── Category
    └── Detail
```

Không coi “3 clicks” là luật Google cứng. Đó chỉ là heuristic.

### SEO-A02 — Internal links

Page quan trọng cần internal links từ page khác.

Anchor text nên mô tả destination.

Tránh:
- click here ở mọi chỗ;
- orphan page;
- link spam footer.

---

## C. On-page

### SEO-O01 — Search intent

Page phải khớp mục đích tìm kiếm:
- informational;
- navigational;
- commercial;
- transactional.

### SEO-O02 — Title

Title nên:
- unique;
- rõ;
- mô tả chính xác;
- tập trung topic chính.

Không dùng một giới hạn ký tự cố định như Google requirement.

### SEO-O03 — Meta description

Mỗi page quan trọng nên có description ngắn, riêng, mô tả giá trị page.

Google có thể chọn snippet khác từ nội dung page.

### SEO-O04 — H1 & headings

Heading phải giúp người đọc hiểu cấu trúc.

Ưu tiên hierarchy hợp lý nhưng không tạo heading chỉ để nhét keyword.

### SEO-O05 — Readability

- đoạn ngắn;
- section rõ;
- danh sách khi phù hợp;
- ngữ pháp tốt;
- tránh filler.

### SEO-O06 — Unique value

Page cần thêm giá trị riêng thay vì chỉ rewrite nội dung đã có.

---

## D. Content

### SEO-C01 — People-first

Nội dung phải giải quyết nhu cầu thật của người đọc.

### SEO-C02 — Experience & expertise

Khi phù hợp, thêm:
- người viết;
- kinh nghiệm thực tế;
- test setup;
- methodology;
- limitation;
- source.

### SEO-C03 — Freshness

Cập nhật những phần có khả năng lỗi thời:
- version;
- price;
- feature;
- regulation;
- benchmark;
- compatibility.

### SEO-C04 — Keyword use

Dùng từ khóa tự nhiên.

Không:
- lặp keyword cưỡng ép;
- tạo đoạn khó đọc;
- tạo hàng loạt page cho synonym.

---

## E. Links

### SEO-L01 — Internal links

Link các page liên quan theo ngữ cảnh.

### SEO-L02 — External links

Fact/số liệu quan trọng nên link đến nguồn đáng tin cậy, ưu tiên nguồn gốc.

### SEO-L03 — User-generated links

Content/link do user tạo nên có cơ chế chống spam; `nofollow`/`ugc` có thể phù hợp tùy trường hợp.

---

## F. Images & Video

### SEO-M01 — Image context

Ảnh nên ở gần text liên quan.

### SEO-M02 — Alt text

Alt phải mô tả ý nghĩa ảnh trong context.

Ảnh trang trí có thể dùng `alt=""`.

### SEO-M03 — Performance

Resize/compress ảnh; dùng format hiện đại khi phù hợp.

### SEO-M04 — Video

Video quan trọng nên có:
- page phù hợp;
- title;
- description;
- text context.

---

## G. Structured Data

### SEO-S01 — Accuracy

Schema phải phản ánh nội dung thật trên page.

### SEO-S02 — Eligibility, not guarantee

Structured data có thể làm page đủ điều kiện cho một số search appearance nhưng không bảo đảm hiển thị.

### SEO-S03 — No fake schema

Không khai báo review/rating/product/etc. nếu nội dung đó không tồn tại thật.

---

## H. Mobile & Performance

### SEO-P01 — Mobile parity

Nội dung/link/meta quan trọng trên mobile không được bị mất so với desktop.

### SEO-P02 — Core Web Vitals

Metric hiện tại:
- LCP
- INP
- CLS

FID không còn là Core Web Vital hiện hành.

### SEO-P03 — Common performance issues

Kiểm tra:
- ảnh quá lớn;
- JS bundle quá lớn;
- font blocking;
- third-party scripts;
- no caching;
- render blocking;
- layout shift;
- excessive hydration.
