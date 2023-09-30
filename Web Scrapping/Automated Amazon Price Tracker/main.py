from bs4 import BeautifulSoup
import requests
import lxml
from send_email import Email

Email = Email()

url = "https://www.amazon.in/Apple-iPhone-Pro-Deep-Purple/dp/B0BDJ48V1N/ref=sr_1_2_sspa?crid=1USHFQ6P0K9RT&keywords=iphone+15+pro+max&qid=1695448510&sprefix=iphone+15+pro%2Caps%2C221&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

req = requests.get(url, headers=header)
soup = BeautifulSoup(req.content, 'lxml')
# print(soup.prettify())
price = soup.find(class_="a-offscreen").get_text()
price = float(price.split('₹')[1].replace(',', ''))
# print(price)

BUY_PRICE = 2_00_000

if price < BUY_PRICE:
    product_name = soup.find(id="productTitle").get_text().strip()
    text = f"Price of {product_name} is {price}. You can purchase it from the below link."
    message = f"Subject: Amazon Price Alert! \n\n{text}\n\n Link: {url}".encode(
        "utf-8")
    Email.send("kkoushikssadhu@gmail.com", message)
