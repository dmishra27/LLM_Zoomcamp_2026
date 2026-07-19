import sqlite3

conn = sqlite3.connect("traces.db")
cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM spans")
print("Number of spans:", cursor.fetchone()[0])

cursor.execute("SELECT * FROM spans")
rows = cursor.fetchall()

print("\nRows:")
for row in rows:
    print(row)

conn.close()