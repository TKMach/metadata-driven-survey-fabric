def parse_answers(survey_id, response_id, pages, matrix_metadata=None):
    matrix_metadata, output = matrix_metadata or {}, []
    for page_number, page in enumerate(pages or [], start=1):
        for q in page.get("questions",[]) or []:
            qid = str(q["id"]) if q.get("id") is not None else None
            skipped = bool(q.get("skippedByLogic",False))
            if "answer" in q:
                score=q.get("score") or {}
                output.append({"survey_id":str(survey_id),"response_id":str(response_id),"page_number":page_number,
                    "question_id":qid,"field_id":None,"answer":None if q.get("answer") is None else str(q.get("answer")),
                    "score":score.get("score"),"score_total":score.get("total"),"skipped_by_logic":skipped})
            elif "fields" in q:
                for f in q.get("fields",[]) or []:
                    output.append({"survey_id":str(survey_id),"response_id":str(response_id),"page_number":page_number,
                        "question_id":qid,"field_id":None if f.get("id") is None else str(f.get("id")),
                        "answer":None if f.get("answer") is None else str(f.get("answer")),
                        "score":None,"score_total":None,"skipped_by_logic":skipped})
            elif "rows" in q:
                columns=matrix_metadata.get(qid,{}).get("columns",{})
                for row in q.get("rows",[]) or []:
                    selected=row.get("answer") or []
                    if not isinstance(selected,list): selected=[selected]
                    labels=[columns.get(str(x),str(x)) for x in selected]
                    output.append({"survey_id":str(survey_id),"response_id":str(response_id),"page_number":page_number,
                        "question_id":qid,"field_id":None if row.get("id") is None else str(row.get("id")),
                        "answer":", ".join(labels) if labels else None,"score":None,"score_total":None,"skipped_by_logic":skipped})
    return output
