from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()))

driver.get("https://www.python.org/")
times = driver.find_elements(
    By.CSS_SELECTOR, '#content div section div.list-widgets.row div.medium-widget.event-widget.last div ul time')
time_list = [time.text for time in times]

names = driver.find_elements(
    By.CSS_SELECTOR, '#content div section div.list-widgets.row div.medium-widget.event-widget.last div ul li a')
name_list = [name.text for name in names]

events = {}

for i in range(len(name_list)):
    events[i] = {
        "Time": time_list[i],
        "Name": name_list[i]
    }

print(events)
