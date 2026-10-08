# Production Readiness Checklist

Mark each item as `PASS`, `FAIL`, `N/A`, or `UNKNOWN`.

## Security

- [ ] Server-side input validation exists for untrusted input.
- [ ] Authentication is enforced where required.
- [ ] Object-level authorization is enforced.
- [ ] Function/role-level authorization is enforced.
- [ ] Secrets are not committed or logged.
- [ ] Password storage uses a proper password hashing function.
- [ ] SQL/query construction is injection-safe.
- [ ] TLS is used for sensitive production traffic.
- [ ] Debug/admin/metrics/profiling exposure is controlled.
- [ ] High-risk operations are auditable when required.

## API and abuse resistance

- [ ] Request body/upload/batch sizes are bounded.
- [ ] Pagination/query complexity is bounded.
- [ ] Abuse-prone endpoints are rate/usage limited.
- [ ] Critical writes are duplicate-safe/idempotent.
- [ ] Breaking contract changes have a compatibility/versioning plan.
- [ ] Client-facing errors do not leak internals.

## Data integrity

- [ ] Critical invariants are enforced by database constraints where possible.
- [ ] Multi-step atomic operations use transactions.
- [ ] Concurrency/race conditions were considered for important writes.
- [ ] Connection pools are bounded.
- [ ] Important queries have appropriate indexes/query behavior.
- [ ] Deletion/cascade/retention behavior is intentional.

## Migrations

- [ ] Schema changes are versioned migrations.
- [ ] Migration is compatible with the rollout strategy.
- [ ] Large backfills/DDL impact is understood.
- [ ] Rollback or forward-fix path is defined.

## Dependencies and networking

- [ ] External calls have timeouts/deadlines.
- [ ] Retries are bounded and only used for safe/retryable failures.
- [ ] Backoff/jitter is used where retry synchronization could be harmful.
- [ ] Retry multiplication across layers is controlled.
- [ ] External side effects are idempotent or deduplicated.

## Workers, queues, webhooks

- [ ] Consumers tolerate duplicate delivery.
- [ ] Worker concurrency is bounded.
- [ ] Retry limits exist.
- [ ] Poison jobs/messages have an inspection/recovery path.
- [ ] Webhook authenticity is verified where supported.
- [ ] Out-of-order/duplicate webhook behavior is handled.

## Observability

- [ ] Production logs are structured.
- [ ] Request ID/trace context exists for important flows.
- [ ] Sensitive data is redacted from logs.
- [ ] Latency, traffic, errors, and saturation are measurable.
- [ ] Alerts are actionable/user-impact oriented.
- [ ] Running version/commit is discoverable.

## Lifecycle and runtime

- [ ] Graceful shutdown is implemented.
- [ ] Readiness behavior prevents traffic to unavailable instances.
- [ ] Liveness checks do not create restart storms.
- [ ] Startup checks exist when slow startup requires them.
- [ ] Shared durable state is not kept only on ephemeral local disk.
- [ ] Runtime resource usage/concurrency is bounded.

## Configuration and release

- [ ] Production config is externalized and validated.
- [ ] Production-safe defaults are used.
- [ ] Build/release is traceable to an artifact and commit.
- [ ] Repeatable deploy steps are automated/documented.
- [ ] Post-deploy verification exists.
- [ ] Rollback or safe forward-fix is documented/tested.

## Backup and recovery

- [ ] Critical data is backed up automatically.
- [ ] Backups are protected appropriately.
- [ ] Restore has been tested.
- [ ] Restored data integrity was validated.
- [ ] RPO/RTO are known for important workloads where required.
- [ ] Recovery/runbook ownership is clear.

## Final gate

A service should normally be `NOT READY` when any applicable non-negotiable security, data-integrity, duplicate-side-effect, timeout, migration-safety, rollback, or recovery item is `FAIL`.

`UNKNOWN` on a high-risk item must be treated as unresolved, not silently assumed to pass.
