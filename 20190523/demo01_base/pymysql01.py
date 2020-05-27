import pymysql

conn = pymysql.Connect(host="127.0.0.1",port=3306,database="books",user="root",password="root")

cursor=conn.cursor()





cursor.close()
conn.close()