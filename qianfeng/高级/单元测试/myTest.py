# coding=gbk
import unittest

from �Ժ������е�Ԫ���� import mySum
from �Ժ������е�Ԫ���� import mySub


class Test(unittest.TestCase):
	def setUp(self):
		print("��ʼ����ʱ�Զ�����")
		
	
	def tearDown(self):
		print("��������ʱ�Զ�����")
		
		
	# Ϊ�˲���mySum
	def test_mySum(self):
		self.assertEqual(mySum(1,2),3,"�ӷ�����")
		
		
		
if __name__ == "__main__":
	unittest.main()

