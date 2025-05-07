import random
from random import *
import classs
from selenium import *
# url = 'http://naver.com'
# url2='http://daum.net'


# lis=[url,url2,"http://google.com"]

# print(lis.index(url)) #url이 리스트 중 몇번쨰에 있는지

# for l in lis :
#     my_str=l.replace('http://',"")

#     mystr=my_str[:my_str.index(".")] #my_str에서 .의 위치 직전까지 자름


#     lenn=len(mystr)

#     pw=mystr[:3]+str(lenn)

#     cnt=mystr.count("e")

#     pw=mystr[:3]+str(lenn)+str(cnt)+"!"
#     print(f"{l}의 비밀번호는 {pw}입니다")

# numlis=[1,2,3,4,5]

# lis.extend(numlis) #extend 리스트들을 합침 
# print(lis)

# cab={3:"재석", 4:"세호"}
# print(cab.get(5,"사용가능")) #키에 5가 없으면 사용가능으로 입력
# print(cab.keys()) #키만출력
# print(cab.values())#값만 출력
# com=[]
# for c in range(1,21) :
#     com.append(c)

# shuffle(com)  #com리스트를 섞음
# print(com)
# win=sample(com,4) #com리스트의 4개를 뽑음
# print(win)

# customer ="토르"
# ind=5

# while rue :
#     print(f"{customer}야 좀와 {ind}")
#     ind-=1
#     if ind < 1 :
#         print("dsaf")


# absent = [2,5]
# nobook=[6]

# for s in range(1,11):
#     if s in absent :
#         continue
#     elif s in nobook :
#         print(f"{s}교무실로 따라오고")
#         break
#     print(f"{s}야 읽어봐")

# cus={}


# for i in range(1,51):
#     b=randrange(5,51)
#     cus.update({i:b})

# for key,value in cus.items() :
#     if 5<= value<=15 :
#         print(f"[o]{key}번쨰손님 소요시간{value}")
#     else :
#         print(f"[ ]{key}번째손님 소요시간{value}")

# def std_weight(height,gender) :
#     if gender=="남자" :
#        return height*height*22
#     elif gender=="여자" :
#          return height*height*21


# height = 175
# gender = "남자"

# weight = round(std_weight(height/100,gender),2)
# print(weight)

# score = open("score.txt","w",encoding="utf8") #w는 쓰기 r은 읽어오기 a는 어펜드(이어씀)
# print("수학 : 80",file=score)
# print("영어 : 90",file=score)
# # score.close()

# for i in range(1,3) :
#     with open(str(i)+"주차.text","w",encoding="utf8") as report:
#         report.write(f"{i}주차 주간보고")

print(dir(selenium))