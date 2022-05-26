pip install selenium
conda install selenium
pip install bs4

print("Hello World")

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.naver.com")