import calendar

# 日历模块


# 返回指定某年某月的日历
print(calendar.month(2019,8))

# 返回指定年的日历
print(calendar.calendar(2019))

# 判断闰年 闰年返回True否则返回False
print(calendar.isleap(2019))

# 返回某个月的weekday的第一天和这个月的天数
print(calendar.monthrange(2019,8))

# 返回某个月以每周为元素的列表
print(calendar.monthcalendar(2019,8))









