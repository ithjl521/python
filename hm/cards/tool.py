def print_menu():

	"""打印菜单"""
	print('*'*50)
	print('欢迎使用名片管理系统')
	str1 = '1.新建名片'
	print(str1.center(10))
	str2 = '2.显示名片'
	print(str2.center(10))
	str3 = '3.搜索名片'
	print(str3.center(10))
	str3 = '0.退出系统'
	print(str3.center(10))
	print('*'*50)


# 记录所有的名片字典
card_list = []


def new_card():
	print('*'*25)
	print('功能：新增名片')

	name  = input('请输入姓名：')
	phone  = input('请输入电话：')
	qq  = input('请输入QQ：')
	email  = input('请输入邮箱：')


	card_dict = {'name':name,
				'phone':phone,
				'qq':qq,
				'email':email}

	card_list.append(card_dict)

	print(card_list)

	print('%s的名片添加成功'%name)


def show_card():
	print('*'*25)
	print('功能：显示所有名片')

	if len(card_list) == 0:
		print('没有名片，请添加！')
		return

	for name in ['姓名','电话','QQ','邮箱']:
		print(name,end='\t\t')

	print('')
	print('='*80)

	for man in card_list:
		print('%s\t\t%s\t\t%s\t\t%s'%(man['name'],
			man['phone'],man['qq'],man['email']))


def search_card():
	print('*'*25)
	print('功能：搜索名片')

	search_name = input('请输入要查询的姓名：')

	for card_dict in card_list:
		if search_name == card_dict['name']:
			print('找到了')
			print('='*60)
			for name in ['姓名','电话','QQ','邮箱']:
				print(name,end='\t\t')

			print('')

			for man in card_list:
				print('%s\t\t%s\t\t%s\t\t%s'%(card_dict['name'],
					card_dict['phone'],card_dict['qq'],card_dict['email']))

			print()
			print('='*60)
		
			deal_card(card_dict)

			break

	else:
		print('用户%s不存在！'%search_name)


def deal_card(find_dict):
	action_str = input('请输入要执行的操作：1修改，2删除，0返回菜单1')
	if action_str == '1':
		find_dict['name'] = input_card_info(find_dict['name'],'修改姓名【回车不修改】：')
		find_dict['phone'] = input_card_info(find_dict['phone'],'修改电话【回车不修改】：')
		find_dict['qq'] = input_card_info(find_dict['qq'],'修改QQ【回车不修改】：')
		find_dict['email'] = input_card_info(find_dict['email'],'修改邮箱【回车不修改】：')
		print('修改名片成功')
	elif action_str == '2':
		
		card_list.remove(find_dict)
		print('删除名片成功')


def input_card_info(dict_val,tip_message):
	"""自定义input函数"""

	res = input(tip_message)

	if len(res) > 0:
		return res
	else:
		return dict_val






