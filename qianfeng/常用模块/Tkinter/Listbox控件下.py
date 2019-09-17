import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")

# MULIPLE 支持多选
lb = tkinter.Listbox(win,selectmode=tkinter.MULTIPLE)
lb.pack()


for item in ['good','nice','handsome','word','haha','1',
'2','3','4']:
	# 按顺序添加
	lb.insert(tkinter.END,item)



# 进入消息循环
win.mainloop()


