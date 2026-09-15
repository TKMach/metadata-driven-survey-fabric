from src.metadata.survey_registry import (
    question_metadata_changed,
    response_activity_changed,
)


def test_new_survey_requires_question_refresh():
    assert question_metadata_changed(
        {"source_modified_date": "2026-09-15"},
        None,
    )


def test_unchanged_question_metadata_does_not_refresh():
    latest = {"source_modified_date": "2026-09-15"}
    previous = {"source_modified_date": "2026-09-15"}
    assert not question_metadata_changed(latest, previous)


def test_response_count_change_indicates_activity():
    latest = {
        "source_last_response_date": "2026-09-15",
        "source_response_count": 11,
    }
    previous = {
        "source_last_response_date": "2026-09-15",
        "source_response_count": 10,
    }
    assert response_activity_changed(latest, previous)
