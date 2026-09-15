# Data model

```text
department_registry 1 -- * survey_registry
                         |-- * survey_questions
                         |-- * survey_response_headers 1 -- * survey_answers
```
