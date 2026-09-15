\# Architecture Diagram



The following diagram represents the sanitized production architecture of the

metadata-driven survey ingestion framework.


```mermaid
flowchart TB

    subgraph ORCH["1. Orchestration Layer"]
        A["Microsoft Fabric<br/>Data Pipeline"]
        B["Fabric Notebook<br/>Python Orchestration"]
        A --> B
    end

    subgraph SEC["2. Authentication & Source"]
        C["Azure Key Vault<br/>OAuth Credentials"]
        D["Zoho Survey<br/>REST API"]
    end

    subgraph CTRL["3. Metadata & Incremental Control"]
        E["Metadata Registry<br/>Departments & Surveys"]
        F["Change Detection<br/>Response Windows & Checkpoints"]
        G["Response Discovery<br/>Detail Extraction"]
        E --> F
        F --> G
    end

    subgraph STORE["4. Delta Lakehouse"]
        H[("Delta Lakehouse")]
        I["Survey Questions"]
        J["Response Headers"]
        K["Survey Answers"]
        L["Ingestion Run Log<br/>Health Views"]

        H --> I
        H --> J
        H --> K
        H --> L
    end

    C --> B
    B --> D
    B --> E
    D --> F
    G --> D
    G --> H
    E --> H
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

