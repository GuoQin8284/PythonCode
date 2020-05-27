import pymysql

conn=pymysql.Connect(host="127.0.0.1",port=3306,database="books",user='root',password='root',charset='utf8')

cursor=conn.cursor()

sql="update t_book set title='后西游记1',`read`=55 where id = 5"

cursor.execute(sql)

conn.commit()

print("响应结果行数 ",cursor.rowcount)

cursor.close()

conn.close()