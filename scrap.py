import requests
from bs4 import BeautifulSoup
import json


url ='http://books.toscrape.com/' 

def scrape_books(url):
    response = requests.get(url)

    if response.status_code != 200:
        return []

    response.encoding = response.apparent_encoding
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article",class_="product_pod")
    
    all_books = []
    for book in books:
        title = book.h3.a['title']
        price_text = book.find("p", class_='price_color').text
        currency = price_text[0]
        price = float(price_text[1:])
        print(title, price, currency)
        all_books.append(
            {
                "title": title,
                "price": price,
                "currency": currency,
            }
        )
    return all_books
books= scrape_books(url)
with open ("books.json","w") as f:

    json.dump(books,f,indent=4, ensure_ascii=False)
