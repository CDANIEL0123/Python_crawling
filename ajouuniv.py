from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse
import re
import csv

#url = 'http://hosp.ajoumc.or.kr/Center/MedicalDoctor.aspx?mpc=MP001'
firsturl = 'http://hosp.ajoumc.or.kr/Center/'
#response = urllib.request.urlopen(url)
#soup = BeautifulSoup(response, 'html.parser')
url1= 'http://hosp.ajoumc.or.kr/Center/PartIndex.aspx'
response1 = urllib.request.urlopen(url1)
soup = BeautifulSoup(response1, 'html.parser')
result3=[]

formatt=[]
A=0
for f in range(3):
    formatt.append("0"+str(A))
    A+=1
for f in range(1):
    formatt.append(str(A))
    A+=1

for fo in formatt :
    #iden = f"ctl00_Contents_repList1_ct{formatte}_hlkImg"
    for link in soup.find_all(id=f"ctl00_Contents_repList1_ctl{fo}_hlkImg") :
        result=link.get('href')
        result2=firsturl+result
        result3.append(result2.replace("MedicalIntroduce","MedicalDoctor"))
result4=[]
for r in result3 :
    url2=r
    response2 = urllib.request.urlopen(url2)
    soup= BeautifulSoup(response2, 'html.parser')
    #i=0
    for fo in formatt :
        for link in soup.find_all(id=f"ctl00_Contents_rptDoctor_ctl{fo}_lnkDetail") :
            resultt=link.get('href')
            doc_add=firsturl+resultt
            result4.append(doc_add)


ajouuniv = []
print(len(result4))
for d in result4 :
    temp =[]
    response = urllib.request.urlopen(d)
    soup = BeautifulSoup(response, 'html.parser')
    exp=soup.find(class_="Txt").get_text().splitlines()
    major_name=soup.find('ul',{"class":"Section"}).get_text().splitlines()

    d= d.replace("Introduce","Career")
    response3 = urllib.request.urlopen(d)
    soup = BeautifulSoup(response3, 'html.parser')
    career=soup.find(class_="BulUl").get_text().splitlines()

  
    d= d.replace("Career","Thesis")
    response4 = urllib.request.urlopen(d)
    soup = BeautifulSoup(response4, 'html.parser')
    thesis=soup.find(class_='BulUl').get_text().splitlines()
 
    d= d.replace("Thesis","BoardRetrieve")
    response6 = urllib.request.urlopen(d)
    soup1 = BeautifulSoup(response6, 'html.parser')
    board=[]
    if soup1.find(class_='aleft'):
        soup1=soup1.select('.aleft')
        for i in soup1 :
         temp=[]
         temp.append(i.a.attrs['href'])
         temp.append(i.a.text)
         board.append(temp)
                          #boradlink=soup.find('href')
    else :
        board="게시글이없습니다"
    #print(board) 
    temp.append(major_name)
    temp.append(exp) 
    temp.append(career)
    temp.append(thesis)
    temp.append(board)
    #temp.append(boardlink)
    ajouuniv.append(temp)
    print(ajouuniv)
   # print(temp)
   # print()
   # print()

with open('ajouuu.csv','w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['전공이름','경험분야','커리어','저서','기사'])
    writer.writerows(ajouuniv)

print('ㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏㅏ ')
    

#for majornum in range(200) :
 #   url = f'http://hosp.ajoumc.or.kr/Center/MedicalDoctor.aspx?mpc=MP{majornum}'
  #  response = urllib.request.urlopen(url)
   # soup = BeautifulSoup(response, 'html.parser')
    #for link in soup.findAll('a',attrs={'class':'Btn StyA Gray FnLayerDoctor'}):
     #   result=link.get('href')
      #  print(firsturl+result)
#result=soup.find_all(class_='Btn StyA Gray FnLayerDoctor')
#print(result.attrs['href'])