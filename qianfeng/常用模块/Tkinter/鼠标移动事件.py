import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")


# <Bl-Motion>鼠标左键按住移动
# <B2-Motion>鼠标中键按住移动
# <B3-Motion>鼠标右键按住移动
label = tkinter.Label(win,text='he jiao long is a good man')
label.pack()

def func(event):
	print(event.x)

label.bind('<B2-Motion>',func)


# 进入消息循环
win.mainloop()


