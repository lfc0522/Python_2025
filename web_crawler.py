from bs4 import BeautifulSoup
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

# print(soup.prettify())
# 取HTML,但找到第一個就停
# print(soup.p.b)  #指找到標籤有<p>跟<b>的
# print(soup.a)  #找整份html有<a> 的標籤 or print(soup.p.b.a)
# print(soup.title) #指找到標籤有<title>的
# print(soup.p["class"])  # 指找到標有<p>且內部屬性有class的，用中括號來找
# 找所有的個標籤
print(soup.find_all('a'))  # 指找到所有的標籤<a>
