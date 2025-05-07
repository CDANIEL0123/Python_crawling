import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

count=1
 
#baseurl = 'https://search.naver.com/search.naver?where=post&sm=tab_jum&query='
plusurl = urllib.parse.quote_plus(input('검색어를 입력하세요'))
#url = baseurl + urllib.parse.quote_plus(plusurl)
pagenum = 1

i =input("몇페이지크롤링할까요?")

lastpage = int(i)*10-9
while pagenum < lastpage+1 : 
    url = f'https://search.naver.com/search.naver?date_from=&date_option=0&date_to=&dup_remove=1&nso=&post_blogurl=&post_blogurl_without=&query={plusurl}&sm=tab_pge&srchby=all&st=sim&where=post&start={pagenum}'

    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html,'html.parser') # BeautifulSoup 객체생성
    title = soup.find_all(class_='sh_blog_title')

    
    for i in title:
        print(i.attrs['title'])
        print(i.attrs['href'])
        count+=1
        print(f'{count}번쨰입니다')

    pagenum = pagenum+10


##keywords = soup.find_all('a','title') # 데이터에서 태그와 클래스를 찾는 함수
