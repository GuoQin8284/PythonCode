import re

import time

from driver.driver import SetupDriver


driver = SetupDriver().setupDriver()


driver.start_activity("com.singxie.btdownload","com.singxie.btdownload.MainActivity")

n = 0
while True:
    item1 = driver.find_elements_by_id("com.singxie.btdownload:id/task_title")
    item2 = driver.find_elements_by_id("com.singxie.btdownload:id/task_msg")
    item3 = driver.find_elements_by_id("com.singxie.btdownload:id/posterImg")
    i = 0
    textList = []
    a = False
    for m in item2:
        textValue = m.text.replace("\n","").replace(" ","")
        textList.append(textValue)
        if "下载" in textValue:
            a = True
    for e in textList:
        if "已暂停" in textValue:
            print(str(int(i)+1)+r"."+item1[i].text+"/s的下载状态："+textValue)
            if a is False:
                item3[i].click()
                print("已点击")
                time.sleep(5)
                break
        else:
            downloadSpend = re.findall(r"正在下载  (.*?) M /s",textValue)
            print(str(int(i)+1)+r"."+item1[i].text+"/s的下载状态："+textValue)
            if downloadSpend:
                n = 0
            elif downloadSpend is False and n < 50:
                n += 1
            elif downloadSpend is False and n >= 50:
                print(item1[i].text + "\s任务的下载速度为0，正在重启")
                item3[i].click()
                time.sleep(5)
                item3[i].click()
                print(item1[i].text + "已完成重启")
        i += 1
    print("本次循环结束")
# a = r"正在下载  3.0 M /s"
# print(re.findall(r"正在下载  (.*?) M /s",a)[0])