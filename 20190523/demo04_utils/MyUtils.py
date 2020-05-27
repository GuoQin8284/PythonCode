import pymysql


class DBUtil():
    def __init__(self):
        pass

    @classmethod
    def get_conn(cls):
        conn=pymysql.Connect(host="127.0.0.1",port=3306,database="books",user="root",password="root",charset='utf8')
        return conn

    @classmethod
    def get_cursor(cls,conn):
        cursor=conn.cursor()
        return cursor

    @classmethod
    def close_res(cls,conn,cursor):
        if conn:
            conn.close()
            conn=None
        if cursor:
            cursor.close()
            cursor=None