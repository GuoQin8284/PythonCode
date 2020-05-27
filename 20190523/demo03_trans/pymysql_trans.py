import pymysql

conn=pymysql.Connect(host="127.0.0.1",port=3306,database="books",user="root",password="root",charset="utf8")

cursor=conn.cursor()
try:
    sql="insert into t_book values(null,'三国演义','1990-10-01',50,80,0)"

    cursor.execute(sql)

    sql2="insert into t_hero values(null,'诸葛亮',1,'足智多谋',0,5)"

    cursor.execute(sql2)

except Exception as f:
    print(f)
    conn.rollback()

else:
    conn.commit()

finally:
    cursor.close()
    conn.close()