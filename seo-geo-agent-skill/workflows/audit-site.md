# Workflow — Audit Website

## Input

Có thể nhận:
- URL;
- repo/source code;
- rendered HTML;
- sitemap;
- robots.txt;
- Lighthouse/Search Console data;
- screenshots.

## Step 1 — Scope

Xác định:
- website type;
- primary audience;
- target market/language;
- business goal;
- page types;
- framework/CMS.

## Step 2 — Discovery

Lấy mẫu:
- homepage;
- category;
- detail/product/article;
- auth-free public docs;
- localized pages nếu có.

## Step 3 — Technical

Kiểm tra:
- status;
- robots;
- noindex;
- canonical;
- sitemap;
- redirects;
- duplicate URLs;
- JS-rendered content;
- orphan pages.

Nếu có P0, báo trước các tối ưu khác.

## Step 4 — Architecture

Kiểm tra:
- hierarchy;
- navigation;
- breadcrumbs;
- internal links;
- URL patterns;
- taxonomy.

## Step 5 — On-page

Cho từng page mẫu:
- title;
- description;
- H1;
- headings;
- search intent;
- internal links;
- image alt;
- content uniqueness.

## Step 6 — Content

Đánh giá:
- people-first;
- original value;
- evidence;
- freshness;
- thin/duplicate;
- expertise/experience.

## Step 7 — GEO/AEO

Đánh giá:
- answer-first;
- questions;
- entities;
- citations;
- original data;
- comparison;
- extractable structure;
- brand consistency.

## Step 8 — i18n

Nếu có locale:
- locale URLs;
- hreflang;
- canonical;
- translated metadata;
- local intent.

## Step 9 — Performance

Kiểm tra:
- LCP;
- INP;
- CLS;
- large images;
- JS;
- fonts;
- scripts;
- caching.

## Step 10 — Report

Output theo `templates/audit-report.md`.

Prioritize:

```text
P0 -> sửa ngay
P1 -> sprint hiện tại
P2 -> sprint tiếp theo
P3 -> tối ưu dần
```
