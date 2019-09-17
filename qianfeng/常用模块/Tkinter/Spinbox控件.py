import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")

# 绑定变量
v = tkinter.StringVar()

def update():
	print(v.get())

'''
数值范围控件
increment 步长
values 最好不要与from_和to同时使用
command 只要值改变就会执行对应的方法
'''
sp = tkinter.Spinbox(win,from_=0,to=100,increment=5,
	textvariable=v,command=update)
# sp = tkinter.Spinbox(win,increment=5,
# 	values=(0,2,4,6,8))
sp.pack()

# 设置值
v.set(20)
# 获取值
print(v.get())


# 进入消息循环
win.mainloop()


