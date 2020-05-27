import pymysql

conn = pymysql.Connect(host="127.0.0.1",port=3306,database="books",user="root",password="root",charset="utf8")

cursor=conn.cursor()

sql_insert="insert into t_book values(null,'西游记','1970-07-24','38','57',0)"

cursor.execute(sql_insert)

conn.commit()

print("响应结果行数",cursor.rowcount)

rows=cursor.fetchall()

cursor.close()
conn.close()