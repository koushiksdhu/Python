from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
print(f"Article count: {int(article_count.text.replace(',', ''))}")
