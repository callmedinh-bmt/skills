---
name: frontend-ui-ux-rules
version: 1.0.0
description: Production-grade frontend UI/UX rules for modern web apps, SaaS, dashboards, developer tools, admin panels, and data-heavy applications. Use this skill before designing, implementing, reviewing, or refactoring frontend UI.
---

# Frontend UI/UX Rules Skill

## When to use
Use this skill whenever the task involves:
- designing a web app, dashboard, SaaS, admin panel, developer tool, or internal tool
- generating React / Next.js / Vue / Svelte frontend
- reviewing UI quality
- improving visual hierarchy, spacing, typography, forms, tables, navigation, motion, accessibility, or responsive behavior
- converting screenshots/specs into production UI
- avoiding generic AI-generated UI

## Core objective
Build interfaces that are:
1. easy to understand
2. easy to scan
3. predictable
4. accessible
5. responsive
6. visually coherent
7. dense enough for real work
8. modern without decorative excess

## Mandatory design order
Always reason and implement in this order:

1. User workflow
2. Information architecture
3. Visual hierarchy
4. Layout and density
5. Typography
6. Spacing
7. Component choice
8. States and feedback
9. Accessibility
10. Responsive behavior
11. Motion
12. Decoration

Never start from gradients, shadows, cards, glassmorphism, or animation.

## Hard rules

### 1. Hierarchy
- Every screen must have one dominant visual focus.
- Primary action must be obvious.
- Secondary actions must be visually quieter.
- Use size, weight, color, and spacing to create hierarchy.
- Do not make all cards, buttons, headings, and badges equally loud.

### 2. Layout
- Prefer clear page structure over card grids.
- Use cards only when content is semantically self-contained.
- Avoid cards inside cards.
- Prefer proximity and spacing before borders.
- Use asymmetric layouts when useful; do not default to 3-column grids.

### 3. Spacing
Use a fixed spacing scale. Recommended baseline:
- 4px micro
- 8px icon/text
- 12px compact controls
- 16px component padding
- 24px group spacing
- 32px section spacing
- 48px major separation
- 64px page-level separation

Do not use arbitrary spacing values unless justified.

### 4. Typography
- Use 1 primary sans font.
- Add 1 monospace font only for code, logs, IDs, timestamps, ports, metrics, and technical data.
- Keep type scale small and consistent.
- Prefer sentence case.
- Do not bold everything.
- Do not use tiny text for core content.

Recommended baseline:
- 12px metadata
- 14px compact UI/body
- 16px standard body
- 20px section title
- 24px large section title
- 32px page title

### 5. Color
- Build with neutral colors first.
- Use one brand accent.
- Use semantic colors for success, warning, danger, and info.
- Never use color alone to communicate state.
- Dark mode requires separate semantic tokens; do not simply invert colors.

### 6. Geometry
- Use few radius tokens.
- Recommended: 4px / 6px / 10px.
- Avoid rounded-xl or rounded-3xl everywhere.
- Use subtle borders more often than heavy shadows.
- Elevation must communicate hierarchy, not decoration.

### 7. Navigation
- Use sidebar navigation for complex applications.
- Group navigation items semantically.
- Use breadcrumbs only when hierarchy is deep.
- Tabs are for sibling views in the same context.
- Do not use tabs as general site navigation.
- Add command palette for power-user apps when useful.

### 8. Data-heavy UI
- Structured data should usually use tables, not cards.
- Tables should support search, filters, sorting, row actions, column controls, and selection when required.
- Charts must answer a specific user question.
- Prefer line charts for trends, sorted bars for category comparison, histograms for distributions, topology graphs for relationships.
- Avoid decorative charts.

### 9. Forms
- Labels must remain visible.
- Placeholder is not a replacement for label.
- Error messages must explain exactly what is wrong and how to fix it.
- Preserve user input after validation errors.
- Use progressive disclosure for advanced options.
- Use inline editing for small contextual edits.

### 10. States
Every important component or screen must consider:
- default
- hover
- active
- focus
- selected
- disabled
- loading
- empty
- error
- success

Never show an empty state when data failed to load.

### 11. Feedback
Every action should have visible feedback.
Examples:
- Saving...
- Saved
- Copied
- Archived + Undo
- Loading progress

Use optimistic UI only for reversible or low-risk actions.

### 12. Overlays
- Modal: short isolated task or destructive confirmation.
- Drawer/sheet: contextual details, filters, quick edit.
- Popover: small contextual controls.
- Tooltip: explanation only, never complex interactive workflow.

