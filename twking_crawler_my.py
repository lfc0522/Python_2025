# 在twking.org這個網站上爬蟲，找top1-5連結與小說名字
# 安裝套件 pip install requests
from pprint import pprint
from bs4 import BeautifulSoup
import requests
# step 1.取回html 2.Request
r = requests.get('https://www.twking.org')
r.encoding = 'utf8'  # 處理亂碼
print(r.text)
# step 3.轉化成soup
soup = BeautifulSoup(r.text, 'html.parser')
print(r.text)
# step 4.分析 連結與小說名稱 by top10
booktop_data = dict()  # 資料儲存，將取得的書名跟連結儲存
booktops = soup.find_all('div', class_='booktop')  # return list of booktops
# booktop,top10,booktop_name為變數名稱
for booktop in booktops:
    booktop_name = booktop.p.string
    print(booktop_name)
    # 排行榜是key，把[小說連結,書名]存為value
    booktop_data[booktop_name] = [
        (top10['href'], top10.string.strip()) for top10 in booktop.find_all('a')]

    # top 10
    for top10 in booktop.find_all('a'):
       # print(top10)
        print(top10['href'], top10.string.strip())  # 取連結跟小說名稱

pprint(booktop_data)  # 把dict的資料存入，以後取資料就由booktop_data取
