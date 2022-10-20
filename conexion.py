from xmlrpc.client import _HostType
import psycopg2

conn = psycopg2.connect(Host='localhost',
                        user = 'postgres',
                        password= 'abcd1234')

cur = conn.cursor()

cur.execute('select * from persona')

print(cur.fetchone())

