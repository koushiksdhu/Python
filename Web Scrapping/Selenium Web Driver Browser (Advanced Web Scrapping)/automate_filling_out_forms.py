from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# article_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# article_count.click()   # To click on the article count using selenium.

# Finding element by LINK TEXT:
# all_portal = driver.find_element(By.LINK_TEXT, "Wikibooks")
# all_portal.click()

# Search:
# search = driver.find_element(
#     By.XPATH, '//*[@id="searchform"]/div/div/div[1]/input')
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


# AUTOFILL AND SUBMIT:

driver.get("http://secure-retreat-92358.herokuapp.com/")

fname = driver.find_element(By.NAME, "fName")
fname.send_keys("Koushik")
lname = driver.find_element(By.NAME, "lName")
lname.send_keys("Sadhu")
email = driver.find_element(By.NAME, "email")
email.send_keys("kkoushikssadhu@gmail.com")

button = driver.find_element(By.XPATH, "/html/body/form/button")
button.click()
