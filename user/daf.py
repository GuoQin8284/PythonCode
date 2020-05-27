import json

# with open("./data/db.json", mode="r+", encoding="utf-8") as f:
#     dbContent = json.load(f)
#     print(type(dbContent))
#     print(dbContent is None)
#     print(dbContent)
#     # json.load(dbContent)
with open("./data/db.json", mode="r+", encoding="utf-8") as f:
    dbContent = json.load(f)
    print(type(dbContent))
    print(dbContent is None)
    if dbContent is None:
        print("当前没有创建数据库")
    else:
        sql_list = dbContent.get("sql")
        if len(sql_list):
            print(sql_list)
            dbNamelist = sql_list[-1]
            dbNameKey = list(dbNamelist.items())[0][0]
            # dbNameKey1=dbNameKey[0][0]
            print(type(dbNameKey))
            print("self.dbNameKey:", dbNameKey)
#             sql.e/me", self.tbName)