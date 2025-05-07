from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.parse
import requests
import csv
firsturl = 'https://www.wkuh.org/main/sub.asp?'
url='https://www.wkuh.org/main/sub.asp?avan=1001020000'
response = urlopen(url)
soup=BeautifulSoup(response,'html.parser')

links=[]
for a in soup.find_all('a', href=True):
    result=a['href']
    links.append(result)

links=[' ?avan=1001020000&MEDI_PARTMode=view&md_code=IMG& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=IMB& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=IMC& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=IMP& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=IME& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=IRM& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=IMK& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=IMH& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=IMI& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=FAM& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=PDC& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=PED& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=NEU& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=PMR& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=PB2& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=ANP& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=DER& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=CVM& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=CVR& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=EMD& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=SCP& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=TRS& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=SHB& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=SBT& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=SGS& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=SVA& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=URO& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=GYN& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=PRS& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=NSW& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=EYE& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=ENT& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=OSG& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=CTS& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=CVS& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=ROC& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=NCM& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=ANE& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=OEM& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=PAT& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=CPP& ',

' ?avan=1001020000&MEDI_PARTMode=view&md_code=RAD& ',]
newlinks=[]


for i in links :
    a=firsturl+i
    x = a.replace('? ?','?')
    y= x.replace('view','view2')
    newlinks.append(y)

postlinks=[]
for n in newlinks :
    response = urlopen(n)
    new=BeautifulSoup(response,'html.parser')
    a_tags = new.select('.btn_orange') 
    for a in a_tags : 
        b=a.attrs['onclick']
        postlinks.append(b)
    break

result=[]

for a in newlinks :
    response = urlopen(a)
    soup=BeautifulSoup(response,'html.parser')
    for z in soup.select('.doc_profile') :
        main=[]
        temp=[]
        ssch=[]
        ssch1=[]
        ssch2=[]
        ssch3=[]
        a_tags = z.select_one('.btn_orange')  
        b=a_tags.attrs['onclick']
        postlinks=b
        li='https://www.wkuh.org/_userApp/MediPlace_Doctor/user/Detail_view.asp?Num=['+postlinks+']'
        lis=li.replace("[detail_view('","")
        lisx=lis.replace("', 'D2')]","")

        soup1=z.select_one('dl')
        for b in soup1.select('dd') :
            ma=b.text.splitlines()
            main.append(ma)
        main1=main
        #print(main) [],[],[],[] 형태

        schlink = lisx+'&typ=D2'
        response = urlopen(schlink)
        sou=BeautifulSoup(response,'html.parser')
        sch=sou.select('td.pal10')
        

        schlink1 = lisx+'&typ=D3'
        response = urlopen(schlink1)
        sou1=BeautifulSoup(response,'html.parser')
        sch1=sou1.select('td.pal10')

        schlink2 = lisx+'&typ=B1'
        response = urlopen(schlink2)
        sou2=BeautifulSoup(response,'html.parser')
        for a in sou2.select('a') : 
            h=a.text
            ssch2.append(h)
        sch2=ssch2

        schlink3 = lisx+'&typ=B2'
        response = urlopen(schlink3)
        sou3=BeautifulSoup(response,'html.parser')
        for b in sou3.select('td > a') :
            boardlink=b.attrs['href']
            board = 'https://www.wkuh.org/_userApp/MediPlace_Doctor/user/Detail_view.asp'+boardlink
            ssch3.append(b)
            ssch3.append(board)
        sch3=ssch3
        temp.append(main1)
        temp.append(sch)
        temp.append(sch1)
        temp.append(sch2)
        temp.append(sch3)
        result.append(temp)
        
    

with open('wonkwang.csv','w',encoding='utf-8',newline='') as f:
    writer=csv.writer(f)
    writer.writerow(['메인','sch제로','sch하나','sch둘','sch셋'])
    writer.writerows(result)
    