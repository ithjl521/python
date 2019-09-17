import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")

def func():
	print('hjl is a good man')

# 菜单条
menubar = tkinter.Menu(win)
win.config(menu=menubar)

# 创建菜单选项
menu1 = tkinter.Menu(menubar,tearoff=False)

# 给菜单选项添加内容
for x in ['hjl','php','java','python','c','c#',
'c++','javascript','nodejs','os','go','shell','退出']:
	if x == '退出':
		menu1.add_separator()  # 添加分割线
		menu1.add_command(label=x,command=win.quit)
	else:
		menu1.add_command(label=x,command = func)


# 向菜单条上添加菜单选择
menubar.add_cascade(label='语言',menu=menu1)	


menu2 = tkinter.Menu(menubar,tearoff=False)
menu2.add_command(label='red')
menu2.add_command(label='bule')
menubar.add_cascade(label='颜色',menu=menu2)	


# 进入消息循环
win.mainloop()


