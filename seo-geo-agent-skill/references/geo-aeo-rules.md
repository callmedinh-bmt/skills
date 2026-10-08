# GEO / AEO Rules

## 1. Mental model

GEO = Generative Engine Optimization.
AEO = Answer Engine Optimization.

Mục tiêu thực tế:

- máy hiểu nội dung dễ hơn;
- câu trả lời dễ được trích xuất;
- fact dễ kiểm chứng;
- entity rõ;
- website có thông tin đáng để citation.

Không có kỹ thuật nào bảo đảm AI sẽ cite website.

---

## 2. Foundation

### GEO-01 — SEO first

Page phải crawl/index được trước khi nói về Google AI visibility.

### GEO-02 — Useful content

Nội dung phải hữu ích cho người dùng, không viết chỉ để “feed AI”.

---

## 3. Answer structure

### GEO-03 — Answer first

Khi section trả lời một câu hỏi cụ thể:

```text
Question heading
↓
Direct answer
↓
Evidence / explanation
↓
Example
↓
Related links
```

Không có số từ bắt buộc của Google cho direct answer.

### GEO-04 — Clear headings

Heading có thể dạng câu hỏi nếu đúng cách người dùng hỏi.

### GEO-05 — Extractable formatting

Dùng:
- short paragraph;
- bullets;
- steps;
- table;
- definition block;

khi chúng thực sự làm nội dung dễ hiểu.

Không “chunk” nhân tạo chỉ để phục vụ AI.

---

## 4. Evidence

### GEO-06 — Cite facts

Fact quan trọng nên có nguồn.

Ưu tiên:
1. official documentation;
2. original research;
3. standards;
4. reputable independent source.

### GEO-07 — Original evidence

Nội dung mạnh:
- benchmark;
- experiment;
- case study;
- internal dataset;
- survey;
- implementation result;
- failure analysis.

Ví dụ tốt:

```text
Chúng tôi chạy 1 triệu log/ngày trên VPS 4 GB RAM.
Setup: ...
Result: ...
Limitation: ...
```

Tốt hơn nhiều so với:

```text
Monitoring giúp hệ thống tốt hơn.
```

---

## 5. Entity clarity

### GEO-08 — Name entities explicitly

Tránh chuỗi đại từ mơ hồ:

`nó -> hệ thống -> công cụ -> giải pháp`

Khi context dễ mất, nhắc lại tên entity:

`OpenTelemetry Collector`, `Prometheus`, `LogLens`.

### GEO-09 — Consistent facts

Giữ thống nhất:
- brand name;
- product name;
- description;
- feature;
- pricing;
- contact;
- release/version.

---

## 6. Content formats mạnh cho GEO

Khi phù hợp:

- definition page;
- comparison;
- how-to;
- troubleshooting;
- FAQ nội dung;
- benchmark;
- case study;
- original research;
- glossary;
- decision guide.

Không dùng FAQ schema chỉ vì có FAQ content. Rich result support phải kiểm tra theo Google hiện tại.

---

## 7. Trust & reputation

### GEO-10 — Author signals

Có thể thêm:
- author name;
- role;
- experience;
- review date;
- sources;
- methodology.

### GEO-11 — Third-party presence

Brand mention/review ngoài website có thể giúp hệ sinh thái thông tin phong phú hơn.

Không tạo fake mention/review/thread.

---

## 8. GEO anti-patterns

### GEO-X01 — llms.txt ranking myth

Không coi `llms.txt` là ranking factor Google hoặc điều kiện để Google AI hiểu site.

### GEO-X02 — AI schema myth

Không có “AI schema” bắt buộc cho AI Overview/AI Mode.

### GEO-X03 — Long-tail page explosion

Không tạo hàng nghìn page chỉ đổi một biến thể keyword.

### GEO-X04 — Artificial chunking

Không chia mọi nội dung thành đoạn siêu ngắn chỉ để “LLM đọc”.

### GEO-X05 — AI content spam

AI có thể hỗ trợ viết, nhưng output cuối phải:
- có giá trị;
- chính xác;
- kiểm chứng được;
- không scaled-content spam.

---

## 9. GEO audit questions

Agent phải hỏi/kiểm tra:

1. Page trả lời câu hỏi gì?
2. Direct answer nằm ở đâu?
3. Có fact nào không có source?
4. Có original evidence không?
5. Entity có mơ hồ không?
6. Có comparison/use-case thực tế không?
7. Có tác giả/methodology khi cần không?
8. Nội dung có cũ không?
9. Có statement nào nghe như marketing nhưng không chứng minh được không?
10. Nếu bỏ tên brand ra, bài có giống 100 bài khác không?

Nếu câu 10 là “có”, page có nguy cơ commodity/thin content.
