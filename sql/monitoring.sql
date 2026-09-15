-- Run-level observability

CREATE TABLE IF NOT EXISTS survey_ingestion_run_log (
    run_id STRING,
    run_started_at TIMESTAMP,
    run_completed_at TIMESTAMP,
    departments_checked INT,
    active_surveys INT,
    survey_discovery_failures INT,
    question_metadata_failures INT,
    response_list_failures INT,
    responses_discovered INT,
    new_responses INT,
    response_detail_failures INT,
    response_headers_prepared INT,
    answer_rows_prepared INT,
    run_status STRING,
    run_duration_seconds DOUBLE
) USING DELTA;

CREATE OR REPLACE VIEW vw_ingestion_health AS
SELECT
    run_started_at,
    run_completed_at,
    active_surveys,
    responses_discovered,
    new_responses,
    run_status,
    CASE
        WHEN run_status = 'SUCCESS' THEN 'HEALTHY'
        ELSE 'WARNING'
    END AS health_status,
    run_duration_seconds
FROM survey_ingestion_run_log;
