from collections import Counter
from pprint import pprint
from bs4 import BeautifulSoup
import requests


def get_chapters(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = 'utf8'
        topn_soup = BeautifulSoup(r.text, 'html.parser')

        chapter_list = topn_soup.find(
            'div', class_='info-chapters flex flex-wrap')
        if not chapter_list:
            print(f"無法找到章節列表：{url}")
            return

        chapter_count = 0
        count_shift = 0
        for chapter in chapter_list.find_all('a'):
            chapter_title = chapter['title']
            chapter_url = chapter['href']
            chapter_title_parts = chapter_title.split()
            chapter_number = chapter_title_parts[0]
            chapter_name = "".join(chapter_title_parts[1:])
            if chapter_number.startswith("第") and chapter_number.endswith("章"):
                print(chapter_number, '|', chapter_name, '|', chapter_url)
                chapter_count += 1

                chapter_number = int(chapter_number[1:-1])
                if chapter_number != (chapter_count + count_shift):
                    count_shift += chapter_number - \
                        (chapter_count + count_shift)
                    print("跳號: ", chapter_title, count_shift)
        print("章節總數: ", chapter_count)
    except requests.RequestException as e:
        print(f"請求錯誤：{e}")
    except Exception as e:
        print(f"發生錯誤：{e}")


def get_top_novels_data():
    try:
        r = requests.get('https://www.twking.org/')
        r.raise_for_status()
        r.encoding = 'utf8'
        soup = BeautifulSoup(r.text, 'html.parser')

        booktop_data = {}
        booktops = soup.find_all('div', class_='booktop')
        for booktop in booktops:
            booktop_name = booktop.p.string
            booktop_data[booktop_name] = [
                (top['href'], top.string.strip()) for top in booktop.find_all('a')
            ]
            for top in booktop.find_all('a'):
                print(top['href'], top.string.strip())

        return booktop_data
    except requests.RequestException as e:
        print(f"請求錯誤：{e}")
    except Exception as e:
        print(f"發生錯誤：{e}")
        return {}


if __name__ == '__main__':
    booktop_data = get_top_novels_data()
    if booktop_data:
        top10_counter = Counter()
        for booktop_name in booktop_data:
            top10_counter.update(booktop_data[booktop_name])

        print('Get Top3')
        pprint(top10_counter.most_common(10))
        for topn, topn_count in top10_counter.most_common(10)[7:]:
            topn_url, topn_name = topn
            print(topn_url)
            print(topn_name)
            get_chapters(topn_url)
