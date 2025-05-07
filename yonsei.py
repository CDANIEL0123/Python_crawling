#!/usr/bin/env python3
# Anchor extraction from HTML document

from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse
from selenium import webdriver
import csv
import re
chromedriver ='C:/PYTHON_수련/chromedriver'
#driver = webdriver.Chrome()


ith urlopen('https://www.ywmc.or.kr/web/www/medical_office') as response:
    soup = BeautifulSoup(response, 'html.parser')

soup = soup.find('div',{"class":"vinr"})

link=[]
for i in soup.select('li > a ') :
    link.append('https://www.ywmc.or.kr' + i['href'])
links=[]
for l in link :
    l = l.replace("intro","doc")
    links.append(l)
links.append('https://www.ywmc.or.kr/web/www/pain_clinic/doc')


school=[]
result=[]
for a in links : 
    response = urlopen(a)
    soup1 = BeautifulSoup(response, 'html.parser')
    for z in soup1.select('.pop_cont') :
        name=z.select_one('div.info').text
        exp=z.select_one('span.posi01')

        school=[]
        for s in z.select('div.box'):
            school.append(s.select_one('li').text)
            school.append("★★★")
        
        #school.append(z.select_one('div.portfolio').text)
        #print(school)
        #print()
        temp=[]
        temp.append(name)
        temp.append(exp) 
        temp.append(school)
        result.append(temp)

with open('yonsei.csv','w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['전공이름','경험분야','커리어'])
    writer.writerows(result)

