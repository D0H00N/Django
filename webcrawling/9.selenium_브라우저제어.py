import selenium

#브라우저가 프로그램 종료시 사라지지 않는 옵션
from selenium.webdriver.chrome.options import Options
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(options=chrome_option)
driver.get("https://www.python.org/")

#검색어 입력요소에 'python'입력
#input_el = driver.find_element(by='id', value='id-search-field')
#input_el = driver.find_element(by=By.id, value='id-search-field')
input_el = driver.find_element(by=By.CSS_SELECTOR, value='#id-search-field')

input_el.send_keys('pycon')
input_el.send_keys(Keys.RETURN)

#검색결과 추출
#content > div > section > form > ul > li:nth-child(1) > h3 > a
input_el = driver.find_elements(by=By.CSS_SELECTOR, value='ul li h3 a')
for i_el in input_el:
    print(i_el.text)
#driver.close()