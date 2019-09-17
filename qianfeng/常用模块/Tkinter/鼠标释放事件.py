import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")

# <ButtonRelease-1>释放鼠标左键
# <ButtonRelease-2>释放鼠标中键
# <ButtonRelease-3>释放鼠标右键
label = tkinter.Label(win,text='he jiao long is a good man',bg='red')
label.pack()

def func(event):
	print(event.x)

label.bind('<ButtonRelease-1>',func)


# 进入消息循环
win.mainloop()


