import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x100+200+50")

# 创建多行文本框
text = tkinter.Text(win,width=30,height=4)
text.pack(side = tkinter.LEFT,fill = tkinter.Y)

str = '''
【推荐】超50万C++/C#源码: 大型实时仿真组态图形源码
【活动】阿里云910会员节多款云产品满减活动火热进行中
【推荐】新手上天翼云，数十款云产品、新一代主机0元体验
【推荐】零基础轻松玩转华为云产品，获壕礼加返百元大礼
【推荐】华为云文字识别资源包重磅上市，1元万次限时抢购'''

# 给文本框插入数据
text.insert(tkinter.INSERT,str)


# 创建滚动条
scroll = tkinter.Scrollbar()
# side:放到窗体的哪一侧 
# fill :填充
scroll.pack(side = tkinter.RIGHT,fill = tkinter.Y)

# 关联
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)


# 进入消息循环
win.mainloop()
