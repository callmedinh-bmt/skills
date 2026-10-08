# Backend Production Rules — Detailed Catalog

This reference expands the non-negotiable rules in `SKILL.md`.

Use `MUST` for a production requirement unless clearly inapplicable. Use `SHOULD` for a strong default that may have justified exceptions.

## 1. Trust boundaries and input

1. **MUST** treat all client-controlled values as untrusted: body, path, query, headers, cookies, JWT claims not cryptographically verified, uploaded files, webhook payloads, filenames, redirects, and external API data.
2. **MUST** validate server-side even if the frontend validates.
3. **MUST** prefer allow-lists for enums, formats, operations, redirect destinations, sort fields, filter fields, and file types.
4. **MUST** enforce length/range/count limits before expensive processing.
5. **MUST** normalize identifiers before comparison when the domain requires canonical form.
6. **SHOULD** reject unknown fields for security-sensitive commands when silent acceptance can hide client mistakes.
7. **MUST** protect server-side URL fetchers against SSRF when clients can influence destination URLs.
8. **MUST** avoid using user-controlled filenames/paths directly for filesystem access.

## 2. Authentication, authorization, sessions

9. **MUST** separate authentication (who are you?) from authorization (may you do this?).
10. **MUST** enforce object-level authorization for resources referenced by IDs.
11. **MUST** enforce function-level authorization for admin/privileged operations.
12. **MUST** use deny-by-default for protected operations.
13. **MUST** not depend on hidden buttons/routes in the frontend for access control.
14. **MUST** validate token signature, issuer/audience/expiry as appropriate to the token design.
15. **MUST** protect refresh/session credentials more strongly than ordinary access tokens where applicable.
16. **MUST** invalidate or rotate credentials when account/session security requires it.
17. **SHOULD** record security-relevant authentication/authorization events without sensitive credential material.

## 3. Passwords, secrets, cryptography

18. **MUST** never store passwords in plaintext or encrypt them reversibly for normal authentication.
19. **MUST** use a password hashing algorithm designed for password storage; Argon2id is a strong default for new systems when available.
20. **MUST** not invent custom cryptographic schemes.
21. **MUST** keep secrets out of source control, container images, frontend bundles, build logs, and ordinary application logs.
22. **MUST** scope credentials using least privilege.
23. **SHOULD** support secret rotation without large code changes.
24. **MUST** use TLS for credentials and sensitive traffic in production.
25. **MUST** not disable certificate verification to bypass connectivity problems.

## 4. API contract and HTTP behavior

26. **MUST** use HTTP methods according to their intended semantics; safe methods must not perform hidden destructive actions.
27. **MUST** return stable status/error semantics that clients can handle.
28. **SHOULD** expose machine-readable error codes independent from human messages.
29. **MUST** not leak stack traces, SQL text, secrets, internal hostnames, filesystem paths, or private topology to clients.
30. **MUST** version or preserve compatibility for externally consumed breaking changes.
31. **MUST** bound pagination; never permit an arbitrary unbounded page size.
32. **MUST** bound request body and upload sizes.
33. **MUST** validate content type and actual file content when file security matters; do not trust filename extension alone.
34. **SHOULD** support request correlation IDs and propagate them downstream.
35. **MUST** protect sensitive or abuse-prone business flows with appropriate rate/usage limits.
36. **SHOULD** define idempotency behavior explicitly for critical POST-like commands.

## 5. SQL and database integrity

37. **MUST** use parameterized queries/prepared statements for untrusted values.
38. **MUST** enforce uniqueness in the database when uniqueness is a business invariant.
39. **MUST** use foreign keys or equivalent consistency controls where referential integrity is required and compatible with the architecture.
40. **SHOULD** use check constraints for simple invariants that belong to the data model.
41. **MUST** use transactions for multi-step state changes that must be atomic.
42. **MUST** reason about concurrent writers for balances, inventory, quotas, attempts, booking slots, sequence numbers, and state machines.
43. **MUST** not assume `SELECT -> if absent -> INSERT` is safe under concurrency without a supporting constraint/locking strategy.
44. **SHOULD** prefer atomic SQL/update conditions over read-modify-write when possible.
45. **MUST** keep transactions as short as practical.
46. **SHOULD NOT** perform slow external network calls while holding database locks unless explicitly justified.
47. **MUST** bound database connection pools.
48. **SHOULD** size pools based on database capacity and total application instances, not per-instance optimism.
49. **MUST** review query plans/indexes for high-volume or latency-sensitive queries.
50. **MUST** avoid N+1 query behavior on large collections unless bounded and acceptable.
51. **MUST** define deletion behavior: restrict, cascade, soft-delete, archive, or anonymize intentionally.

## 6. Migrations and schema evolution

