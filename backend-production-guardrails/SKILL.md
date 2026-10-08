---
name: backend-production-guardrails
description: Design, implement, review, harden, and productionize backend services and APIs. Use when building or modifying backend endpoints, database logic, authentication/authorization, background jobs, integrations, observability, deployments, or when auditing a backend repository for production-readiness, reliability, security, data-integrity, and operability issues.
---

# Backend Production Guardrails

Use this skill as a production-quality gate for backend work.

It is stack-agnostic. Apply it to Go, Java/Spring, Node.js/NestJS, Python, .NET, Rust, or similar backend stacks. Adapt implementation details to the existing architecture instead of forcing a new architecture.

## Core principle

Assume all of these can happen:

- clients send invalid or malicious input;
- requests are duplicated or retried;
- two requests race for the same data;
- network calls hang, fail, or return late;
- dependencies become slow or unavailable;
- a deployment partially fails;
- an instance is terminated while serving traffic;
- credentials leak unless explicitly protected;
- operators need to debug an incident with incomplete context;
- backups are useless unless restoration is proven.

Design for those cases before calling a backend production-ready.

## When to use this skill

Use it for one or more of these modes:

1. **BUILD** — creating or changing backend code.
2. **REVIEW** — auditing code, configuration, database schema, API behavior, or infrastructure.
3. **RELEASE** — deciding whether a service is safe to deploy.
4. **INCIDENT** — diagnosing production failures and proposing the smallest safe fix.

Do not over-engineer toy examples or throwaway prototypes unless the user explicitly asks for production-grade behavior.

## Start by understanding the system

Before changing code, inspect available project context and identify:

- language and framework;
- API style: REST, gRPC, GraphQL, events, webhooks;
- authentication and authorization model;
- database and ORM/query layer;
- cache, queue, scheduler, object storage, email/SMS, payment, or other external dependencies;
- deployment target: VM, Docker, Kubernetes, serverless, PaaS;
- current logging, metrics, tracing, health checks, CI/CD, migrations, and backup strategy;
- existing conventions and architecture.

Prefer evidence from the repository over assumptions. If an important fact cannot be determined, state the assumption instead of inventing one.

## Non-negotiable production rules

Treat violations of the following as release blockers unless the project context clearly makes the rule inapplicable:

1. Validate and normalize untrusted input on the server.
2. Enforce authentication and authorization at the backend, including object-level and function-level authorization.
3. Never trust hidden frontend controls as a security boundary.
4. Use HTTPS/TLS for production traffic carrying credentials or sensitive data.
5. Never commit secrets, credentials, private keys, tokens, or production passwords to source control.
6. Never log secrets, passwords, session identifiers, authorization headers, private keys, or full sensitive payloads.
7. Store passwords with a purpose-built password hashing function such as Argon2id; never plaintext or general-purpose hashes alone.
8. Use parameterized database queries; never concatenate untrusted input into SQL.
9. Enforce important invariants in the database with constraints where possible.
10. Use transactions when a business operation must succeed or fail atomically.
11. Design critical write operations for concurrency and duplicate requests.
12. Add timeouts to network, database, cache, queue, and storage calls.
13. Retries must be bounded and only used when safe; use backoff and jitter where appropriate.
14. Do not retry non-idempotent side effects blindly. Use idempotency keys, deduplication, unique business keys, or equivalent safeguards.
15. Protect expensive or abuse-prone endpoints with limits and rate controls.
16. Bound request body size, upload size, pagination size, query complexity, queue depth, and other resource consumption.
17. Keep processes stateless when horizontal scaling requires it; persist shared state in appropriate backing services.
18. Support graceful shutdown and stop accepting new work before process exit.
19. Expose meaningful health/readiness signals appropriate to the deployment platform.
20. Use structured logs with correlation identifiers such as request ID and trace ID.
21. Measure at least latency, traffic, errors, and saturation for important services.
22. Client-facing errors must not expose stack traces, secrets, SQL, filesystem paths, or internal topology.
23. Database migrations must be versioned, reviewable, and safe for the deployment strategy.
24. Schema changes must consider old and new application versions running at the same time.
25. Connection pools and worker concurrency must be bounded.
26. Production configuration must be externalized from source code.
27. Builds/releases must be traceable to a version or commit.
28. A deployment must have a tested rollback or forward-fix strategy.
29. Backups must be automated for critical data and restoration must be tested.
30. Dependencies must be pinned/locked where appropriate and checked for known vulnerabilities.
31. Privileges for services, databases, cloud identities, and secrets must follow least privilege.
32. Sensitive administrative, debug, profiling, and metrics endpoints must not be unintentionally exposed publicly.
33. Security-sensitive and destructive operations should be auditable.
34. Breaking API or event-contract changes require an explicit compatibility/versioning plan.
35. Production changes must not depend on undocumented manual steps known by only one person.

