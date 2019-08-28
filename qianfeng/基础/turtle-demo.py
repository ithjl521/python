"""
简单绘图工具
"""
import turtle

# 笔画控制命令
# 速度
turtle.speed(0)

# 运动命令
turtle.forward(100) # 前进
turtle.backward(100)
turtle.circle(100) # 圆
turtle.circle(100,steps=5) # 五边形,steps表示多少笔画完
# 开始填充
turtle.begin_fill()
# 填充
turtle.fillcolor("blue")
turtle.circle(100,steps=5) # 五边形,steps表示多少笔画完
# 结束填充
turtle.end_fill()






# 其他命令
# turtle.done()




