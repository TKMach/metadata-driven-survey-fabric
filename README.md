# Metadata-Driven Survey API Ingestion Framework on Microsoft Fabric

A sanitized portfolio implementation of a metadata-driven framework that extracts
Zoho Survey data through REST APIs and loads normalized Delta tables into a
Microsoft Fabric Lakehouse.

## Problem

A growing survey estate creates several engineering challenges: surveys can have
different question structures, new surveys can appear over time, repeatedly
extracting every response is inefficient, and operational teams need visibility
into whether ingestion completed successfully.

## Engineering solution

The framework uses registry metadata to determine which surveys require work.
Microsoft Fabric orchestrates the ingestion workload, OAuth credentials are
supplied securely at runtime, source metadata is compared with stored state,
response extraction uses checkpoint-based windows, and normalized results are
persisted to Delta tables.

This allows one ingestion pattern to support multiple surveys without building a
new pipeline and wide destination table for every survey.

## Result

The resulting design provides:

- metadata-driven multi-survey ingestion
- source change detection
- incremental response discovery
- duplicate protection using source response identifiers
- normalized question, response-header, and answer storage
- support for simple, compound, and matrix-style answers
- operational run logging and health monitoring
- separation of credentials and production identifiers from source code

## Architecture

```text
Microsoft Fabric Pipeline
          |
          v
Ingestion Notebook / Python Modules
          |
          +------ Secret Provider ------> OAuth Token
          |
          +------ Metadata Registry
          |            |
          |            v
          +------ Zoho Survey REST API
                         |
                  JSON / metadata
                         |
                         v
                   Delta Lakehouse
                 /       |        \
          Questions   Headers    Answers
                         |
                         v
                 Run Log / Monitoring
```

## Incremental ingestion

The registry stores source activity metadata and ingestion checkpoints. Surveys
showing new activity are selected for response discovery. The response window
overlaps the previous checkpoint to reduce boundary risk, and existing
`(survey_id, response_id)` keys are excluded before response-detail extraction.

The initial no-checkpoint path uses a bounded lookback. The repository does not
claim complete historical backfill or endpoint pagination unless those
capabilities are explicitly implemented.

## Data model

```text
department_registry
        |
        | 1:M
        v
survey_registry
    |          |
    | 1:M      | 1:M
    v          v
survey_questions    survey_response_headers
                              |
                              | 1:M
                              v
                         survey_answers
```

See `docs/data_model.md` and the SQL definitions under `sql/`.

## Repository structure

```text
config/       Safe configuration template
docs/         Architecture, model, incremental loading, security, monitoring
notebooks/    Sanitized Fabric orchestration example
src/          API, metadata, ingestion, parsing, and monitoring modules
sql/          Delta table definitions and monitoring view
tests/        Unit tests for deterministic business logic
```

## Architecture evolution

The original proof of concept used webhook-based ingestion through an
intermediary. The current design uses direct REST API extraction orchestrated by
Microsoft Fabric, reducing external dependencies and enabling metadata-driven
multi-survey ingestion, checkpoints, and operational monitoring.

## Security

Production workspace and lakehouse identifiers, Key Vault names, portal IDs,
credentials, tokens, organization-specific values, participant records, and IP
addresses are excluded. See `docs/security.md`.

## Current limitations

- initial ingestion uses a bounded lookback rather than a complete backfill
- pagination is not claimed until implemented for the relevant API endpoints
- retry/backoff beyond authentication retry remains an improvement area
- the public notebook is an orchestration example, not a production export

## Future improvements

- API pagination where required
- configurable historical backfill
- retry/backoff for throttling and transient server errors
- failed-record quarantine/dead-letter handling
- CI/CD and automated Microsoft Fabric deployment
- broader Spark and integration tests

## Portfolio note

This repository is a deliberately sanitized and modularized representation of
an implemented Microsoft Fabric ingestion pattern. It demonstrates engineering
decisions and reusable design without exposing production data or credentials.
