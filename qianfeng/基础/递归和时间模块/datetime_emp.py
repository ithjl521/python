import datetime


d1 = datetime.datetime.now()
print(d1)

d2 = datetime.datetime(1999,10,1,10,28,25,123456)
print(d2)

d3 = d1.strftime("%Y-%m-%d %X")
print(d3)







