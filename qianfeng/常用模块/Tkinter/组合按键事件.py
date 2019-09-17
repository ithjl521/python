import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")



label = tkinter.Label(win,text='he jiao long is a good man',bg='yellow')
label.focus_set() # 给控件设置焦点
label.pack()

def func(event):
	print('event.char=',event.char)
	print('event.keycode=',event.keycode)
	
# 只有同时按下ctrl,alt,a键时有触发事件
label.bind('<Control-Alt-a>',func)


# 进入消息循环
win.mainloop()


