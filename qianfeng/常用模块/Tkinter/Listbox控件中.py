import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")

lbv = tkinter.StringVar()


# 与BORWSE相似，但是不支持鼠标选中位置
lb = tkinter.Listbox(win,selectmode=tkinter.SINGLE,
	listvariable=lbv)
lb.pack()

for item in ['good','nice','handsome','word','haha']:
	# 按顺序添加
	lb.insert(tkinter.END,item)


# 当前列表中的选项
print(lbv.get())

# 改变列表选项
# lbv.set(('1','2','3','4'))


def myPrint(event):
	print(lb.get(lb.curselection())) 

# 给控件绑定事件
lb.bind("<Double-Button-1>",myPrint)


# 进入消息循环
win.mainloop()
