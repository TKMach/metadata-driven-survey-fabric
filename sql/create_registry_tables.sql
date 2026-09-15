-- Metadata registry tables

CREATE TABLE IF NOT EXISTS department_registry (
    dept_id STRING,
    dept_name STRING,
    portal_id STRING,
    is_active BOOLEAN,
    discovered_at TIMESTAMP,
    updated_at TIMESTAMP
) USING DELTA;

CREATE TABLE IF NOT EXISTS survey_registry (
    survey_id STRING,
    portal_id STRING,
    dept_id STRING,
    survey_name STRING,
    is_active BOOLEAN,
    discovered_at TIMESTAMP,
    updated_at TIMESTAMP,
    last_ingested_at TIMESTAMP,
    last_response_checked_at TIMESTAMP,
    source_modified_date STRING,
    source_last_response_date STRING,
    source_response_count BIGINT
) USING DELTA;
