# coding=gbk
#ԭ�� filter(fn,lsd)
# ����һΪ������������Ϊ����

#���� �����ڹ�������
# �Ѵ���ĺ���һ�����������е�ÿ��Ԫ�أ����ݷ��ص���True����False�ж��Ƿ���


list1 = [1,2,3,4,5,6,7,8,9]
# ɸѡ����
def func(num):
	# ż������
	if num%2 == 0:
		return True
	
	# �����߳�
	return False
	
	
l = filter(func,list1)
print(list(l))







