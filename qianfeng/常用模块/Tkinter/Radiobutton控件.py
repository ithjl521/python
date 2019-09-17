import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")


def update():
	print(r.get())


# r = tkinter.IntVar()
r = tkinter.StringVar()

radio1 = tkinter.Radiobutton(win,text='one',value='good',
	variable=r,command=update)
radio1.pack()

radio2 = tkinter.Radiobutton(win,text='two',value='nice',
	variable=r,command=update)
radio2.pack()



# 进入消息循环
win.mainloop()
