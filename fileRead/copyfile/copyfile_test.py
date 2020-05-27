import time

import shutil

try:
    starttime=time.time()
    shutil.copyfile(r'D:\fiddler使用.wmv','./data.wmv')
    endtime=time.time()
    print("备份成功")
    print("共用时：",endtime-starttime)

except IOError as e:
    print(e)