# coding=gbk

import unittest

from person import Person


class Test(unittest.TestCase):
	def test_init(self):
		p = Person("hjl",20)
		self.assertEqual(p.name,"hjl","属性赋值错误")
		
	
	def test_getAge(self):
		p = Person('hjl',22)
		self.assertEqual(p.getAge(),p.age,"getAge函数有误")
		
		
if __name__ == "__main__":
	unittest.main()