import tkinter
root=tkinter.Tk()
root.title("这是主窗口")
w=tkinter.Label(root)
w2=tkinter.Label(root)
w2['text']='hello'
w2.config(fg='blue',bg='yellow')

w.pack(side='top')
w2.pack(side='bottom',expand='yes',fill='both')
w.config(fg="red",bg='green')
w["text"]='你好，python'
root.mainloop()