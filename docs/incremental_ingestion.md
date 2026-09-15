# Incremental ingestion

Source modification/activity metadata is compared with persisted registry state. Response checks use a checkpoint overlap, unseen response keys are selected before detail calls, and Delta MERGE provides idempotent persistence. The initial path uses a 30-day lookback and is not presented as full historical backfill.