Read `references/backend-production-rules.md` for the detailed rule catalog and implementation guidance.

## Workflow

### Step 1 — Classify the task

Choose the relevant mode: BUILD, REVIEW, RELEASE, or INCIDENT. Multiple modes may apply.

### Step 2 — Map the request/data flow

For the code or feature being changed, trace:

`client -> edge/proxy -> handler/controller -> auth -> validation -> business logic -> database/cache/queue/external service -> response/event`

Identify trust boundaries and irreversible side effects such as:

- payment;
- money or credits;
- email/SMS;
- file deletion;
- privilege changes;
- account deletion;
- inventory changes;
- external API mutations;
- event publication.

### Step 3 — Check invariants and failure modes

For each important operation, answer:

- What must always remain true?
- What happens if the same request arrives twice?
- What happens if two requests run concurrently?
- What happens if the dependency succeeds but the response is lost?
- What happens if the database commit succeeds but event publication fails?
- What happens if the process dies halfway through?
- What is the timeout?
- Is retry safe?
- Can the failure be observed and traced?
- Can an operator recover safely?

### Step 4 — Implement the smallest safe solution

Prefer simple, local changes that fit the current stack.

Examples:

- unique constraint before distributed lock;
- transaction before custom compensation logic when one database is sufficient;
- bounded retry before a complex resilience framework;
- structured logs before introducing a new logging platform;
- database-backed idempotency before distributed coordination when it satisfies the requirement.

Do not add microservices, Kafka, service mesh, CQRS, event sourcing, Redis locks, or Kubernetes merely because they are common production technologies.

### Step 5 — Add verification

When relevant, verify with tests covering:

- valid request;
- invalid input;
- unauthorized/forbidden access;
- duplicate request;
- concurrent request;
- dependency timeout/failure;
- transaction rollback;
- boundary values;
- pagination/resource limits;
- migration compatibility;
- graceful shutdown or worker interruption;
- idempotency of side effects.

Do not claim a test passed unless it was actually run or the evidence is available.

### Step 6 — Run the release gate

Use `assets/production-readiness-checklist.md` before declaring a backend production-ready.

If a blocker remains, say the service is **not production-ready** and explain exactly why.

## Review severity

Use these levels:

- **P0 — Critical:** likely security compromise, data corruption/loss, duplicate money movement, secret exposure, or catastrophic outage. Release blocker.
- **P1 — High:** realistic authorization bypass, unbounded resource exhaustion, unsafe migration, missing rollback for high-risk change, uncontrolled retry storm, or major operability gap. Normally a release blocker.
- **P2 — Medium:** meaningful reliability, observability, maintainability, or defense-in-depth weakness that should be fixed soon.
- **P3 — Low:** hardening, consistency, cleanup, or optimization with limited immediate risk.

See `references/review-severity.md` for examples.

## Required review output

When auditing a project, produce findings in this order:

1. **Verdict** — `READY`, `READY WITH RISKS`, or `NOT READY`.
2. **Release blockers** — P0/P1 only.
3. **Findings** — each finding must include:
   - severity;
   - exact file/component when known;
   - concrete failure scenario;
   - why it matters;
   - smallest recommended fix;
   - verification/test to add.
