import duckdb

con = duckdb.connect("logfire_traces.duckdb")

tables = con.sql("""
SELECT table_name
FROM information_schema.tables
WHERE table_schema='agent_traces'
ORDER BY table_name
""").fetchall()

print(f"Number of tables: {len(tables)}")
print()

for t in tables:
    print(t[0])