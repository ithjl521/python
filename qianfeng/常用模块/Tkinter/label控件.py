import tkinter


win = tkinter.Tk()
win.title('title-hjl')
win.geometry("400x400+200+50")

# label:标签控件可以显示文本
# win:父窗体，
# text:显示的文本内容，
# bg：背景色，
# fg:字体颜色,
# font:字体
# width:宽
# height:高
# wraplength:指定text文本中多宽进行换行
# justify:设置text换行后的对齐方式
# anchor:text位置 n:北 e：东 s：南 w：西 center：居中 ne se sw nw
lable = tkinter.Label(win,
	text = 'this is text',
	bg = 'pink',
	fg = 'red',
	font = ('黑体',20),
	width =10,
	height = 3,
	wraplength = 100,
	justify = 'left',
	anchor = 'center')

# 显示出来
lable.pack()


win.mainloop()


