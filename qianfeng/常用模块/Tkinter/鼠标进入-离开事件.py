import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")

# <Enter> 鼠标光标进入控件时候触发
# <Leave> 鼠标光标离开控件时候触发
label = tkinter.Label(win,text='he jiao long is a good man',bg='yellow')
label.pack()

def func(event):
	print(event.x)

label.bind('<Leave>',func)


# 进入消息循环
win.mainloop()


