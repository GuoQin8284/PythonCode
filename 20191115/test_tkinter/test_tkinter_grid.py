from tkinter import *
root = Tk()
root.minsize(300,300)
root.title('超级计算器')

btn0=Button(text='0')
btn0.grid(row=3,column=2,ipadx=5,ipady=3,padx=1,pady=1)
btn1=Button(text='1')
btn1.grid(row=0,column=0,ipadx=5,ipady=3,padx=1,pady=1)
btn2=Button(text='2')
btn2.grid(row=0,column=1,ipadx=5,ipady=3,padx=1,pady=1)
btn3=Button(text='3')
btn3.grid(row=0,column=2,ipadx=5,ipady=3,padx=1,pady=1)
btn4=Button(text='4')
btn4.grid(row=1,column=0,ipadx=5,ipady=3,padx=1,pady=1)
btn5=Button(text='5')
btn5.grid(row=1,column=1,ipadx=5,ipady=3,padx=1,pady=1)
btn6=Button(text='6')
btn6.grid(row=1,column=2,ipadx=5,ipady=3,padx=1,pady=1)
btn7=Button(text='7')
btn7.grid(row=2,column=0,ipadx=5,ipady=3,padx=1,pady=1)
btn8=Button(text='8')
btn8.grid(row=2,column=1,ipadx=5,ipady=3,padx=1,pady=1)
btn9=Button(text='9')
btn9.grid(row=2,column=2,ipadx=5,ipady=3,padx=1,pady=1)
btn10=Button(text='.')
btn10.grid(row=3,column=0,ipadx=21,ipady=3,columnspan=2,padx=1,pady=1)

# subtract is "-"
# add is "+"
# multiply is "*"
# divide is "/"
subtract=Button(text='-')
subtract.grid(row=0,column=3,ipadx=5,ipady=3,padx=1,pady=1)
add=Button(text='+')
add.grid(row=1,column=3,ipadx=3,ipady=3,padx=1,pady=1)
multiply=Button(text='x')
multiply.grid(row=2,column=3,ipadx=4.5,ipady=3,padx=1,pady=1)
divide=Button(text='/')
divide.grid(row=3,column=3,ipadx=5,ipady=3,padx=1,pady=1)

# 显示窗口
getnum=Label(text="这是显示窗口位置")
getnum.grid(row=4,column=0,columnspan=4,ipadx=10,ipady=20)

root.mainloop()
