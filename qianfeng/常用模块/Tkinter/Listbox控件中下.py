import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x100+200+50")

# EXTENDED 可以使listbox支持shift和Ctrl
lb = tkinter.Listbox(win,selectmode=tkinter.EXTENDED)
lb.pack(side=tkinter.LEFT,fill=tkinter.BOTH)


for item in ['good','nice','handsome','word','haha','1',
'2','3','4']:
	# 按顺序添加
	lb.insert(tkinter.END,item)


# 滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT,fill = tkinter.Y)
lb.configure(yscrollcommand=sc.set)
# 额外给属性赋值
sc['command'] = lb.yview

# 进入消息循环
win.mainloop()
