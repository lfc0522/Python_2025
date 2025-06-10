# 在twking.org這個網站上爬蟲，找top1-5連結與小說名字
# 安裝套件 pip install requests
from collections import Counter
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
    # print(booktop_name)
    # 排行榜是key，把[小說連結,書名]存為value
    booktop_data[booktop_name] = [
        (top10['href'], top10.string.strip()) for top10 in booktop.find_all('a')]

    # top 10
    for top10 in booktop.find_all('a'):
       # print(top10)
       # print(top10['href'], top10.string.strip())  # 取連結跟小說名稱

        pprint(booktop_data)  # 把dict的資料存入，以後取資料就由booktop_data取

      # step 5:取排行榜交集

top10_counter = Counter()
for booktop_name in booktop_data:
    # print(top)
   # pprint(booktop_data[booktop_name])
    top10_counter.update(booktop_data[booktop_name])  # update top10
   # print()

# 取第1名的資料，  most_common(1)[0]會回傳資料,出現次數
# pprint(top10_counter.most_common(1)[0])
# top1, top1_count = top10_counter.most_common(1)[0]  # 取幾筆的第幾個 下例3是指排行榜出現3次
# [(https://www.twking.cc/223_223913/','苟在妖武亂世修仙'),3]
# top1_url, top1_name = top1
# print(top1_url)
# print(top1_name)  # 可以分別取出list的key與vlaue
# print()
# 例取出top3
# w3topn, topn_count = top10_counter.most_common(3)
pprint(top10_counter.most_common(10))
for topn, topn_count in top10_counter.most_common(3):  # 取前3筆
    topn_url, topn_name = topn
#    print(topn_url)
#    print(topn_name)
 #   print()

# 再更深入搜尋資料→進階查詢
# 例如查出的書有幾個章節 info-chapters
r = requests.get(topn_url)
r.encoding = 'utf-8'
topn_soup = BeautifulSoup(r.text, 'html.parser')

chapter_list = topn_soup.find('div', class_='info-chapters flex flex-wrap')
chapter_count = 0  # 計算章節數
count_shift = 0  # 計算章節跳號數
for chapter in chapter_list.find_all('a'):
    # print(chapter['title'], chapter['href'])
    chapter_title = chapter['title']
    chapter_href = chapter['href']
    chapter_title_part = chapter_title.split()  # 把章節名用空白切開
    chapter_number = chapter_title_part[0]  # 第幾章
   # chapter_name = chapter_title[1:]  # 取除了第1個以外的
    chapter_name = "".join(chapter_title_part[1:])  # 將章節名稱轉化成名稱，這樣就不會有空格

    # 判斷取出的第x章是正規的
    if chapter_number.startswith("第") and chapter_number.endswith("章"):
        # print(chapter_number, '|', chapter_name, '|', chapter['href'])
        chapter_count += 1

        chapter_number = int(chapter_number[1:-1])
        if chapter_number != (chapter_count + count_shift):
            count_shift += chapter_number - chapter_count
            print("跳號:", chapter_title, count_shift)
            print(chapter_number)
            break

print("章節總數:", chapter_count)
print()
