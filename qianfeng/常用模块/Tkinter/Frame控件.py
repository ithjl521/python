import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")


'''
框架控件
在屏幕上显示一块矩形区域，多作为容器控件
'''

frm = tkinter.Frame(win)
frm.pack()

# left
frm_l = tkinter.Frame(frm)
tkinter.Label(frm_l,text='左上',bg='pink').pack(side=tkinter.TOP)
tkinter.Label(frm_l,text='左下',bg='blue').pack(side=tkinter.TOP)
frm_l.pack(side=tkinter.LEFT)


# right
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r,text='右上',bg='red').pack(side=tkinter.TOP)
tkinter.Label(frm_r,text='右下',bg='yellow').pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.RIGHT)


# 进入消息循环
win.mainloop()


