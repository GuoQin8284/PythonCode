import pymysql


con = pymysql.connect(host= "127.0.0.1",port = 3306 ,user = "root" , password = "root",charset = "utf8",database = "books")

consor = con.cursor()

sql = 'insert into t_book values("5","hhh","1995-5-24",12,0,1)'
consor.execute(sql)
con.commit()
print(consor.rowcount)
print(consor.rownumber)

consor.close()
con.close()