from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# 使用瀏覽器開啟
# webdriver.Firefox()
# webdriver.safari()
# webdriver.Edge()
driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
time.sleep(10)  # 開啟瀏覽器10秒後會自動quit
driver.implicitly_wait(10)  # 功能跟time.seep一樣，也可以這樣寫，但只在這個功能用

print("title=" + driver.title)
# 取節點的資料
driver.find_element(By.NAME, 'my-text')  # 找單個

text_box = driver.find_element(by=By.NAME, value="my-text")
submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")
readio_default = driver.find_element(
    By.XPATH, '//label/input[@id="my-readio-2"]')

print("default readio:", readio_default.is_selected())
readio_default.click()
# driver.find_elements()  # 找多個

text_box.send_keys("Selenium")  # 模擬人手動填入資料，輸入Selenium
submit_button.click()  # 模擬人手動按下按鈕
time.sleep(3)
message = driver.find_element(by=By.ID, value="message")
text = message.text

print("text:", text)
time.sleep(3)
driver.quit()  # 關掉瀏覽器
