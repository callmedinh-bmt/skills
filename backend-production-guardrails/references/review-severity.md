# Review Severity Guide

## P0 — Critical

Use when exploitation/failure can plausibly cause immediate severe damage.

Examples:

- production secret/private key committed or exposed;
- authentication bypass affecting protected data/actions;
- cross-tenant authorization bypass with broad sensitive access;
- SQL injection/RCE with realistic exploit path;
- duplicate charging or money movement under normal retry behavior;
- migration that can irreversibly destroy large amounts of data without a recovery path;
- unrestricted destructive admin action exposed publicly.

Expected action: block release and fix immediately.

## P1 — High

Examples:

- missing object-level authorization on sensitive resource;
- unbounded expensive endpoint that can cause realistic outage/cost abuse;
- no timeout on a critical dependency in the main request path;
- uncontrolled retry multiplication causing dependency overload;
- risky schema change incompatible with rolling deployment;
- no duplicate protection on order/payment/webhook side effects;
- no rollback/forward-fix for a high-risk release;
- public debug/profiling endpoint with sensitive internals.

Expected action: normally block release.

## P2 — Medium

Examples:

- weak observability making incidents difficult to diagnose;
- missing audit trail for sensitive but non-catastrophic operations;
- query/index issue likely to degrade at expected growth;
- noisy or ineffective health probe;
- backup exists but restore drill is stale;
- dependency vulnerability with limited exploitability in current architecture.

Expected action: fix soon; may ship only with explicit risk acceptance.

## P3 — Low

Examples:

- inconsistent error codes;
- minor missing metadata in logs;
- cleanup that improves resilience but has little immediate risk;
- optional hardening with no realistic current exploit/failure path.

Expected action: backlog or opportunistic fix.

## Finding quality rules

Every finding must answer:

1. **Where?** Exact file, function, route, schema, manifest, or component when known.
2. **What fails?** A concrete reproduction/failure scenario.
3. **Impact?** Security, integrity, availability, money, privacy, or operability.
4. **Why now?** Explain why the current code/config permits it.
5. **Smallest fix?** Prefer a precise local correction.
6. **How to prove?** Test, query, load test, migration rehearsal, or operational check.

Do not report speculative findings as confirmed bugs. Label uncertainty explicitly.
