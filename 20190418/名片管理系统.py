card = {}
list_card = []
card_1=dict
def input_card() :
    global list_card
    name = input('请输入姓名：')
    tel = input('请输入电话：')
    qq = input('请输入qq：')
    email = input('请输入邮箱：')
    if name.isalnum() or tel.isalnum() or qq.isalnum() or email.isalnum():
        card = {'id':len(list_card)+1,'姓名':name,'电话':tel,'qq':qq,'email':email}
        list_card.append(card)
def show_list():
    little=["id","姓名","电话","qq","email"]
    i = 0
    for little_str in little:
        print(little_str.ljust(20),end='')
    for card_2 in list_card:
        def b():
            if i == 0 :
                return '\n'
            else:
                return ''
        print(b(),(str (card_2['id'])).ljust(19),card_2['姓名'].ljust(21),card_2['电话'].ljust(20),card_2['qq'].ljust(20),card_2['email'])
        i += 1
def xiugai():
    global list_card,card_1
    print("1.修改名片\n2.删除名片")
    ch_del = int(input('请输入数字选择：'))
    if ch_del == 2:
        list_card.remove(card_1)
        print('已删除')
    elif ch_del == 1:
        a = input('请输入新的姓名(Enter跳过)：')
        if a == '':
            pass
        else:
            card_1['姓名'] = a
        b = input('请输入新的电话(Enter跳过)：')
        if b == '':
            pass
        else:
            card_1['电话'] = b
        c = input('请输入新的qq(Enter跳过)：')
        if c == '':
            pass
        else:
            card_1['qq'] = c
        d = input('请输入新的邮箱(Enter跳过)：')
        if d == '':
            pass
        else:
            card_1['email'] = d
        print(list_card)
def ch_list():
    i = 0
    global list_card,card_1
    xh = []
    name_1=input('请输入要修改的姓名：')
    for card_1 in list_card:
        if name_1 ==card_1['姓名']:
            xh.append(list_card.index(card_1,i))
            i += 1
    if i >1:
        print('系统中共查询到%d个同名，请选择序号'% i)
        for xh_src in xh:
            print(xh_src,list_card[xh_src])
        xid = int(input())
        print(i)
        print('序号为：%s'% xh)
        card_1=list_card[xh.index(xid)]
        xiugai()
    elif i ==1:
        xiugai()
    elif i ==0:
        print('没有查询到该姓名，请重新输入')
xing_hao='*'*50
little='欢迎使用【名片管理系统】V1.0'
mingpian='1.新建名片'
show1='2.显示全部'
cha='3.查询名片'
tui='0.退出系统'
def show():
    print(xing_hao,'\n',little, '\n\n', mingpian, '\n',show1,'\n', cha, '\n\n', tui, '\n', xing_hao)
xu=int
e = ''
def shu():
    global xu
    xu = input('请输入：')
    e = xu
    if e.isdecimal()==False:
        show()
        print('错误请重新输入')
        shu()
    return xu
show()
shu()
i = 1
while i != 0:
    if int(xu) == 1:
        input_card()
        show()
        shu()
    elif int(xu) == 2:
        if len(list_card)==0:
            show()
            print('还没有新建过名片，请返回新建名片')
            shu()
        else:
            show_list()
            print('1.编辑名片','2.返回','3.退出系统')
            shu()
            if int(xu)==1:
                ch_list()
            elif int(xu)==2:
                show()
                shu()
            elif int(xu)==3:
                print("已退出系统")
                print("输入“5”登入系统")
                shu()
    elif int(xu)  == 3:
        if len(list_card)==0:
            show()
            print('还没有新建过名片，请返回新建名片')
            print('1.返回','2.退出系统')
            shu()
            if int(xu) ==1:
                show()
                shu()
            elif int(xu)==2:
                print("已退出系统")
                print("输入“5”登入系统")
                shu()
        else:
            ch_list()
            show()
            shu()
    elif int(xu)  == 0:
        print("已退出系统")
        print("输入“5”登入系统")
        shu()
    elif int(xu) ==5:
        show()
        shu()
    else:
        show()
        print("输入错误")
        shu()


