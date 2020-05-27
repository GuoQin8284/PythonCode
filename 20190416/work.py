# #   1.	定义两个列表：list1 = ['life','is','short'],   list2 = ['you','need','python']，完成如下操作：
#
#
# # 1)	输出python及其下标
# list2 = ['you','need','python']
# print('%s\t 其下标为：%d'% (list2[list2.index('python')],list2.index('python')))
#
# #  2)	在list1的’is’后添加元素’so’，在list2的’you’后添加’really’
# list1 = ['life','is','short']
# list2 = ['you','need','python']
# list1.insert(2,'so')
# list2.insert(1,'really')
# print('%s'% list1)
# print('%s'% list2)
#
# #  3)	将两个列表合并后，排序并输出其长度
# list1.extend(list2)
# list1.sort()
# b = len(list1)
# print('%s \n%s'%(list1,b) )
#
#
# # 4)	将list2中的 'python' 改为 'python3'
# list2[3]='python3'
# print(list2)
#
# # 5)	移除之前添加的‘so’和’really’
#
# list1.pop(2)
# list2.pop(1)
# print(list1,"\n ",list2)


#  2.	先定义一个空列表，通过for循环，使用随机数（数据范围1-100）的生成办法，向列表中添加10个随机整数。累加和
def im_list():
    nun = []
    import random
    b = 0
    for i in range(10):
        a = random.randint(1, 100)
        b += a
        nun.append(a)

    return nun
    # print('列表为：%s \n累加和为：%d' % (nun, b))


# im_list()

# #  3.	在一个拥有10个随机整数的列表中，查找某个整数是否出现，如果有显示该值的索引；若未出现，显示“数据未出现”的提示。
# 进阶要求：
# 			若数据多次出现，应打印每个数的索引

#
# c = im_list()
# print(c)
# x = int(input ('请输入正整数：'))
# i = 0
# e = 1
# for d in c:
#     if c.count(x):
#         if x == c[i]:
#             print('%d第%d次出现，索引值为：%d' % (x,e,i))
#             e += 1
#         i += 1
#     else:
#         print('数据未出现')
#         break

# print('%d'% len('12343'))

a = (1,2,3,4)
print(a)







