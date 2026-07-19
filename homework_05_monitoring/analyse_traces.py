import sqlite3
import pandas as pd

conn = sqlite3.connect("traces.db")

df = pd.read_sql_query("""
SELECT
    name,
    input_tokens,
    output_tokens
FROM spans
WHERE name = 'llm'
""", conn)

conn.close()

print(df)

print("\nInput tokens:")
print(df["input_tokens"])

print("\nStatistics:")
print(df["input_tokens"].describe())