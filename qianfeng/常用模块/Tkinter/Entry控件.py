import tkinter

'''
输入控件
用于显示简单的文本内容
'''

win = tkinter.Tk()
win.title('title-hjl')
win.geometry("400x400+200+50")

# 绑定变量
e = tkinter.Variable()
'''
创建输入控件
show:密文显示
textvariable:将输入框对象绑定到e
'''
entry = tkinter.Entry(win,textvariable=e,show='*')
entry.pack()

# 给输入框设置值
e.set('hello')
# 取值
print(e.get())


win.mainloop()