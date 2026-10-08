# Backend Production Audit

## Verdict

`READY | READY WITH RISKS | NOT READY`

Reason: <one short paragraph>

## Release blockers

| Severity | Component | Problem | Failure scenario | Required fix |
|---|---|---|---|---|
| P0/P1 | | | | |

## Findings

### <P0/P1/P2/P3> — <short title>

- **Location:** `<file:function/route/component>`
- **Evidence:** <what the code/config actually does>
- **Failure scenario:** <concrete scenario>
- **Impact:** <security/data/availability/money/privacy/operations>
- **Fix:** <smallest safe fix>
- **Verification:** <test/check to prove the fix>

## Good existing controls

- <evidence-backed item>

## Production readiness checklist

| Area | Status | Notes |
|---|---|---|
| Security | PASS/FAIL/UNKNOWN/N/A | |
| API/abuse resistance | | |
| Data integrity | | |
| Migrations | | |
| Dependencies/retries | | |
| Workers/webhooks | | |
| Observability | | |
| Runtime/lifecycle | | |
| Release/rollback | | |
| Backup/recovery | | |

## Residual risks / unknowns

- <unknown that could materially change the verdict>

## Recommended fix order

1. P0 release blockers.
2. P1 release blockers.
3. Data integrity and rollback/recovery gaps.
4. Observability and operational risks.
5. P2/P3 hardening.
