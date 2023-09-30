from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://www.flipkart.com/apple-iphone-13-midnight-128-gb/p/itmca361aab1c5b0?pid=MOBG6VF5Q82T3XRS&lid=LSTMOBG6VF5Q82T3XRSOXJLM9&marketplace=FLIPKART&q=Iphone&store=tyy%2F4io&spotlightTagId=BestsellerId_tyy%2F4io&srno=s_1_2&otracker=search&otracker1=search&fm=Search&iid=71e8f6bd-0fd9-4422-8631-683614857f0d.MOBG6VF5Q82T3XRS.SEARCH&ppt=sp&ppn=sp&ssid=zkwt6gpci80000001695539190609&qH=29e0a89b3149a9af")
# elements = driver.find_elements(By.CLASS_NAME, '_16Jk6d')
# list = [element.text for element in elements]
# print(list[0].replace(',', '')[1:])

# Using XPath:
price = driver.find_element(
    By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]')
print(price.text)

# driver.close()            # closes the current opened tab.
driver.quit()               # closes the browser.
