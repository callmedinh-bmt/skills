# Recommended Frontend Tokens

These are a safe baseline, not a universal standard.

```css
:root {
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 24px;
  --space-6: 32px;
  --space-7: 48px;
  --space-8: 64px;

  --radius-sm: 4px;
  --radius-md: 6px;
  --radius-lg: 10px;

  --text-xs: 12px;
  --text-sm: 14px;
  --text-md: 16px;
  --text-lg: 20px;
  --text-xl: 24px;
  --text-page: 32px;

  --control-sm: 28px;
  --control-md: 32px;
  --control-lg: 40px;

  --motion-fast: 100ms;
  --motion-normal: 180ms;
  --motion-slow: 280ms;
}
```

## Token rules
- Do not introduce one-off spacing values unless required.
- Keep radius choices limited.
- Separate semantic colors from raw palette values.
- Use component tokens where needed instead of hardcoded colors.
- Keep motion values consistent across components.