### 13. Responsive design
- Components should adapt to available space.
- Prefer container queries when useful.
- Sidebars should collapse on narrow layouts.
- Tables need a deliberate narrow-screen strategy.
- Test zoom and split-screen, not only standard phone widths.

### 14. Accessibility
- Maintain readable contrast.
- Preserve visible keyboard focus.
- Use semantic HTML before custom ARIA.
- Interactive controls must be keyboard usable.
- Icon-only controls require accessible labels.
- Respect prefers-reduced-motion.
- Do not encode status by color alone.

### 15. Motion
- Motion must explain state, direction, relationship, or hierarchy.
- Do not animate everything.
- Recommended timing:
  - 50–150ms: hover/press/microinteraction
  - 150–400ms: panels/modals/larger transitions
- Avoid large hover movement or scale effects on dense app UI.

## Modern web app patterns
Prefer these when they fit the workflow:
- collapsible sidebar
- command palette
- master-detail split view
- right contextual panel
- contextual row actions
- saved views
- scoped search
- inline editing
- progressive disclosure
- empty-state onboarding
- keyboard shortcuts
- density controls
- data as visual identity
- topology / logs / traces / metrics as product visuals

Read: `references/patterns.md`

## Anti-patterns
Do not default to:
- purple/blue neon gradients
- glassmorphism everywhere
- huge rounded cards
- nested cards
- 3-column feature grids everywhere
- giant centered headings inside apps
- decorative charts
- icon-only interfaces with unclear meaning
- huge whitespace in operational dashboards
- random shadows
- random radii
- random spacing values
- excessive pills and badges
- heavy blur
- animated floating cards
- Dribbble-style mockups that ignore real data

Read: `references/anti-patterns.md`

## Recommended product style for modern technical apps
For observability, analytics, developer tools, admin panels, infrastructure products:

- neutral background
- subtle borders
- restricted accent palette
- compact typography
- information-dense layout
- sidebar navigation
- command palette
- split views
- contextual detail panels
- tables for collections
- charts for questions
- topology for relationships
- minimal decoration
- strong keyboard UX

Think: Linear + Vercel + GitHub Primer + Carbon principles, without copying branding.

## Implementation workflow

### Step 1: Understand workflow
Before writing UI code, identify:
- primary user
- main task
- primary action
- critical information
- secondary information
- common repeated actions

### Step 2: Define page structure
Write a text wireframe first.
Example:

```text
Page
├── Header
│   ├── Title
│   ├── Context
│   └── Primary action
├── Toolbar
│   ├── Search
│   ├── Filters
│   └── Secondary actions
├── Main content
└── Context panel
```

### Step 3: Define tokens
Before custom styling, define:
- spacing scale
- typography scale
- colors
- radii
- control heights
- motion timings

Read: `references/tokens.md`

### Step 4: Use library primitives first
Prefer proven libraries before custom components.
Typical choices:
- shadcn/ui
- Radix UI
- React Aria
- TanStack Table
- TanStack Query
- Recharts / ECharts
- React Flow
- Cytoscape
- cmdk

Create custom primitives only when existing libraries cannot satisfy the requirement cleanly.

### Step 5: Build real states
Do not stop at happy-path screenshots.
Implement loading, empty, error, disabled, permissions, long text, overflow, and large data states.

### Step 6: Visual QA
After implementation:
1. render page
2. inspect screenshot
3. check hierarchy
4. check density
5. check typography
6. check alignment
7. remove unnecessary borders/cards
8. verify states
9. verify responsiveness
10. verify keyboard navigation

Read: `references/review-checklist.md`

## Output requirements for AI agents
When generating frontend code:
- explain the page structure briefly before code
- prefer existing design-system components
- do not invent excessive custom components
- do not introduce visual styles outside the token system
- keep component names simple
- keep data-heavy interfaces compact
- use semantic HTML
- include responsive behavior
- include interaction states
- avoid unnecessary animations
- avoid generic AI-style design

## Final quality gate
A page is not finished until all answers are YES:
- Can a user understand the page in 3 seconds?
- Is the primary action obvious?
- Is information hierarchy clear?
- Is spacing consistent?
- Is typography consistent?
- Are colors semantic?
- Are tables used for structured data?
- Do charts answer real questions?
- Are loading/empty/error states designed?
- Is keyboard focus visible?
- Does the page work at narrow widths?
- Can decorative elements be removed without losing usability?
- Does the interface still look intentional with real data?

If any answer is NO, refine the design before shipping.
