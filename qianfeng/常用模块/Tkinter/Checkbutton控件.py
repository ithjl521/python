import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")


def update():
	message = ''
	if hobby1.get() == True:
		message += 'money\n'
	if hobby2.get() == True:
		message += 'power\n'
	if hobby3.get() == True:
		message += 'person\n'

	# 清空所有内容
	text.delete(0.0,tkinter.END)
	text.insert(tkinter.INSERT,message)


hobby1 = tkinter.BooleanVar()
check1 = tkinter.Checkbutton(win,text='money',
	variable=hobby1,command=update)
check1.pack()

hobby2 = tkinter.BooleanVar()
check2 = tkinter.Checkbutton(win,text='power',
	variable=hobby2,command=update)
check2.pack()

hobby3 = tkinter.BooleanVar()
check3 = tkinter.Checkbutton(win,text='person',
	variable=hobby3,command=update)
check3.pack()


text = tkinter.Text(win,width=50,height=10)
text.pack()


# 进入消息循环
win.mainloop()
