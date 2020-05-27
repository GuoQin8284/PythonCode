from demo04_utils.MyUtils import DBUtil

conn=DBUtil.get_conn()

cursor=conn.cursor()

sql="select * from t_book"

cursor.execute(sql)

rows=cursor.fetchall()

for row in rows:
    print(row)

DBUtil.close_res(conn,cursor)