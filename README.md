# Metamorphic Rocks DuckDB Client

A DuckDB Client to perform analytical queries over S3 parquet files generated via the remote compactor.

Ubuntu 20.04 for a VSCode dev container.

Setup script separated that installs git, python, and pip for the dev container. May have to be modified if running elsewhere.

Requires a `.env` file with the following secrets:
```
AWS_REGION=
AWS_S3_BUCKET=

AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
```