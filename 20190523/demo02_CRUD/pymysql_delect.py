import pymysql

conn=pymysql.Connect(host='127.0.0.1',port=3306,database='books',user='root',password='root',charset='utf8')

cursor=conn.cursor()

sql="delete from t_book where id = 5"

cursor.execute(sql)

conn.commit()

cursor.close()
conn.close()