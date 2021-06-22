from bs4 import BeautifulSoup
from urllib import parse,request
import locale

locale.setlocale(locale.LC_ALL, 'en_US.UTF8')

keyword="대전 코로나"
keyword=parse.quote(keyword)

URL='https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query='+keyword
print(URL)

req=request.urlopen(URL)
soup=BeautifulSoup(req, 'html.parser')

tbody=soup.find_all('tbody')
coronadic={}
for t in tbody:
    result=t.get_text()
    if("서울" in result or "대전" in result or "세종" in result):
        tlist=t.get_text().split()
        #print(tlist)
        for i in range(0,len(tlist),3):
            coronadic[tlist[i]]=[locale.atoi(tlist[i+1]),locale.atoi(tlist[i+2])]

for k in coronadic.keys():
    print(k,":",coronadic[k])