4. **What is already good** — only evidence-backed positives.
5. **Production checklist status**.
6. **Residual risks / unknowns**.

Use `assets/audit-report-template.md` when a structured report is useful.

## Coding behavior

When directly editing backend code:

- follow the repository's current style and conventions;
- preserve public contracts unless a breaking change is explicitly required;
- avoid unrelated refactors;
- avoid swallowing errors;
- keep error handling explicit;
- return stable machine-readable error codes when the project uses them;
- propagate cancellation/deadlines through downstream calls when the stack supports it;
- never disable TLS verification, certificate checks, authentication, authorization, validation, or security controls merely to make a request work;
- never hard-code production credentials;
- avoid logging full request/response payloads by default;
- prefer migrations over manual schema changes;
- keep rollback/compatibility in mind for every persistent data change.

## Database rules

For every important table or write path, inspect:

- primary key;
- unique constraints;
- foreign keys where appropriate;
- nullability;
- check constraints where useful;
- indexes for real query patterns;
- transaction boundaries;
- isolation/concurrency behavior;
- deletion behavior;
- audit/history requirements;
- migration compatibility;
- connection-pool limits.

Do not rely on `SELECT then INSERT` for uniqueness without a database constraint.

Do not hold a transaction open while performing slow network calls unless the design explicitly requires it and the trade-off is justified.

## External dependency rules

Every external call should have an explicit policy for:

- timeout;
- retry eligibility;
- retry count/budget;
- backoff/jitter where relevant;
- idempotency;
- error mapping;
- circuit breaking or load shedding when justified by scale/failure mode;
- observability;
- secret handling.

Never assume `200 OK` alone means a business operation succeeded if the provider defines its own status field or asynchronous completion model.

## Background jobs and events

For queues, schedulers, consumers, and webhooks, check:

- at-least-once delivery assumptions;
- duplicate processing;
- poison messages;
- retry limits;
- dead-letter handling when appropriate;
- ordering assumptions;
- idempotent consumer behavior;
- visibility/acknowledgement semantics;
- observability and replay strategy;
- transactional gap between database changes and event publication.

Use an outbox/inbox pattern only when the consistency problem actually requires it.

## Observability rules

Prefer logs that are structured and queryable. Include relevant fields such as:

- timestamp;
- level;
- service;
- environment;
- version/commit;
- request_id;
- trace_id/span_id;
- route or operation;
- status/error_code;
- duration;
- relevant non-sensitive business identifiers.

Do not put high-cardinality or sensitive values into metric labels without understanding the cost/risk.

Alerts should map to a human action or an SLO/user-impact signal, not merely noisy infrastructure fluctuations.

## Deployment and recovery rules

Before release, determine:

- exact artifact/version being deployed;
- migration ordering;
- compatibility with old instances;
- health/readiness behavior;
- shutdown/draining behavior;
- rollback or forward-fix procedure;
- secret/config rollout;
- dependency changes;
- backup status for risky data changes;
- post-deploy verification;
- ownership/runbook for failure.

A backup is not considered proven until restoration has been tested and the restored data has been validated.

## Security source hierarchy

When current guidance matters, prefer:

1. project/vendor official documentation;
2. OWASP Cheat Sheet Series and OWASP API Security;
3. language/framework official security documentation;
4. cloud/platform official reliability guidance;
5. OpenTelemetry/Kubernetes/standards documentation;
6. reputable secondary sources only when primary sources do not cover the issue.

Do not invent a CVE, vulnerability status, framework behavior, or compliance requirement. Verify time-sensitive claims from authoritative current sources.

See `references/source-of-truth.md`.

## Final quality check

Before finishing, confirm:

- no security control was weakened;
- no secret was introduced into code/logs/output;
- no unbounded loop/retry/pagination/upload/query was added;
- no race-sensitive invariant relies only on application code;
- network calls have bounded behavior;
- persistent schema changes have a safe migration path;
- errors are observable without leaking internals;
- the change can be rolled back or safely forward-fixed;
- important claims are supported by code, tests, or authoritative documentation.
