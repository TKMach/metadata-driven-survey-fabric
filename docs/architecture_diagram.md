\# Architecture Diagram



The following diagram represents the sanitized production architecture of the

metadata-driven survey ingestion framework.



```mermaid

flowchart LR



&#x20;   A\[Microsoft Fabric<br/>Data Pipeline]



&#x20;   B\[Fabric Notebook<br/>Python Orchestration]



&#x20;   C\[Azure Key Vault<br/>OAuth Credentials]



&#x20;   D\[Zoho Survey<br/>REST API]



&#x20;   E\[Metadata Registry<br/>Departments \& Surveys]



&#x20;   F\[Change Detection<br/>\& Response Windows]



&#x20;   G\[Response Discovery<br/>\& Detail Extraction]



&#x20;   H\[(Delta Lakehouse)]



&#x20;   I\[Survey Questions]

&#x20;   J\[Response Headers]

&#x20;   K\[Survey Answers]

&#x20;   L\[Ingestion Run Log<br/>\& Health Views]



&#x20;   A --> B



&#x20;   C --> B

&#x20;   B --> D



&#x20;   B --> E

&#x20;   E --> F



&#x20;   D --> F

&#x20;   F --> G

&#x20;   G --> D



&#x20;   G --> H

&#x20;   E --> H



&#x20;   H --> I

&#x20;   H --> J

&#x20;   H --> K

&#x20;   H --> L

```



\## Processing flow



The Fabric pipeline triggers the ingestion notebook. Authentication credentials

are retrieved securely from Azure Key Vault and used to obtain access to the

Zoho Survey REST API.



The framework uses metadata registries to identify active surveys and detect

source activity. Incremental response windows are calculated from ingestion

checkpoints, after which new response identifiers are discovered and response

details are extracted.



The resulting data is persisted into normalized Delta Lakehouse structures for

survey metadata, questions, response headers, answers, and operational

monitoring.



Production identifiers, credentials, organizational names, survey responses,

and other sensitive information are intentionally excluded from this public

architecture.

