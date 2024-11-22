import requests
from bs4 import BeautifulSoup

import selenium

#브라우저가 프로그램 종료시 사라지지 않는 옵션
from selenium.webdriver.chrome.options import Options
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

urls = "https://www.weather.go.kr/w/index.do"

#크롬 브라우저 객체를 생성
driver = webdriver.Chrome(options=chrome_option)
driver.get(urls)

#명시적 대기 /요소가 로드될때까지 대기
wait = WebDriverWait(driver,10)
tmp_element = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, 'span.tmp'))
)
#tmp_element = driver.find_element(by=By.CSS_SELECTOR, value='span.tmp')
print(tmp_element.text)

# 특정 요소나 조건에 대해 개별적으로 적용됩니다.
# 다양한 기대 조건(Expected Conditions)을 사용할 수 있습니다.
# 요소가 나타날 때까지 또는 지정된 시간(이 경우 10초)이 경과할 때까지 기다립니다.
# 특정 요소의 상태를 정확히 확인할 수 있어, 테스트의 신뢰성과 안정성이 향상됩니다