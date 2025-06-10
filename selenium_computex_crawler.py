from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 使用瀏覽器開啟
# webdriver.Firefox()
# webdriver.safari()
# webdriver.Edge()
driver = webdriver.Chrome()
# driver.get("https://www.computextaipei.com.tw/zh-tw/index.html")
# 或者下列寫法 參展廠商列表從前100筆取vip的廠商資料
computex_url = "https://www.computextaipei.com.tw/zh-tw/exhibitor/show-area-data/index.html"
computex_url += "?pageSize=100"
driver.get(computex_url)

while
vip_vender = driver.find_elements(By.CLASS_NAME, 'vip')
for vender in vip_vender:
    vender_name = vender.find_element(By.TAG_NAME, 'h3')
    spans = vender.find_elements(By.XPATH, './/ul/li/span')
    ps = vender.find_elements(By.XPATH, './/ul/li/p')
    tags = vender.find_elements(By.XPATH, './/ul/li/a')
    print(vender_name.text)
    print("span:", [span.text for span in spans])  # 用list來做
    print("p:", [p.text for p in ps])

    # 合併zip ，取短的
    for key, value in zip(spans, ps):
        print(key.text, value.text)

    print("tags:", [tag.text for tag in tags])
    print()

    # 選頁數
    select_page_size = driver.find_element(By.ID, '//A[@AREA-LABEL="下一頁"]')

    # 下一頁取法
    nextpage = driver.find_element(By.XPATH, '//A[@AREA-LABEL="下一頁"]')
    if nextpage:
        nextpage.click()
    else:
        break

driver.quit()
