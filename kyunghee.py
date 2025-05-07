from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse
import requests
import csv

url = 'https://www.khuh.or.kr/03/01.php'  #전체 진료과화면 링크

response = urlopen(url)
soup=BeautifulSoup(response,'html.parser')
link_soup=soup.select('tr > td.style1') #각 진료과 href 들어있는 htmp 추출

links=[] #각 진료과 href
link=[] #각 진료과 의사목록
lin=[] #default 링크를 제외한 전체 진료과 링크


for a in soup.select('tr > td.style1 > a'):
    result=a['href']
    links.append(result) 

firsturl = 'https://www.khuh.or.kr/03/'

for b in links :
    li=firsturl+b #+'#02'
    link.append(li)   

for l in link[0:-4] : 
    lin.append(l)

name1=[]
for a in lin :
    response = urlopen(a)
    #html = response.read().decode(encoding="iso-8859-1")
    soup=BeautifulSoup(response,'html.parser')
    major=soup.select_one('table > tr > td > table > tr > td > div > table > tr > td > img')
    print(major)
    for a in soup.select('div > table > tr > td > table > tr > td > table > tr > td > table > tr > td > table > tr > td > div > table > tr > td.padding01 > table > tr > td > table > tr > td > table > tr > td > table > tr > td' ) :#의사정보+의사명 영역
        temp=[]
        #a2=a.find( align = "center")  
        #a1=a.select_one('td > b')
        #print(a1)
        print(a)

        #s=soup.select_one('div > table > tr > td > table > tr > td > table > tr > td > table > tr > td > table > tr > td > div > table > tr > td.padding01 > table > tr > td > table > tr > td > table > tr > td > font > table') #의사정보만있는 영역
        #print(s)
        #print(len(soup.select('div > table > tr > td > table > tr > td > table > tr > td > table > tr > td > table > tr > td > div > table > tr > td.padding01 > table > tr > td > table > tr > td > table > tr')))
        break
    break
    #for n in soup.select('td > div > tr > td > table > tr > td > b') :
    #    namae=n.text.splitlines()
    #    name1.append(namae)

    #for n in soup.select('tr > td > table > tr > td > font >table') :
    #    n1=n.text.splitlines()
    #    #print(n1)