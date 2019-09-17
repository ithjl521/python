import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")


def showInfo():
	print(entry.get())


entry = tkinter.Entry(win)
entry.pack()

button = tkinter.Button(win,text='按钮',command=showInfo)
button.pack()



# 进入消息循环
win.mainloop()
