from bs4 import BeautifulSoup
import requests

yCombinator = requests.get("https://news.ycombinator.com/")

soup = BeautifulSoup(yCombinator.text, "html.parser")

# print(soup.select(".score"))
# score = [each.getText() for each in soup.select(".score")]
# print(score)

text = soup.find(name="a", class_="storylink")
print(text)
