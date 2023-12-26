import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

EMAIL_ADDRESS = 'Your Email Address'
PASSWORD = 'Your Password'
URL = "https://www.amazon.com/Sony-Playstation-Console-Disc-Version/dp/B095N5T4LB/ref=sr_1_3?crid=275MQUKWG6AHH&keywords=ps5&qid=1703585447&sprefix=ps5+%2Caps%2C427&sr=8-3"
headers = {
    'Accept-Language': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    'User-Agent': "en-US,en;q=0.9"
}

response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')
# print(soup.prettify())
title = soup.find(id="productTitle").get_text().strip()

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
Expected_price = float(550)


if price_as_float <= Expected_price:
    message = f"{title} is now {price}"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL_ADDRESS, password=PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
        )
