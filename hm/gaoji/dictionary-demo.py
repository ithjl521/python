man = {"name":'xiaoming',
		'age':12,
		'height':174,
		'gender':True,
		}

print(man)

# 取值
print(man['name'])

# 增加/修改 键存在则修改，不存在则增加
man['weight'] = 100
man['age'] = 18
print(man)

# 删除
man.pop('weight')
print(man)

# 统计键值对数量
print(len(man))

# 合并字典
tmp_dictionary = {'a':'a'}
man.update(tmp_dictionary)
print(man)

# 清空字典
man.clear()
print(man)

del man

