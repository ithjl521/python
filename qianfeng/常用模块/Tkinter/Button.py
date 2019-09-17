import tkinter


def fun():
	print('hello word')


win = tkinter.Tk()
win.title('title-hjl')
win.geometry("400x400+200+50")

# 创建按钮
button = tkinter.Button(win,
	text='按钮',
	command=fun,
	width=10,
	height=10)
button.pack()


button2 = tkinter.Button(win,
	text='按钮',
	command=win.quit)
button2.pack()


win.mainloop()