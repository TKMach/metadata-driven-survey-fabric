"""Helpers for deriving ingestion run health."""


def derive_run_status(
    survey_failures: int = 0,
    question_failures: int = 0,
    response_list_failures: int = 0,
    response_detail_failures: int = 0,
) -> str:
    """Return a high-level status from component failure counts."""

    total_failures = (
        survey_failures
        + question_failures
        + response_list_failures
        + response_detail_failures
    )

    return (
        "SUCCESS"
        if total_failures == 0
        else "COMPLETED_WITH_WARNINGS"
    )
