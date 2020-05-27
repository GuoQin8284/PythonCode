import pymysql

conn = pymysql.Connect(host="127.0.0.1",port=3306,database="books",user="root",password="root",charset="utf8")

cursor=conn.cursor()

sql="select * from t_book"

cursor.execute(sql)


print("响应结果行数",cursor.rowcount)

# row1=cursor.fetchone()
# print(row1)
# row2=cursor.fetchone()
# print(row2)
# row3=cursor.fetchone()
# print(row3)

rows=cursor.fetchall()

for row in rows:
    print("-"*100)
    print("id:",row[0])
    print("书名:",row[1])
    print("日期:", row[2])
    print("阅读量:", row[3])
    print("评论量:", row[4])
    print("状态:", row[5])


cursor.close()
conn.close()