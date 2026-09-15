"""Incremental response-window and duplicate-filtering helpers."""

from datetime import date, datetime, timedelta
from typing import Any, Iterable, Mapping, Optional, Sequence


def build_response_window(
    today: date,
    last_response_checked_at: Optional[datetime] = None,
    last_ingested_at: Optional[datetime] = None,
    source_response_count: Optional[int] = None,
    activity_changed: bool = False,
    initial_lookback_days: int = 30,
    overlap_days: int = 1,
) -> Optional[dict[str, date]]:
    """Build a bounded extraction window for a survey requiring a response check."""

    never_checked_with_responses = (
        last_response_checked_at is None
        and source_response_count is not None
        and int(source_response_count) > 0
    )

    if not (activity_changed or never_checked_with_responses):
        return None

    if last_response_checked_at is not None:
        start_date = (
            last_response_checked_at.date()
            - timedelta(days=overlap_days)
        )
    elif last_ingested_at is not None:
        start_date = (
            last_ingested_at.date()
            - timedelta(days=overlap_days)
        )
    else:
        start_date = today - timedelta(days=initial_lookback_days)

    return {"from_date": start_date, "to_date": today}


def unseen_response_keys(
    discovered: Iterable[Mapping[str, Any]],
    existing: Sequence[tuple[str, str]],
) -> list[Mapping[str, Any]]:
    """Return discovered responses whose survey/response key is not persisted."""

    existing_keys = {
        (str(survey_id), str(response_id))
        for survey_id, response_id in existing
    }

    return [
        row
        for row in discovered
        if (
            str(row["survey_id"]),
            str(row["response_id"]),
        )
        not in existing_keys
    ]
