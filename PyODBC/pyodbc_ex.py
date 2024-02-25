import pyodbc

# Connect to the Databricks cluster by using the
# Data Source Name (DSN) that you created earlier.
conn = pyodbc.connect("DSN=<dsn-name>", autocommit=True)

# Run a SQL query by using the preceding connection.
cursor = conn.cursor()
cursor.execute(f"SELECT * FROM samples.nyctaxi.trips")

# Print the rows retrieved from the query.
for row in cursor.fetchall():
  print(row)
