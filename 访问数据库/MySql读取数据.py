import mysql.connector

conn = mysql.connector.connect(user='root', password='root', database='lxl')
cursor = conn.cursor()
