import requests
import os
from newsapi import NewsApiClient
# import datetime as dt


STOCK = "TCS"
# API key= "918L0T3H2OOPSBIU" (STOCK API)
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=RELIANCE.BSE&outputsize=full&apikey=demo
# Your API key is: 3c05b6fef51845b0b80f1d9917a2b368 (NewsAPI)

ENDPOINT_STOCK = "https://www.alphavantage.co/query"
PARAMETERS_STOCK = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "full",
    "apikey": os.environ.get('STOCK_API_KEY')   # setx STOCK_API_KEY 918L0T3H2OOPSBIU
}



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

req_stock = requests.get(ENDPOINT_STOCK, params=PARAMETERS_STOCK)
print(f"Status Code: {req_stock.status_code}")
req_stock.raise_for_status()
stock_data = req_stock.json()

# yesterday_closing_price = stock_data["Time Series (Daily)"][str(dt.date.today() - dt.timedelta(days=2))]["4. close"]
# today_opening_price = stock_data["Time Series (Daily)"][str(dt.date.today() - dt.timedelta(days=1))]["1. open"]
# print(f"Yesterday Closing Price: {yesterday_closing_price}")
# print(f"Today Opening Price: {today_opening_price}")

stock_data = stock_data['Time Series (Daily)']
data_list = [value for(key, value) in stock_data.items()]       # List Comprehension
# print(data_list)

yesterday_closing_price = data_list[0]['4. close']
print(f"Yesterday Closing Price: {yesterday_closing_price}")

day_before_yesterday_closing_price = data_list[1]['4. close']
print(f"Day Before Yesterday Closing Price: {day_before_yesterday_closing_price}")

difference_price = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
print(f"Difference in Price: {int(difference_price)}")

percentage_difference = (difference_price / float(yesterday_closing_price)) * 100
print(f"Percentage Difference: {'{:.2f}'.format(percentage_difference)}")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    
def news(topic) -> []:
    NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"
    NEWS_API_PARAMETER = {
        "qInTitle": topic,
        "from": "2023-09-01",
        "sortBy": "popularity",
        "apiKey": os.environ.get('NEWS_API_KEY')   # setx NEWS_API_KEY 3c05b6fef51845b0b80f1d9917a2b368
    }
    
    newsapi_req = requests.get(NEWS_API_ENDPOINT, params=NEWS_API_PARAMETER)
    newsapi_req.raise_for_status()
    print(newsapi_req.status_code)
    newsapi_data = newsapi_req.json()
    return newsapi_data["articles"][:3]


if(percentage_difference > 0.5):
    global first_three_articles 
    first_three_articles = news(STOCK+" Stocks")
    
# print(first_three_articles)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

formatted_articles = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in first_three_articles]
print(formatted_articles)


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