52. **MUST** version schema changes in migrations under source control.
53. **MUST** avoid manual production-only schema edits as the normal workflow.
54. **MUST** consider rolling-deploy compatibility between old and new application versions.
55. **SHOULD** use expand/migrate/contract for risky breaking schema changes:
    - add compatible structure;
    - deploy code that supports both forms;
    - migrate/backfill;
    - switch reads/writes;
    - remove old structure later.
56. **MUST** understand locking/rewrite impact of large table alterations.
57. **MUST** have rollback or forward-fix strategy for data migrations.
58. **SHOULD** backfill large datasets in controlled batches instead of one giant transaction.

## 7. Idempotency and concurrency

59. **MUST** assume a client can retry after timeout even when the first request succeeded.
60. **MUST** make money movement, order creation, webhook handling, credit issuance, voucher redemption, and other irreversible side effects duplicate-safe.
61. **SHOULD** use idempotency keys or stable business keys for request deduplication when clients can safely provide/reuse them.
62. **MUST** persist the deduplication outcome when process-local memory is insufficient.
63. **MUST** protect state transitions against illegal or repeated transitions.
64. **SHOULD** use optimistic concurrency/version checks when overwrite races matter.
65. **MUST** not use a distributed lock where a simpler database constraint or atomic operation solves the invariant.

## 8. Timeouts, retries, resilience

66. **MUST** set bounded timeouts/deadlines on external calls.
67. **MUST** propagate cancellation/deadlines downstream when supported.
68. **MUST** distinguish retryable from permanent failures.
69. **MUST** bound retry attempts or total retry budget.
70. **SHOULD** use exponential backoff and jitter for distributed retry scenarios.
71. **MUST** ensure the retried operation is idempotent or otherwise duplicate-safe.
72. **MUST** not stack retries blindly across multiple layers because retry multiplication can overload dependencies.
73. **SHOULD** implement load shedding, circuit breaking, or concurrency limiting only when the observed failure mode/scale justifies it.
74. **MUST** define behavior for partial dependency outage rather than allowing requests to hang indefinitely.

## 9. Queues, workers, jobs, events

75. **MUST** assume at-least-once delivery when the messaging system can redeliver.
76. **MUST** make important consumers idempotent.
77. **MUST** bound worker concurrency.
78. **MUST** cap retry attempts for poison messages/jobs.
79. **SHOULD** use dead-letter handling or an equivalent inspection path for repeatedly failing work.
80. **MUST** understand acknowledgement/visibility timeout behavior.
81. **MUST** not acknowledge work before it is safely completed unless the loss trade-off is intentional.
82. **MUST** document ordering assumptions; do not assume global ordering unless guaranteed.
83. **SHOULD** use transactional outbox/inbox when database state and message delivery require reliable coordination across systems.
84. **MUST** make webhook consumers verify authenticity when the provider supports signed webhooks.
85. **MUST** expect duplicate and out-of-order webhooks unless the provider explicitly guarantees otherwise.

## 10. Resource limits and abuse controls

86. **MUST** bound memory/CPU-amplifying input.
87. **MUST** bound list sizes, nested input depth, query complexity, export size, and batch operation size.
88. **MUST** protect endpoints that trigger paid third-party actions such as email, SMS, AI inference, payment verification, or document processing.
89. **SHOULD** use per-user/account/IP/business-key limits according to the abuse model rather than one universal limiter.
90. **MUST** bound caches and define eviction/TTL behavior.
91. **MUST** prevent unbounded queue growth or at least alarm before capacity exhaustion.

## 11. Logging, metrics, tracing

92. **MUST** use structured logs in production for non-trivial services.
93. **MUST** include enough context to correlate a request across services.
94. **MUST** redact credentials, authorization headers, passwords, session tokens, private keys, and sensitive personal data.
95. **SHOULD** avoid full request/response body logging by default.
96. **MUST** measure errors and latency for important API operations.
97. **SHOULD** monitor the four golden signals: latency, traffic, errors, saturation.
98. **SHOULD** propagate distributed trace context across service boundaries.
99. **MUST** monitor saturation of bounded resources: CPU, memory, DB pool, queue depth, worker concurrency, file descriptors where relevant.
100. **SHOULD** alert on user impact/SLO symptoms and actionable conditions, not every infrastructure fluctuation.
101. **MUST** make deployed version/commit discoverable to operators.

## 12. Health, lifecycle, containers

102. **MUST** distinguish process liveness from traffic readiness when the platform supports those concepts.
103. **MUST** ensure readiness becomes false before an instance that cannot serve safely receives traffic.
104. **MUST** configure liveness carefully; a bad liveness probe can amplify overload by restarting healthy-but-busy instances.
105. **SHOULD** use startup probes for slow-starting applications on Kubernetes.
106. **MUST** handle SIGTERM/termination events gracefully where the runtime supports them.
107. **MUST** stop accepting new work, drain in-flight work within a deadline, then close connections and exit.
108. **MUST** avoid storing shared durable state only on local ephemeral disk in horizontally scaled systems.
109. **SHOULD** run containers as non-root where practical and reduce Linux/container privileges.
110. **MUST** set CPU/memory resource boundaries appropriate to the platform when unbounded resource use can impact neighbors.

