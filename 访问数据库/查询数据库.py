import sqlite3
#我们再来查询
conn = sqlite3.connect('test.db')
cursor = conn.cursor()
#执行查询语句
cursor.execute('select * from user where id=?', ('0',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close()