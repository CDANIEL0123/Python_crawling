from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse
from selenium import webdriver
import requests


link = [3,4,5,6]

for i in link :
    url = f'https://www.brmh.org/medicalcare/doctors/_/{i}/docDtl.do?showTab=profile#tabs01'  
    response = urllib.request.urlopen(url)  
    soup=BeautifulSoup(response,'html.parser')
    txt=soup.find('h4',{"class":"text-info"}).get_text()
    major=soup.find('span',{"class":"label label-info"}).get_text()
    exp=soup.find('ul').get_text()
   
    re=[]
    soup1 = soup.find_all('ul', style='list-style-type: none;')
    for i in soup1 :
        re.append(i.get_text())
        re.append(" ")
   
    ap=[]
    for el in soup.select("ol > li") :
        ap.append(el.get_text())
        ap.append(" ")
        
    print(txt)
    print(major)
    print(exp)
    print(re)
    print(ap)
    print()
    print()
    break



   



#response = urllib.request.urlopen(url)
#soup = BeautifulSoup(response, 'html.parser')
#docnum=[]

#soup = soup.select('div.btn-group.btn-group-sm > a.btn.btn-default')
#soup = soup.select('btn.btn-default')

#for i in soup :
#    docnum.append(i)

#for s in docnum :
#    print(s)
#    print()
#    //*[@id="content"]/div[3]/div[2]/div[1]/div/div/div/div
    