from selenium import webdriver
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse
import requests
import time
import csv
driver=webdriver.Chrome()
    
   # html = urllib.request.urlopen(url).read()
   # soup = BeautifulSoup(html,'html.parser')
def craw(a,b) :#xpath번호,리스트
   for l in soup.select(f'#BT0{a} > ul > li > div') :
            l=l.text.splitlines()
            b.append(l)


driver.get('https://www.jbuh.co.kr/cuh/main/sub03/sub01_1.jsp')

sum=0
result=[]
for j in range(1,5) :#35까지임
    driver.get('https://www.jbuh.co.kr/cuh/main/sub03/sub01_1.jsp')
    xpath1=f'//*[@id="content"]/div[2]/div/div/div[2]/div[{j}]/a/img'
    driver.find_element_by_xpath(xpath1).click()
    html=driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    num=len(soup.select('.btn_box'))

    for i in range(1,num+1) :
        #print(i)
        xpath2=f'//*[@id="content"]/div[2]/div/div/div[2]/table/tbody/tr[{i}]/td[2]/table/tbody/tr/td[1]/p[3]/a'
        driver.find_element_by_xpath(xpath2).click()
        driver.switch_to_window(driver.window_handles[1])
        html1=driver.page_source
        soup=BeautifulSoup(html1,'html.parser')
        temp=[]

        for i in soup.select('body > div > div > div > ul.Tap_content > li.Base_info > table > tbody > tr > td') :
            i=i.text.splitlines()
            temp.append(i)

        for j in soup.select('#BT02 > ul > li > div') :
            j=j.text.splitlines()
            temp.append(j)

        for k in soup.select('#BT03 > ul > li > div') :
            k=k.text.splitlines()
            temp.append(k)

        for l in soup.select('#BT04 > ul > li > div') :
            l=l.text.splitlines()
            temp.append(l)

        result.append(temp)
            
        time.sleep(1)
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
    #break
with open('jeonbuk.csv','w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['전공','이름','경험분야','주요학력','주요경력','논문저서'])
    writer.writerows(result)