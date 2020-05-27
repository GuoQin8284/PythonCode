content=open("./dataWriteLines","w+")
list=["a\n","aaaaaa\n","!@#$%^&*()\n","哈哈哈哈哈哈\n"]
content.writelines(list)
content.seek(0)
if content.read():
    content.seek(0)
    print("写入成功")
    print(content.read())
else:
    print("写入失败")
content.close()
