import re

string = '<p><div><span>八戒</span></div></p>'

pattern = re.compile(r'<(\w+)><(\w+)>\w+</\2></\1>')

ret = pattern.search(string)

print(ret)

