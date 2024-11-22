import requests
from bs4 import BeautifulSoup

urls = "https://www.weather.go.kr/w/index.do"
#weather_info = requests.get(url)
#soup = BeautifulSoup(weather_info.text, "html.parser")

#current-weather > div.cmp-cur-weather.wbg.wbg-type2.BGDB00 > ul.wrap-1 > li.w-icon.w-temp.no-w > span.tmp
#print(soup.select('span.tmp'))

import selenium

#브라우저가 프로그램 종료시 사라지지 않는 옵션
from selenium.webdriver.chrome.options import Options
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#크롬 브라우저 객체를 생성
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.weather.go.kr/w/index.do")

#암시적 대기 /요소가 로드될때까지 대기
driver.implicitly_wait(5)

tmp_element = driver.find_element(by=By.CSS_SELECTOR, value='span.tmp')
print(tmp_element.text)

#모든 find_element 메서드에 적용됩니다.
#한 번 설정하면 WebDriver 세션 전체에 적용됩니다.
#요소를 찾을 때마다 최대 지정된 시간(이 경우 5초)까지 기다립니다.