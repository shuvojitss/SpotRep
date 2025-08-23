import sqlite3

# Connect to the database
conn = sqlite3.connect("issues.db")
cursor = conn.cursor()

# Delete the row with id = 7
cursor.execute("DELETE FROM issues WHERE id = 7")

# Commit and close
conn.commit()
conn.close()