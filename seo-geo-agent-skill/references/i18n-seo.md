# International / i18n SEO

## I18N-01 — Stable locale URLs

Chọn một pattern và dùng nhất quán.

Ví dụ:

```text
/en/docs
/vi/docs
/ja/docs
```

Không thay locale chỉ bằng client state mà vẫn giữ cùng URL nếu muốn từng locale được index riêng.

---

## I18N-02 — Localize, not only translate

Cần localize:
- keywords;
- search intent;
- title;
- meta description;
- examples;
- currency;
- date/unit;
- terminology;
- legal/business context.

---

## I18N-03 — hreflang

Kiểm tra:
- code language/region hợp lệ;
- URL absolute;
- page trả 200;
- reciprocal links;
- self reference;
- canonical không conflict.

Ví dụ:

```html
<link rel="alternate" hreflang="en" href="https://example.com/en/docs" />
<link rel="alternate" hreflang="vi" href="https://example.com/vi/docs" />
<link rel="alternate" hreflang="x-default" href="https://example.com/docs" />
```

---

## I18N-04 — Self canonical

Thông thường:

```text
/vi/docs -> canonical /vi/docs
/en/docs -> canonical /en/docs
```

Không canonical toàn bộ locale về một ngôn ngữ nếu nội dung thực sự là các bản localized cần index.

---

## I18N-05 — Locale redirects

Không ép redirect dựa vào IP/browser language theo cách ngăn crawler/user truy cập locale khác.

Cho phép user đổi language thủ công.

---

## I18N-06 — Sitemap

Sitemap phải bao phủ URL localized quan trọng.

Có thể:
- sitemap chung;
- sitemap theo locale;
- hreflang trong sitemap.

Miễn cấu hình nhất quán và hợp lệ.

---

## I18N-07 — Translation quality

Machine translation có thể là bước đầu, nhưng page production cần review để:
- tự nhiên;
- đúng thuật ngữ;
- đúng intent;
- không sai nghĩa.
