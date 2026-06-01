# from bs4 import BeautifulSoup
# import lxml #you can use it in the place of "html.parser"
# import requests
# import smtplib
# import os
# import dotenv
#
# dotenv.load_dotenv()
#
# FROM_MY_EMAIL = os.environ.get("from_my_email")
# PASSWORD = os.environ.get("passwword")
# EMAIL = os.environ.get("email")
#
# URL = "https://appbrewery.github.io/instant_pot/"
# header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36"}
#
# response = requests.get(URL, headers=header)
# soup = BeautifulSoup(response.content, "html.parser")
#
# price_symbol = soup.find(name="span", class_="a-price-symbol")
# price_whole = soup.find(name="span", class_="a-price-whole")
# price_fraction = soup.find(name="span", class_="a-price-fraction")
# img_title = soup.find(name="img", id="landingImage")
# title = img_title.get("alt")
# # print(price_symbol.text)
# # print(price_whole.text)
# total_price = float(f"{price_whole.text}{price_fraction.text}")
# print(f"{price_symbol.text}{total_price}")
#
# print(f"Subject: Amazon price alert!\n\n{title} is now {price_symbol.text}{total_price}:\n{URL}")
#
# if total_price < 100.00:
#     with smtplib.SMTP("smtp.gmail.com", 587) as connection:
#         connection.starttls()
#         connection.login(FROM_MY_EMAIL, PASSWORD)
#         msg = f"Subject: Amazon price alert!\n\n{title} is now {price_symbol.text}{total_price}:\n{URL}"
#         connection.sendmail(from_addr=FROM_MY_EMAIL, to_addrs=EMAIL,
#                             msg=msg.encode("utf-8"))#Avoid the msg to break


from bs4 import BeautifulSoup
import lxml #you can use it in the place of "html.parser"
import requests
import smtplib
import os
import dotenv

dotenv.load_dotenv()

FROM_MY_EMAIL = os.environ.get("from_my_email")
PASSWORD = os.environ.get("passwword")
EMAIL = os.environ.get("email")

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1"
}

response = requests.get(URL, headers=header)
soup = BeautifulSoup(response.content, "html.parser")

price_symbol = soup.find(name="span", class_="a-price-symbol")
price_whole = soup.find(name="span", class_="a-price-whole")
price_fraction = soup.find(name="span", class_="a-price-fraction")
img_title = soup.find(name="img", id="landingImage")
title = img_title.get("alt")
print(price_symbol.text)
print(price_whole.text)
print(price_fraction.text)
print(title)
total_price = float(f"{price_whole.text}{price_fraction.text}")
print(f"{price_symbol.text}{total_price}")

print(f"Subject: Amazon price alert!\n\n{title} is now {price_symbol.text}{total_price}:\n{URL}")

if total_price < 100.00:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(FROM_MY_EMAIL, PASSWORD)
        msg = f"Subject: Amazon price alert!\n\n{title} is now {price_symbol.text}{total_price}:\n{URL}"
        connection.sendmail(from_addr=FROM_MY_EMAIL, to_addrs=EMAIL,
                            msg=msg.encode("utf-8"))#Avoid the msg to break
