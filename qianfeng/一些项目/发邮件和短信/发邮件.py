# 发邮件的库
import smtplib
# 邮件文本
from email.mime.text import MIMEText

# SMTP服务器
SMTPServer = "smtp.163.com"

# 发邮件地址
sender = "it_hjl@163.com"

# 发送者邮箱的密码 (授权码)
passwd = "ithjl163"



# 设置发送内容
message = 'hjl is a good man'

# 转换成邮件文本
msg = MIMEText(message)

# 邮件标题
msg['Subject'] = "来自远方的邮件"
# 发送者
msg['From'] = sender

# 创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer,25)
# 登录邮箱
mailServer.login(sender,passwd)


# 发送邮件
mailServer.sendmail(sender,['245180912@qq.com','154981815@qq.com'],msg.as_string())

# 退出邮箱
mailServer.quit()