## 13. Configuration and environment

111. **MUST** keep environment-specific configuration separate from application code.
112. **MUST** fail fast on missing/invalid required configuration instead of silently using dangerous defaults.
113. **MUST** distinguish development convenience defaults from production-safe defaults.
114. **MUST** never default production auth/security features to disabled.
115. **SHOULD** validate config schema/types at startup.
116. **MUST** know which configuration changes require restart and which can change dynamically.

## 14. CI/CD and releases

117. **MUST** identify exactly which version/commit/artifact is running.
118. **SHOULD** build once and promote the same immutable artifact through environments.
119. **MUST** automate repeatable build/test/deploy steps instead of depending on undocumented SSH/manual edits.
120. **MUST** run automated tests appropriate to change risk before release.
121. **MUST** have rollback or a well-understood forward-fix strategy.
122. **SHOULD** perform post-deploy health/smoke verification.
123. **MUST** coordinate application rollout with schema/config/secret changes.
124. **SHOULD** use progressive rollout/canary/blue-green only when risk/traffic justify the additional complexity.
125. **MUST** protect production deployment credentials and CI secrets with least privilege.

## 15. Backups and recovery

126. **MUST** identify which data cannot be recreated and back it up according to business requirements.
127. **MUST** automate backups for critical persistent data.
128. **MUST** protect backups with appropriate encryption/access controls.
129. **MUST** test restoration periodically.
130. **MUST** validate restored data, not only the existence of a backup file.
131. **SHOULD** define RPO (maximum acceptable data loss window) and RTO (maximum acceptable recovery duration) for important workloads.
132. **MUST** keep a recovery procedure/runbook for critical systems.
133. **SHOULD** exercise disaster/failover paths regularly enough to prove they still work.

## 16. Security exposure and operations

134. **MUST** restrict or authenticate debug, profiling, admin, management, metrics, and database-console endpoints.
135. **MUST** disable development debug mode in production.
136. **MUST** avoid exposing internal service errors or infrastructure details unnecessarily.
137. **MUST** maintain an inventory of externally reachable API routes/services for non-trivial systems.
138. **MUST** audit privilege changes, destructive operations, security configuration changes, and other high-risk actions when the system's risk warrants it.
139. **SHOULD** define retention for security/audit logs according to business/legal needs.
140. **MUST** not rely on CORS as authentication/authorization.

## 17. Dependencies and supply chain

141. **MUST** declare dependencies explicitly.
142. **SHOULD** use lockfiles/checksums/version pinning supported by the ecosystem for reproducible builds.
143. **MUST** scan or otherwise review known vulnerabilities in direct and transitive dependencies for production services.
144. **MUST** remove or patch vulnerable dependencies based on exploitability and risk, not CVSS alone.
145. **MUST** protect package-registry and CI credentials.
146. **SHOULD** generate/store an SBOM when organization/risk/compliance needs it.
147. **MUST** verify framework/library security behavior against current official documentation when making time-sensitive claims.

## 18. Testing expectations

148. **MUST** test authorization boundaries, not only happy-path authentication.
149. **MUST** test invalid and boundary input.
150. **MUST** test transaction rollback for important multi-write workflows.
151. **MUST** test duplicate delivery/request behavior for idempotent operations.
152. **SHOULD** test concurrent writes for race-sensitive invariants.
153. **MUST** test timeout/failure behavior for critical dependencies.
154. **SHOULD** test migrations against realistic data volume/schema state.
155. **SHOULD** test graceful shutdown/worker interruption for systems where lost work matters.
156. **MUST** not call a backend production-ready solely because unit tests pass.

## 19. Operability and ownership

157. **MUST** have a way to determine service health, recent errors, and current deployed version.
158. **MUST** have enough telemetry to investigate a failed request or job.
159. **SHOULD** document top operational procedures: deploy, rollback, restore, rotate secret, replay/requeue, disable feature/traffic if applicable.
160. **MUST** avoid single-person operational knowledge for critical production actions.
161. **SHOULD** define ownership/escalation for important services.
162. **MUST** turn repeated manual incident actions into documented or automated procedures.

## 20. Design restraint

163. **MUST** solve the actual failure mode, not add infrastructure for appearance.
164. **SHOULD** prefer local transactional guarantees over distributed coordination when both satisfy requirements.
165. **SHOULD** prefer a modular monolith over premature microservices when independent deployment/scaling/team boundaries are not required.
166. **MUST** explain the failure mode that justifies any distributed lock, queue, cache, circuit breaker, event bus, or service split.
167. **MUST** preserve simplicity because operational complexity is itself a production risk.
