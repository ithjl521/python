#！ python

import tool

while True:
	print('')

	tool.print_menu()

	action_str = input("请输入希望执行的操作：")
	print("您选择的操作是【%s】" % action_str)

	if action_str in ['1','2','3']:
		if action_str == '1':
			tool.new_card()
		elif action_str == '2':
			tool.show_card()
		elif action_str == '3':
			tool.search_card()


	elif action_str == '0':
		print('欢迎再次使用【名片管理系统】')
		break

	else:
		print('输入错误，请重新输入：')
