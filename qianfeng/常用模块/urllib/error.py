import urllib.request
import urllib.parse
import urllib.error

url = 'http://www.maodan.com/'
try:
	response = urllib.request.urlopen(url)
except urllib.error.URLError as e:
	print(e)
except urllib.error.HTTPError as e:
	print(e)




