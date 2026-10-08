---
name: seo-geo-aeo
version: 1.0.0
description: Audit, design, write, and review websites/pages for SEO, GEO, AEO, international SEO, crawlability, content quality, structured data, AI-search visibility, and launch readiness.
language: vi
tags:
  - seo
  - geo
  - aeo
  - technical-seo
  - content-seo
  - international-seo
  - ai-search
---

# SEO / GEO / AEO Skill

## 1. Mục tiêu

Dùng skill này khi agent cần:

- Audit SEO/GEO cho website, landing page, blog, docs hoặc product page.
- Thiết kế website mới có SEO/GEO ngay từ kiến trúc.
- Review HTML/Next.js/React/Nuxt/Vue/Svelte/CMS theo SEO.
- Viết hoặc tối ưu title, meta description, heading, nội dung, internal link, image alt.
- Kiểm tra crawl/index/canonical/sitemap/robots/structured data.
- Tối ưu nội dung cho Google Search và AI Search.
- Làm international SEO: locale URL, hreflang, canonical, sitemap, localized metadata.
- Tạo báo cáo audit với severity và cách sửa cụ thể.

Không dùng skill này để hứa hẹn thứ hạng hoặc traffic cụ thể.

---

## 2. Source priority

Khi các nguồn mâu thuẫn, ưu tiên theo thứ tự:

1. Google Search Central / Google Developers.
2. Tiêu chuẩn chính thức liên quan đến web/platform nếu có.
3. Better i18n cho international SEO.
4. Semrush cho workflow/best practice thực chiến.
5. WRITER cho GEO/AEO best practice.

Phân loại mọi rule:

- `GOOGLE_REQUIRED`: yêu cầu hoặc điều kiện kỹ thuật trực tiếp từ Google.
- `GOOGLE_RECOMMENDED`: Google khuyến nghị.
- `INDUSTRY_BEST_PRACTICE`: thực hành tốt nhưng không phải ranking requirement chính thức.
- `GEO_BEST_PRACTICE`: giúp nội dung dễ được AI hiểu/trích dẫn, không phải bảo đảm visibility.

Không biến best practice thành “Google bắt buộc”.

---

## 3. Nguyên tắc cứng

### 3.1 Không được hứa hẹn ranking

Không nói:

- “Làm vậy chắc chắn top 1.”
- “Schema này giúp lên AI Overview.”
- “llms.txt giúp Google AI rank cao hơn.”

Phải nói theo dạng:

- “giúp Google hiểu nội dung tốt hơn”
- “có thể cải thiện khả năng được crawl/index”
- “có thể tăng khả năng nội dung dễ được AI trích dẫn”

### 3.2 Ưu tiên người dùng trước

Nội dung phải:

- hữu ích;
- đúng intent;
- rõ ràng;
- có giá trị riêng;
- cập nhật;
- có nguồn khi có fact/số liệu;
- không nhồi keyword.

### 3.3 Không spam

Không khuyến nghị:

- keyword stuffing;
- hàng loạt page gần giống nhau chỉ đổi keyword;
- fake backlink;
- fake review;
- fake Reddit/forum mention;
- AI-generated page hàng loạt không có giá trị;
- hidden text/link để thao túng Search.

### 3.4 GEO không thay thế SEO

Đối với Google AI Search, SEO nền tảng vẫn là điều kiện chính:

`crawlable -> indexable -> useful -> understandable -> trustworthy`

GEO/AEO là lớp tối ưu thêm cho khả năng AI hiểu, tổng hợp và trích dẫn nội dung.

---

## 4. Quy trình chuẩn

Khi nhận một website/page, luôn đi theo thứ tự:

```text
1. Discovery
   ↓
2. Crawl & Index
   ↓
3. Site Architecture
   ↓
4. On-page SEO
   ↓
5. Content Quality
   ↓
6. Internal/External Links
   ↓
7. Media SEO
   ↓
8. Structured Data
   ↓
9. Performance & Mobile
   ↓
10. GEO/AEO
   ↓
11. i18n SEO nếu có
   ↓
12. Measurement
   ↓
13. Final prioritized fixes
```

Không audit GEO trước khi xác nhận page có thể crawl/index.

---

## 5. Severity

Mỗi issue phải có severity:

- `P0 - Blocker`: có thể làm page không crawl/index hoặc tạo lỗi nghiêm trọng.
- `P1 - High`: ảnh hưởng lớn đến khả năng hiểu, chất lượng hoặc discoverability.
- `P2 - Medium`: tối ưu quan trọng nhưng không chặn hệ thống.
- `P3 - Low`: refinement/nice-to-have.

Ví dụ:

- `noindex` trên landing production -> P0.
- canonical trỏ sai domain -> P0/P1.
- title trùng nhiều page -> P1.
- alt text thiếu ở ảnh trang trí -> P3 hoặc không issue nếu `alt=""` đúng ngữ nghĩa.

---

## 6. Audit contract

Mỗi audit phải trả về tối thiểu:

1. `Summary`
2. `Critical Issues`
3. `Technical SEO`
4. `On-page SEO`
5. `Content`
6. `GEO/AEO`
7. `International SEO` nếu có
8. `Structured Data`
9. `Performance/Mobile`
10. `Prioritized Action Plan`

Mỗi issue theo format:

