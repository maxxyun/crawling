install ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time, random


def chromeWebdriver():
    chrome_service = ChromeService(executable_path=ChromeDriverManager().install())
    options = Options()
    options.add_experimental_option('detach', True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    options.add_argument(f'user-agent={user_agent}')    
    # options.add_argument('--headless')
    driver = webdriver.Chrome(service=chrome_service, options=options)
    return driver


url ='https://smartstore.naver.com/blmgshop/products/100061153/'
driver = chromeWebdriver()
driver.get(url)
time.sleep(2)

# review = driver.find_element(By.ID, 'REVIEW')  # xpath로 직접하면 필요없음
cnt = 1
for page in range(1, 3):
    lis = driver.find_element(By.XPATH, '//*[@id="REVIEW"]/div/div[3]/div/div[2]/ul').find_elements(By.TAG_NAME, 'li')
    for li in lis:
        print(li.text)
        print(f'review_count: {cnt}\n')
        cnt += 1
    time.sleep(random.uniform(0.5, 1))

    # 페이징 처리 부분 (다음 버튼)
    driver.find_element(By.XPATH, '//*[@id="REVIEW"]/div/div[3]/div/div[2]/div/div/a[12]')

driver.quit()