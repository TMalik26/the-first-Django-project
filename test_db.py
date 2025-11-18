import psycopg
conn = psycopg.connect(
    dbname="project",
    user="project",
    password="project",
    host="localhost",
    port="5432"
)
print("Connected successfully")
conn.close()
