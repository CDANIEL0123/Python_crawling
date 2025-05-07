import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

 
baseurl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusurl = input('검색어를 입력하세요')
url = baseurl + urllib.parse.quote_plus(plusurl)
#pagenum = 1
html = urllib.request.urlopen(url).read()

#url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&
#post_blogurl_without=&query={plusurl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pagenum}'

soup = BeautifulSoup(html,'html.parser') # BeautifulSoup 객체생성

### ↑↑↑↑기본설정
title = soup.find_all(class_='sh_blog_title')
#title=title[1]
ttt=[]
res=[]
for i in title:
    titles=i.attrs['title']
    href=i.attrs['href']
    ttt.append(titles)
    ttt.append(href)
    res.append(ttt)

for i in ttt:
    print(ttt)
    print()



##keywords = soup.find_all('a','title') # 데이터에서 태그와 클래스를 찾는 함수




