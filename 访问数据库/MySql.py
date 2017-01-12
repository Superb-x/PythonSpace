import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='lxl')
cursor = conn.cursor()
#创建user表
cursor.execute('create table user (id VARCHAR (20) PRIMARY KEY, name VARCHAR (20))')
#插入一行记录,注意MySql的占位符是%s
name = ['liuxianglin', 'zhuyuan', 'wangshengkai', 'xiehuan', 'hukunyu', 'fangyue', 'yanghao']
for x in range(len(name)):
    cursor.execute('insert into user (id, name) values (%s, %s)', [x, name[x]])
print(cursor.rowcount)
conn.commit()
cursor.close()
