import tkinter

root=tkinter.Tk()
btn1=tkinter.Button(root,text="按钮1")
btn2=tkinter.Button(root,text="按钮2")
btn3=tkinter.Button(root,text='按钮3')
btn4=tkinter.Button(root,text="按钮4")
btn1.pack(side="bottom",ipadx="30",ipady=10)
btn2.pack(fill="both",expand='yes')
btn3.pack(pady=100,padx='200',side='left')
btn4.pack(ipadx=150,ipady=150)
root.mainloop()