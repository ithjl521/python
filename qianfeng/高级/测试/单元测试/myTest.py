# coding=gbk
import unittest

from 对函数进行单元测试 import mySum
from 对函数进行单元测试 import mySub


class Test(unittest.TestCase):
	def setUp(self):
		print("开始测试时自动调用")
		
	
	def tearDown(self):
		print("结束测试时自动调用")
		
		
	# 为了测试mySum
	def test_mySum(self):
		self.assertEqual(mySum(1,2),3,"加法有误")
		
		
		
if __name__ == "__main__":
	unittest.main()

