import requests

# video标签中的src地址
url = 'https://v1-tt.ixigua.com/a17cb8003636739247d65182957fd76e/5da68415/video/m/220017d5d104ed44f379e41d571d848e6f81163de71b00000e41debee34e/?a=1768&br=1367&cr=0&cs=0&dr=0&ds=3&er=&l=201910160943540100140510892A7BD6E6&lr=&rc=Mzptd2U8aDpycDMzNTczM0ApaTo8NGY1MzxmNzVnNWkzN2drbC0vbTUzc2ZfLS1eLTBzc2JjYTAyYmMvYDY2X19iNTQ6Yw%3D%3D'

headers = {
	"User-Agnet":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"
}

r = requests.get(url=url,headers=headers)

with open('1.mp4','wb') as fp:
	fp.write(r.content)
