import duckdb

con = duckdb.connect("logfire_traces.duckdb")

result = con.sql("""
SELECT
    SUM(total) AS total_input_tokens
FROM agent_traces.records__attributes__logfire_metrics__gen_ai_client_token_usage__details
WHERE attributes__gen_ai_token_type = 'input';
""").fetchone()

print("Total input tokens:", result[0])