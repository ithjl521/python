# coding=gbk

import unittest

from person import Person


class Test(unittest.TestCase):
	def test_init(self):
		p = Person("hjl",20)
		self.assertEqual(p.name,"hjl","���Ը�ֵ����")
		
	
	def test_getAge(self):
		p = Person('hjl',22)
		self.assertEqual(p.getAge(),p.age,"getAge��������")
		
		
if __name__ == "__main__":
	unittest.main()