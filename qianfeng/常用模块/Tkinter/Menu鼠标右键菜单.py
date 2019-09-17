import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")

# 菜单条
menubar = tkinter.Menu(win)

# 菜单
menu = tkinter.Menu(menubar,tearoff=False)
for x in ['hjl','php','java','python','c','c#',
'c++','javascript','nodejs','os','go','shell','退出']:
	
	menu.add_command(label=x)


menubar.add_cascade(label='语言',menu=menu)

def showMenu(event):
	menubar.post(event.x_root,event.y_root)

win.bind('<Button-3>',showMenu)

# 进入消息循环
win.mainloop()


