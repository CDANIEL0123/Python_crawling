from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse
import requests
import csv

links = []
def find_bad_qn(i,mylist):
    url = f'https://www.cmcism.or.kr/treatment/treatment_team?deptSeq={i}'
    try:
        urlopen(url)
        mylist.append(url)
    except:
        pass
for j in range(1, 200) :
    find_bad_qn(j,links)
    break

result=[]

for a in links :
    response= urlopen(a)
    soup = BeautifulSoup(response, 'html.parser')

    for b in soup.select('.tab_container.mgt35') :
        temp=[]
        med=[]
        school=[]
        #print(b)

        name1 = soup.select_one('li.li_h').text

        etc1=soup.select_one('.mgt10').text
    
        car1 = soup.select_one('dl.dl_type02').text    #career 

        for g in soup.select('dl.dl_type02.mgt30 > dd') :
            sch = g.text    #school + etc
            school.append(sch)

        for c in soup.select('td.text_left') :
            a = c.select_one('a')
            med.append(a)

        temp.append(name1)
        temp.append(etc1)
        temp.append(car1)
        temp.append(school)
        temp.append(med)
        result.append(temp)
    
    break
for b in result :
    print(b)
    print()
    print()

with open('incheon.csv','w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['전공이름','기타등등','커리어1','커리어2~','미디어'])
    writer.writerows(result)