from bs4 import BeautifulSoup as bs
import requests
import csv

# html로 작성된 웹페이지 코드를 반환
# html언어 구조: <태그 속성=속성값> 텍스트 </태그>
html = requests.get('http://ncov.mohw.go.kr/')
soup = bs(html.text,'html.parser')

# find(태그, {속성: 속성값})
# 처음 매칭된 1개의 값만 반환
data1 = soup.find('div',{'class':'datalist'})   #


# findAll(태그)
# 매칭된 모든 값을 리스트 형태로 반환
data2 = data1.findAll('li')

# 국내 코로나 출력
fine_dust = data2[0].find('span',{'class':'data'}).text
print("일일 국내 코로나 발생자",fine_dust)


# 해외 유입 확진자
ultra_fine_dust = data2[1].find('span',{'class':'data'}).text
print("해외 유입 확진자", ultra_fine_dust)




#file = open('hello.txt', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
#file.write(str(fine_dust)+","+str(ultra_fine_dust))      # 파일에 문자열 저장
#file.close()

#f = open('hello.csv','w', newline='')
#wr = csv.writer(f)
#wr.writerow([1,str(fine_dust)])
#wr.writerow([2,str(ultra_fine_dust)])
#f.close()

file = open('crawler/korea_corona.html', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
file.write('<div class="daydata">'+'<h1>'+'<p style ="color:rgb(255, 255, 255)">'+str(fine_dust)+'명</p></h1>'+'</div>')      # 파일에 문자열 저장
file.close()

file = open('crawler/world_corona.html', 'w')    # hello.txt 파일을 쓰기 모드(w)로 열기. 파일 객체 반환
file.write('<div class="daydata">'+'<h1>'+'<p style ="color:rgb(255, 255, 255)">'+str(ultra_fine_dust)+'명</p></h1>'+'</div>')      # 파일에 문자열 저장
file.close()


###########################################
