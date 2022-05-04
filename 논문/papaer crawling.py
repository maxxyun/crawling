
import sys
import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver

url = 'https://play.google.com/store/apps/details?id=com.ekkorr.cook&hl=ko'

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get(url)
driver.implicitly_wait(3)

##더보기 횟수 저장
more = 0
max_more = 100

while(True):
 driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 time.sleep(0.5)

 if (more == max_more):
 break

 try:
 ## 더보기
 element = driver.find_element_by_xpath('//div[@jsname="xxxxx"]')
 if (element is not None):
 more += 1
 print(more)
 element.click()
except Exception:
continue

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')

##사용자 리뷰만 뽑아오기. 기본 리뷰
reviews1 = soup.find_all("span", {"jsname":"xxxxx"})
##전체 리뷰 버튼이 있을 때
reviews2 = soup.find_all("span", {"jsname":"xxxxx"})

print(len(reviews2))

##파일에 쓰기
sys.stdout = open('documents.txt','w', -1, "utf-8")

count = 0

for n in reviews2:
 if len(n.text) == 0:
 ##contents = reviews1[count].text.strip()
 contents = reviews1[count].get_text()
 else:
 ##contents = n.text.strip()
 contents = n.get_text()

 ##특수 문자 제거
 contents = re.sub('[^가~힣0-9a-zA-Z ]', '', contents)

 contents.encode('utf-8')
 print(contents)

 count = count + 1