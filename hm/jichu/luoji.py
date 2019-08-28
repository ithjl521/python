height = 180
weight=130
age=23
if height>150 and weight<150:
	print('身高：%d，并且体重：%d'%(height,weight))

if height>150 or age>18:
	print('身高大于150，或者年龄大于18')

if not height>180:
	print('身高小于等于180')