"""dlt pipeline: pull Pydantic Logfire traces into DuckDB (homework Q2).

Uses the Logfire read/query API (https://logfire-us.pydantic.dev/v2/query) as a
REST source. A single `SELECT * FROM records` returns all spans/traces; each
record carries deeply nested JSON (`attributes` with LLM messages / tool calls /
token usage, plus `otel_events`, `otel_links`, `*_attributes`, ...). dlt
normalizes these into a root `records` table plus one child table per nested
level, all in the `agent_traces` schema.

Auth: the Logfire *read* token is taken from the LOGFIRE_READ_TOKEN env var
(loaded from homework/.env). The token value is never printed.

Run from the workshop root so dlt finds the .dlt workspace:
    uv run python homework/logfire_pipeline.py
"""

import os
from pathlib import Path

import dlt
from dlt.sources.rest_api import RESTAPIConfig, rest_api_resources
from dotenv import load_dotenv

# Load homework/.env regardless of the current working directory.
load_dotenv(Path(__file__).with_name(".env"))

# US region confirmed for this project's read token; override via env if needed.
LOGFIRE_BASE_URL = os.environ.get("LOGFIRE_BASE_URL", "https://logfire-eu.pydantic.dev")
# Wide lower bound so we capture every historical trace (API requires min_timestamp).
MIN_TIMESTAMP = "2024-01-01T00:00:00+00:00"
QUERY = "SELECT * FROM records"


@dlt.source(name="agent_traces")
def logfire_source(read_token: str = None):
    """REST source over the Logfire query API. Loads all `records` rows."""
    token = read_token or os.environ["LOGFIRE_READ_TOKEN"]
    config: RESTAPIConfig = {
        "client": {
            "base_url": LOGFIRE_BASE_URL,
            "headers": {"Accept": "application/json"},
            "auth": {"type": "bearer", "token": token},
            # Query API returns the whole result set in one response body.
            "paginator": "single_page",
        },
        "resources": [
            {
                "name": "records",
                "primary_key": "span_id",
                "write_disposition": "replace",
                "endpoint": {
                    "path": "v2/query",
                    "method": "POST",
                    "json": {"sql": QUERY, "min_timestamp": MIN_TIMESTAMP},
                    "data_selector": "data",  # response is {"schema": ..., "data": [...]}
                },
            },
        ],
    }
    yield from rest_api_resources(config)


def load_agent_traces() -> None:
    pipeline = dlt.pipeline(
        pipeline_name="logfire_traces",
        destination="duckdb",
        dataset_name="agent_traces",
    )
    load_info = pipeline.run(logfire_source())
    print(load_info)
    print(pipeline.last_trace.last_normalize_info)


if __name__ == "__main__":
    load_agent_traces()
