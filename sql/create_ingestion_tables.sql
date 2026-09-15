-- Normalized survey ingestion tables

CREATE TABLE IF NOT EXISTS survey_questions (
    survey_id STRING,
    page_number INT,
    question_id STRING,
    question_text STRING,
    question_type STRING,
    field_id STRING,
    field_label STRING,
    field_type STRING,
    discovered_at TIMESTAMP
) USING DELTA;

CREATE TABLE IF NOT EXISTS survey_response_headers (
    survey_id STRING,
    response_id STRING,
    response_unique_id STRING,
    response_status STRING,
    start_date STRING,
    end_date STRING,
    language STRING,
    time_taken STRING,
    collector_id STRING,
    ingested_at TIMESTAMP
) USING DELTA;

CREATE TABLE IF NOT EXISTS survey_answers (
    survey_id STRING,
    response_id STRING,
    page_number INT,
    question_id STRING,
    field_id STRING,
    answer STRING,
    score DOUBLE,
    score_total DOUBLE,
    skipped_by_logic BOOLEAN,
    ingested_at TIMESTAMP
) USING DELTA;
