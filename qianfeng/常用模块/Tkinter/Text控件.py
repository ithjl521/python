import tkinter

# 创建主窗口
win = tkinter.Tk()

# 设置标题
win.title('title-hjl')
# 设置大小和位置
win.geometry("400x400+200+50")

'''
文本控件，用于显示多行文本
'''
text = tkinter.Text(win,width=30,height=4)
text.pack()

str = '''
【推荐】超50万C++/C#源码: 大型实时仿真组态图形源码
【活动】阿里云910会员节多款云产品满减活动火热进行中
【推荐】新手上天翼云，数十款云产品、新一代主机0元体验
【推荐】零基础轻松玩转华为云产品，获壕礼加返百元大礼
【推荐】华为云文字识别资源包重磅上市，1元万次限时抢购'''

text.insert(tkinter.INSERT,str)



# 进入消息循环
win.mainloop()
