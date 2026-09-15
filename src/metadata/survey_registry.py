"""Change-detection rules for survey registry metadata."""

from typing import Any, Mapping, Optional


def question_metadata_changed(
    latest: Mapping[str, Any],
    previous: Optional[Mapping[str, Any]],
) -> bool:
    """Return True when question metadata should be refreshed."""
    if previous is None:
        return True

    return (
        latest.get("source_modified_date")
        != previous.get("source_modified_date")
    )


def response_activity_changed(
    latest: Mapping[str, Any],
    previous: Optional[Mapping[str, Any]],
) -> bool:
    """Return True when source metadata indicates response activity."""
    if previous is None:
        return True

    return (
        latest.get("source_last_response_date")
        != previous.get("source_last_response_date")
        or latest.get("source_response_count")
        != previous.get("source_response_count")
    )
