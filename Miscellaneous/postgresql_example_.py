import psycopg2
import sys
connection = psycopg2.connect(host="localhost", database='postgres', user='postgres', password='arundhuti2003')
cursor = connection.cursor()
# cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
connection.commit()
cursor.execute("INSERT INTO test (num, data) VALUES (%s, %s)",(100, "abc'def"))
connection.commit()
f=cursor.execute("SELECT * FROM test;")
connection.commit()
cursor.copy_to(sys.stdout,'test',sep = '\t')