```text
ID: SEO-TECH-001
Severity: P1
Category: Technical SEO
Finding: Canonical trỏ sang URL khác không tương đương.
Why it matters: Google có thể chọn URL khác làm canonical.
Evidence: <code/url/screenshot>
Fix: Đổi canonical về URL chính xác.
Validation: Re-crawl + URL Inspection.
Source class: GOOGLE_RECOMMENDED
```

Không chỉ nói “SEO chưa tốt”. Phải chỉ ra bằng chứng và cách xác nhận sau sửa.

---

## 7. Technical SEO rules

Luôn kiểm tra:

- HTTP status.
- robots.txt.
- meta robots / X-Robots-Tag.
- crawlability.
- indexability.
- canonical.
- redirect chain/loop.
- sitemap.xml.
- orphan pages.
- URL structure.
- duplicate content.
- JS rendering của nội dung quan trọng.
- CSS/JS/resource có bị block không.
- mobile availability.
- HTTPS.

Rule chi tiết: `references/seo-rules.md`.

---

## 8. On-page rules

Mỗi page phải kiểm tra:

- search intent;
- topic chính;
- unique `<title>`;
- meta description;
- H1;
- heading hierarchy;
- URL mô tả;
- intro trả lời đúng intent;
- content depth phù hợp;
- internal links;
- external sources khi có fact;
- image alt;
- duplicate/thin content.

Không đặt giới hạn cứng kiểu “title phải 60 ký tự” như một luật của Google. Có thể dùng giới hạn hiển thị như heuristic (quy tắc kinh nghiệm), nhưng phải ghi rõ là best practice.

---

## 9. Content rules

Ưu tiên:

- original experience;
- original research;
- benchmark;
- case study;
- screenshots/logs/results;
- clear examples;
- expert review;
- references to primary sources.

Nếu nội dung chỉ paraphrase 5 bài khác mà không thêm giá trị -> đánh dấu `P1/P2 thin/commodity content`.

---

## 10. GEO/AEO rules

Mục tiêu: làm nội dung dễ hiểu, dễ trích xuất, dễ xác minh.

Khuyến nghị:

- answer-first;
- câu trả lời ngắn ngay sau heading khi phù hợp;
- heading dạng câu hỏi khi tự nhiên;
- facts có citation;
- entity rõ ràng;
- table/list/steps khi giúp đọc nhanh;
- original data;
- comparison content;
- case study;
- author/expertise rõ;
- brand/entity nhất quán trên các nguồn;
- cập nhật nội dung cũ.

Không bắt buộc:

- llms.txt để rank Google;
- “AI schema” đặc biệt;
- artificial chunking;
- tạo page cho mọi long-tail variation.

Chi tiết: `references/geo-aeo-rules.md`.

---

## 11. International SEO

Nếu site có nhiều ngôn ngữ/quốc gia:

- locale URL ổn định;
- self-canonical;
- hreflang đúng;
- reciprocal hreflang;
- x-default nếu phù hợp;
- localized title/meta/content;
- không ép redirect làm crawler không truy cập được locale;
- sitemap chứa locale đúng;
- từ khóa phải localize, không chỉ dịch máy.

Chi tiết: `references/i18n-seo.md`.

---

## 12. Structured data

Chỉ thêm schema khi:

- đúng loại page;
- phản ánh nội dung người dùng nhìn thấy;
- dữ liệu chính xác;
- tuân thủ Google structured data guideline.

Ví dụ thường dùng:

- Organization
- WebSite
- BreadcrumbList
- Article
- Product
- VideoObject
- SoftwareApplication khi phù hợp

Không tự thêm schema chỉ vì “SEO tốt hơn”.

---

## 13. Performance

Core Web Vitals hiện tại:

- LCP
- INP
- CLS

Không dùng FID như metric Core Web Vitals hiện hành.

Performance audit nên kiểm tra:

- oversized images;
- render-blocking resources;
- JS bundle lớn;
- hydration quá mức;
- third-party scripts;
- caching;
- CDN;
- font loading;
- lazy loading;
- layout shifts.

Không coi đạt Core Web Vitals là bảo đảm ranking.

---

## 14. Khi viết page mới

Workflow bắt buộc:

1. Xác định audience.
2. Xác định search intent.
3. Xác định primary topic.
4. Xác định supporting entities/questions.
5. Viết page outline.
6. Viết answer-first intro.
7. Thêm proof/data/examples.
8. Thêm internal links.
9. Thêm external primary sources.
10. Viết metadata.
11. Thêm schema nếu hợp lệ.
12. Review crawl/index/mobile/performance.
13. Review GEO extractability.

Dùng `workflows/create-or-optimize-page.md`.

---

## 15. Output style

Ưu tiên câu ngắn, rõ, actionable.

Không chỉ nêu lỗi. Phải đưa code/fix khi có thể.

Ví dụ:

```html
<link rel="canonical" href="https://example.com/observability" />
```

Nếu review code framework, phải chỉ rõ file/component có thể sửa.

---

## 16. Definition of Done

Một page chỉ được coi là “SEO/GEO ready” khi:

- không có P0;
- P1 quan trọng đã được xử lý hoặc có lý do chấp nhận;
- crawl/index path rõ;
- title/H1/content intent nhất quán;
- canonical đúng;
- mobile usable;
- không spam;
- nội dung có giá trị riêng;
- fact quan trọng có nguồn;
- GEO structure rõ;
- analytics/Search Console strategy tồn tại.

Dùng checklist tại `checklists/master-checklist.md`.

---

## 17. Canonical references

Xem `references/sources.md`.
