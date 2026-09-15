from datetime import date, datetime
from src.ingestion.response_discovery import build_response_window, unseen_response_keys
from src.parsers.answer_parser import parse_answers
from src.metadata.survey_registry import response_activity_changed

def test_overlap_window():
    r=build_response_window(date(2026,9,15),datetime(2026,9,14,12),source_response_count=10,activity_changed=True)
    assert r["from_date"]==date(2026,9,13)

def test_unseen():
    d=[{"survey_id":"S1","response_id":"R1"},{"survey_id":"S1","response_id":"R2"}]
    assert unseen_response_keys(d,[("S1","R1")])[0]["response_id"]=="R2"

def test_matrix():
    p=[{"questions":[{"id":"Q","rows":[{"id":"R","answer":["C"]}]}]}]
    assert parse_answers("S","X",p,{"Q":{"columns":{"C":"Choice"}}})[0]["answer"]=="Choice"

def test_activity_change():
    assert response_activity_changed({"source_last_response_date":"2","source_response_count":2},{"source_last_response_date":"1","source_response_count":1})
