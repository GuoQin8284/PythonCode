# pymysql的使用步骤

import pymysql
# 导包

url = "127.0.0.1"
port = 3306
user = "root"
pwd = "root"
connect = pymysql.connect(host = url,port = port,user = user,password = pwd,charset = "utf8")
print(connect)
#创建连接

cursor = connect.cursor()
print(cursor)
#创建游标对象

sql1 = "use books;"
sql2 = "select * from t_book;"
cursor.execute(sql1)
cursor.execute(sql2)
response = cursor.fetchall()
print(type(response))
print("response:",response)
for i in range(len(response)):
    print(response[i])
# 发送sql语句

cursor.close()
connect.close()
# 关闭连接



