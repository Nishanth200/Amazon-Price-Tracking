import requests
from bs4 import BeautifulSoup
import smtplib

my_email = "xxxxx@gmail.com"
password = "xxxxxxx"
recipient_email = "yyyy@gmail.com"

product_link ="PRODUCT-link"
amazon_endpoint = product_link

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/118.0.0.0 Safari/537.36"


}

response = requests.get(amazon_endpoint, headers=headers)
webpage = response.text

soup = BeautifulSoup(webpage, 'lxml')

price = soup.select_one('span .a-price-whole').get_text().replace('.','').split(',')
price = float(''.join(price))

product_title = soup.find(name='span', id='productTitle').get_text().strip()

if price <= 50_000:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(password=password, user=my_email)
        connection.sendmail(to_addrs=recipient_email, from_addr=my_email, msg=f"{product_title} is now at Rs.{price}")

