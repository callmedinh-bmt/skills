# Workflow — Pre-launch SEO/GEO Review

## P0 Gate

Không launch nếu có:
- production `noindex` ngoài ý muốn;
- robots block site quan trọng;
- canonical sai domain;
- redirect loop;
- page chính trả 4xx/5xx;
- staging domain được index nhưng production bị block;
- hreflang/canonical tạo vòng sai nghiêm trọng.

## P1 Gate

Nên sửa trước launch:
- title/H1 không rõ;
- duplicate metadata diện rộng;
- sitemap thiếu page chính;
- mobile thiếu content;
- page quan trọng không có internal link;
- nội dung placeholder/thin;
- claim marketing không có bằng chứng.

## Launch checks

- production URL live;
- HTTPS;
- robots.txt;
- sitemap.xml;
- canonical;
- Search Console property;
- analytics;
- 404 page;
- redirect map;
- structured data validation;
- mobile test;
- CWV baseline.

## Post-launch

Theo dõi:
- index coverage;
- crawl errors;
- query/impressions/clicks;
- CWV;
- rich result errors;
- conversion;
- content freshness.
