import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import csv

hdr = { 'User-Agent' : 'Mozilla/5.0'} #406에러
url = 'https://www.melon.com/chart/day/index.htm'

req = urllib.request.Request(url, headers=hdr) #406에러
html =urllib.request.urlopen(req).read()
soup = BeautifulSoup(html,'html.parser')
lst50 = soup.select('.lst50,.lst100') #select로 가져오면 list가 됨
#lst100 = soup.select('.lst100')

melonlist = []
for i in lst50 :
    temp =[]
    temp.append(i.select_one('.rank').text) #end='위: ')
    temp.append(i.select_one('.ellipsis.rank01').a.text)#,end=' ') # 텍스트만 가져오기  / end~~는 로우처럼 한줄로 나오게
    temp.append(i.select_one('.ellipsis.rank02').a.text)#,end=' ') #a태그안의 텍스트만 가져오기 -> 공백없앰
    temp.append(i.select_one('.ellipsis.rank03').a.text)
    melonlist.append(temp)

for m in melonlist :
    print(m)
    print()

#with open('melon100.csv','w',encoding='utf-8',newline='') as f :
#    writer = csv.writer(f)
#    writer.writerow(['순위','제목','아티스트','앨범'])
#    writer.writerows(melonlist)