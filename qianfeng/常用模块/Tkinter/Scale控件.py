import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")

'''
供用户通过拖拽指示器改变变量的值，可以水平也可以竖直
tkinter.HORIZONTAL 水平方向
tkinter.VERTICAL 竖直方向（moren)
tickinterval 选择值为该值得倍数
length 水平时表示宽度，竖直时表示宽度
'''
scale = tkinter.Scale(win,from_=0,to=100,
	orient=tkinter.HORIZONTAL,tickinterval=10,length=200)
scale.pack()

#设置值
scale.set(20)

# 获取值
def showNum():
	print(scale.get())


tkinter.Button(win,text='按钮',command=showNum).pack()

# 进入消息循环
win.mainloop()


