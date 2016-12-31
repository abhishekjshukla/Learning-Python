from bs4 import BeautifulSoup
import requests
import os
print("Start")
data=requests.get('https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-006-introduction-to-algorithms-fall-2011/lecture-videos/')
data=data.content
soup=BeautifulSoup(data,"html.parser")
data2=soup.find_all('a',{'class':'bullet medialink'},href=True)
for i in data2:
	name1=str(i.string)
	name1=name+'.srt'
	print(name1)
	lk='https://ocw.mit.edu'+i['href']
	d1=requests.get(lk)
	d1=d1.content
	s2=BeautifulSoup(d1,'html.parser')
	d2=s2.find('a',string="SRT",href=True)
	srtl='https://ocw.mit.edu'+d2['href']
	l3=requests.get(srtl)
	with open(name1, "wb") as code:
		code.write(l3.content)
	print('done')
	t+=1
print('final')