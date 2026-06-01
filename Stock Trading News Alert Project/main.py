import smtplib
import requests
import html

from_my_email = "Your sender Email"
email = "Your receiver Email"
password = "Your password"

# FOR STOCKS----------------------------------------
STOCK_KEY = "Your key" #pythonEmailKey
STOCK_END_POINT = "https://www.alphavantage.co/query"
STOCK_TAG = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_TAG,
    "apikey": STOCK_KEY,
}

# FOR NEWS------------------------------------------
NEWS_KEY = "3ce7aa43a7204bdbb60775baf89099c8"
NEWS_END_POINT = "https://newsapi.org/v2/everything"

NEWS_PARAMS = {
    "qInTitle": COMPANY_NAME,
    "apikey": NEWS_KEY,
    # "language": "en"
}

# ------------------------------------------STOCKS REQUESTS--------------------------------------------------

response = requests.get(STOCK_END_POINT, params=STOCK_PARAMS)
response.raise_for_status()
stock_data = response.json()
print(stock_data)


# Params to use with Global quote
# print(stock_data["Global Quote"]["05. price"])
# print(stock_data["Global Quote"]["08. previous close"])

# Params to use with daily series
# Creates a list with the dict keys
# days_list = list(stock_data["Time Series (Daily)"].keys())
days_list = [key for (key, value) in stock_data["Time Series (Daily)"].items()]#List comprehension to get all the keys to search the values
previous_close = days_list[1]
previous_previous_close = days_list[2]

p_stock_value = stock_data["Time Series (Daily)"][previous_close]["4. close"]
pp_stock_value = stock_data["Time Series (Daily)"][previous_previous_close]["4. close"]
print(p_stock_value)
print(pp_stock_value)

# p_stock_value = 350.120
# pp_stock_value = 360.130

up_down_value = float(p_stock_value) - float(pp_stock_value)
up_down_value_percent = (float(p_stock_value) - float(pp_stock_value))/float(pp_stock_value)*100
percent = round(up_down_value_percent, 2)

# ------------------------------------------NEWS REQUESTS--------------------------------------------------
# if percent > 5:

article_news = requests.get(NEWS_END_POINT, params=NEWS_PARAMS)
article_news.raise_for_status()
news_data = article_news.json()["articles"]
three_articles = news_data[:3]

edited_three_articles = [f"Headline: {news_data['title']}. \nBrief: {news_data['description']}" for news_data in three_articles]
print(edited_three_articles)

for i in range(0, 2):

    edited_three_articles = edited_three_articles[i].encode("ascii", "ignore").decode()
    print(edited_three_articles)

    if percent > 0:
        up_down_header = f"{STOCK_TAG} up over {percent}%"
    else:
        up_down_header = f"{STOCK_TAG} down over {percent}%"

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(from_my_email, password)
        connection.sendmail(from_addr=from_my_email, to_addrs=email,
                            msg=f"Subject: {up_down_header}\n\n{edited_three_articles}")








