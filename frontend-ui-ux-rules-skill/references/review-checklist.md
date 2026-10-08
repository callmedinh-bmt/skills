# Frontend Review Checklist

## Hierarchy
- Can the user understand the page purpose in 3 seconds?
- Is one primary action clearly dominant?
- Are secondary actions quieter?

## Layout
- Is the page structure obvious?
- Are there unnecessary cards or borders?
- Is the density appropriate for the task?

## Typography
- Are font sizes consistent?
- Is text readable?
- Is monospace used only for technical content?

## Color
- Is contrast sufficient?
- Are semantic colors used consistently?
- Is any meaning conveyed by color only?

## Tables and charts
- Is structured data represented as a table when appropriate?
- Does each chart answer a real user question?

## Forms
- Are labels visible?
- Are error messages specific?
- Does failed validation preserve input?

## States
- Loading?
- Empty?
- Error?
- Disabled?
- Success?
- Permission denied?

## Accessibility
- Keyboard navigation works?
- Focus visible?
- Accessible names on icon buttons?
- Semantic HTML used?
- Reduced motion respected?

## Responsive
- Works at narrow widths?
- Sidebar collapses correctly?
- Table overflow handled deliberately?
- Content works at browser zoom?

## Performance perception
- Does each user action receive immediate feedback?
- Are expensive visual effects avoided?

## Anti-slop check
Remove or redesign if found:
- unnecessary gradients
- nested cards
- random glows
- giant rounded panels
- repeated 3-column card grids
- decorative charts
- floating animation
