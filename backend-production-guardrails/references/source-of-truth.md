# Source of Truth

Use authoritative and current sources when verifying production/security behavior.

## Agent Skills format

- OpenAI Skills guide: https://developers.openai.com/api/docs/guides/tools-skills
- OpenAI plugin skills concepts: https://developers.openai.com/plugins/concepts/skills

## API and application security

- OWASP API Security Top 10: https://api-security.owasp.org/
- OWASP Cheat Sheet Series: https://cheatsheetseries.owasp.org/
- REST Security Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html
- SQL Injection Prevention Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
- Password Storage Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html
- Secrets Management Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html
- Logging Cheat Sheet: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html

## Reliability and operations

- Google SRE — Monitoring Distributed Systems: https://sre.google/sre-book/monitoring-distributed-systems/
- AWS Builders' Library: https://aws.amazon.com/builders-library/
- AWS Well-Architected Framework: https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html
- Backup/restore verification: https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_backing_up_data_periodic_recovery_testing_data.html
- Automated testing and rollback: https://docs.aws.amazon.com/wellarchitected/latest/framework/ops_mit_deploy_risks_auto_testing_and_rollback.html

## Runtime and observability

- Kubernetes probes: https://kubernetes.io/docs/concepts/workloads/pods/probes/
- OpenTelemetry signals: https://opentelemetry.io/docs/concepts/signals/
- OpenTelemetry logs: https://opentelemetry.io/docs/concepts/signals/logs/

## Application operations

- Twelve-Factor App: https://12factor.net/
- Build, release, run: https://12factor.net/build-release-run
- Processes/statelessness: https://12factor.net/processes
- Disposability/graceful shutdown: https://12factor.net/disposability
- Dev/prod parity: https://12factor.net/dev-prod-parity

## HTTP semantics

- RFC 9110 HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110

## Database behavior

Always prefer the official documentation for the actual database/version in use.

Examples:

- PostgreSQL transactions/isolation: https://www.postgresql.org/docs/current/transaction-iso.html
- MySQL InnoDB transactions: https://dev.mysql.com/doc/refman/en/innodb-transaction-model.html

## Framework-specific behavior

When a finding depends on framework defaults, verify using the exact version's official documentation or release/security advisory.

Never assume a security default from memory when it materially affects the conclusion.
