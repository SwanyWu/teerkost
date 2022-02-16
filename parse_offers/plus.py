import requests
import categorize
from bs4 import BeautifulSoup

def returnOffers():

    SHOP = "Plus"
    URL = "https://www.plus.nl/aanbiedingen"

    URL2 = "https://www.plus.nl/INTERSHOP/web/WFS/PLUS-website-Site/nl_NL/-/EUR/ViewPromotions-LoadNextPromotions"

    cookies = {
        'nlbi_1876175':'e4SOXj4wxT3LtTbwQmr54wAAAABFLluA6P+abpYW4eWEkoJ7',
        'incap_ses_282_1876175':'RIRDRNXvIzJKQwkyG97pA3i5/2EAAAAAU4DdqWjhRtDtf08jTkP98Q==',
        'visid_incap_1876175':'u/aqxwzYSKG3ah1XtpcO4ne5/2EAAAAAQUIPAAAAAABgsLX0Np5ts4cjVUjxajNh'
    }

    headers = {
        'Host': 'www.plus.nl',
        'Accept': 'text/html,application/xhtml+xml,application/xml',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    # r = requests.get(URL, headers=headers, cookies=cookies)
    r = requests.post(URL2, headers, cookies=cookies)
    soup = BeautifulSoup(r.content, "html.parser")
    collection = []

    print(soup)
    # for item in soup.find_all("p", {"class": "product-tile__description"}):
    #     offer = {"product": "",
    #              "productInfo": "",
    #              "category": "",
    #              "image": "",
    #              "deal": "",
    #              "price": 0,
    #              "dateStart": "",
    #              "dateEnd": "",
    #              "link": "",
    #              "shop": ""}

    #     title = ""
    #     description = ""
    #     date = ""
    #     price = ""
    #     oldPrice = ""
    #     priceLabel = ""
    #     priceLowerLabel = ""
    #     priceLabelOnImage = ""
    #     imageUrl = ""
    #     link = ""

    #     titleElement = item.find("li", {"class": "ish-productList-item"})
    #     if titleElement != None:
    #         title = titleElement

    #     # category = categorize.findCategoryForProduct(title, description)
    #     # offer.update({"category": category})
    #     # offer.update({"product": title })
    #     # offer.update({"productInfo": concatDescription.strip()})

    #     # offer.update({"shop": SHOP})
    #     # offer.update({"price": price})
    #     # offer.update({"image": imageUrl})
    #     # offer.update({"link": "https://www.lidl.nl" + link})

    #     # offer.update({"dateStart": str(startDate)})
    #     # offer.update({"dateEnd": str(endDate)})

    #     print("ping")
    #     print('item gevonden ->' + title)
    #     # print(title)
    #     collection.append(offer)

    # return collection
