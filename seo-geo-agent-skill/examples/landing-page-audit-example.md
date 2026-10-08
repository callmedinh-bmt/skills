# Example — Landing Page Audit

## Context

Page:
`https://example.com/loglens`

Goal:
Rank/discover for self-hosted observability use cases and convert users to docs/demo.

## Finding 1

ID: SEO-TECH-001
Severity: P0
Category: Technical SEO

Finding:
Page có `meta name="robots" content="noindex"` trên production.

Why it matters:
Page đang yêu cầu search engine không index.

Fix:

```html
<meta name="robots" content="index,follow" />
```

Hoặc bỏ meta nếu không cần explicit directive.

Validation:
- deploy production;
- fetch rendered HTML;
- dùng URL Inspection;
- chờ recrawl.

Source class:
GOOGLE_REQUIRED / technical eligibility.

---

## Finding 2

ID: SEO-CONTENT-004
Severity: P1
Category: Content/GEO

Finding:
Hero chỉ ghi “Observability made simple” nhưng không nói sản phẩm làm gì, cho ai, hoặc khác biệt ở đâu.

Why it matters:
User và search/AI system thiếu context về entity và use case.

Before:

```text
Observability made simple.
```

After:

```text
Self-hosted observability cho VPS và container: gom log, metric và incident vào một dashboard nhẹ.
```

Validation:
- H1 phù hợp intent;
- product entity rõ;
- nội dung support claims ở section dưới.

Source class:
GOOGLE_RECOMMENDED + GEO_BEST_PRACTICE.

---

## Finding 3

ID: GEO-EVIDENCE-002
Severity: P2
Category: GEO/AEO

Finding:
Page nói “lightweight” nhưng không có benchmark.

Fix:
Thêm test setup thật:

```text
Environment: 2 vCPU / 4 GB RAM
Traffic: 1M log events/day
Peak RAM: ...
P95 ingest latency: ...
```

Kèm methodology và limitation.

Source class:
GEO_BEST_PRACTICE.
