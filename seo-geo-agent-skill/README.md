# SEO / GEO / AEO Agent Skill Pack

Bộ skill dùng để audit, thiết kế và tối ưu website cho:

- SEO kỹ thuật
- On-page SEO
- Content SEO
- GEO / AEO / AI Search
- International SEO
- Structured Data
- Performance
- Pre-launch review

## Cấu trúc

```text
seo-geo-agent-skill/
├── SKILL.md
├── README.md
├── references/
│   ├── sources.md
│   ├── seo-rules.md
│   ├── geo-aeo-rules.md
│   └── i18n-seo.md
├── workflows/
│   ├── audit-site.md
│   ├── create-or-optimize-page.md
│   └── prelaunch-review.md
├── templates/
│   ├── audit-report.md
│   ├── page-brief.md
│   └── page-output.md
├── checklists/
│   └── master-checklist.md
└── examples/
    └── landing-page-audit-example.md
```

## Cách dùng

Cho agent đọc `SKILL.md` trước. Agent chỉ mở thêm file reference/workflow khi nhiệm vụ cần tới.

Ví dụ prompt:

```text
Use the seo-geo-aeo skill.
Audit this landing page for SEO + GEO.
Return P0/P1/P2/P3 issues, evidence, exact fixes, and validation steps.
```

Hoặc:

```text
Use the seo-geo-aeo skill.
Create an SEO/GEO-ready landing page brief for a self-hosted observability platform.
Target: backend/devops engineers in Vietnam.
```

## Nguyên tắc nguồn

Google Search Central luôn có ưu tiên cao nhất khi rule liên quan Google Search. Better i18n, Semrush và WRITER bổ sung workflow/best practice, không được dùng để thay thế guideline chính thức của Google.
