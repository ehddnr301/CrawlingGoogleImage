from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager

import os
import time


SEARCH_TERM = "아이유"  # will also be the name of the folder
URL = "https://www.google.co.in/search?q=" + SEARCH_TERM + "&source=lnms&tbm=isch"

browser = webdriver.Chrome(ChromeDriverManager().install())

browser.get(URL)

# User-Agent를 통해 봇이 아닌 유저정보라는 것을 위해 사용
header = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
}
# 이미지 카운트 (이미지 저장할 때 사용하기 위해서)
counter = 0
succounter = 0

print(os.path)
# 소스코드가 있는 경로에 '검색어' 폴더가 없으면 만들어준다.(이미지 저장 폴더를 위해서)
if not os.path.exists(SEARCH_TERM):
    os.mkdir(SEARCH_TERM)

for _ in range(500):
    # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    browser.execute_script("window.scrollBy(0,10000)")

for _ in range(1):
    browser.find_element_by_class_name("mye4qd").click()

for _ in range(500):
    # 가로 = 0, 세로 = 10000 픽셀 스크롤한다.
    browser.execute_script("window.scrollBy(0,10000)")

time.sleep(10)

search_results = browser.find_elements_by_class_name("bRMDJf")
print(search_results)

for index, search_result in enumerate(search_results):
    search_result.screenshot(f"{SEARCH_TERM}/{SEARCH_TERM}x{index}.png")


print(succounter, "succesfully downloaded")
browser.quit()
