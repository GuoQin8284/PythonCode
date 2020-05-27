import datetime
import re


import pymysql

startTime="startTime:{}".format(datetime.datetime.today())
db = pymysql.connect("127.0.0.1","root","root")

show_databases="show databases"
use="use test"
select = "select * from stu"
cursor=db.cursor()
# cursor.execute(show_databases)
# insert="insert into stu values(005,'hehe','20','612.56')"
desc="desc stu"
# print(cursor.fetchall())
def execute(info,button=False):
    cursor.execute(info)
    db.commit()
    a=cursor.fetchall()
    if button:
        printAll()
        endTime=datetime.datetime.today()


        print("startTime:",startTime)
        print("endTime:",endTime)
    return a
def printAll():
    info = execute(select)
    values=""
    for i in range(len(info)):
        content=info[i]
        content1="id：{}\t姓名：{}\t年龄：{}\t身高：{}\n".format(content[0],content[1],content[2],content[3])
        values=values+content1
        print(content1)
    with open("./stu.txt", "w", encoding="utf-8") as f:
        f.write(values)
execute(use)
execute(desc)
# execute(select)
# execute(desc)
# execute(insert)
# db.close()
try:
    num=1
    commit_num=2
    values=''
    info = execute(select)[-1]
    id = info[0]
    n=0
    for i in range(num):
        id1=id+1
        content="(null ,'he{}',{},{}),".format(str(id1),20+id1,100.56+id1)
        values = values+content
        # print("valunes:",values)
        id += 1
        # print(n)
        if n==commit_num or i==num-1:
            values1 = values[0:-1:]
            insert = "insert into stu values{}".format(values1)
            if i==num-1:
                button = True
                execute(insert, button)
                break
            execute(insert)
            print(123)
            n=0
            continue
        n += 1
except pymysql.err.DataError:
    name=execute(desc)[1]
    varchar=name[1]
    varchar1=int(re.findall(r"\d+",varchar)[0])+1
    # print("varchar1:",varchar1)
    update="alter table stu change name name varchar({}) not null".format(varchar1)
    execute(update)
    raise
