from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

baseurl='https://search.naver.com/search.naver?sm=tab_hty.top&where=image&query='
plusurl=input('검색어를 입력하세요')
url = baseurl + quote_plus(plusurl)

print(url)

html = urlopen(url).read()
soup=BeautifulSoup(html,'html.parser')
img = soup.find_all(class_='_img')

n=1
for i in img :
    imgurl=i['data-source']
    with urlopen(imgurl) as f:
        with open('./img/' + plusurl + str(n) + '.jpg', 'wb') as h:
            img = f.read()
            h.write(img)
    n= n+1
    print(imgurl)

print("다운로드완료")            