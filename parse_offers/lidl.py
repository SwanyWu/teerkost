import requests
import categorize
from bs4 import BeautifulSoup

def returnOffers():

    SHOP = "Lidl"
    URL = "https://www.lidl.nl/c/aanbiedingen/a10008785"


    r = requests.get(URL)
    soup = BeautifulSoup(r.content)
    # FIXME add features="lxml"

    collection = []

    for item in soup.find_all("li", {"class": "ACampaignGrid__item"}):
        offer = {"product":"", "productInfo":"", "category":"", "image":"", "deal":"", "price": 0, "dateStart":"", "dateEnd":"", "link": "", "shop":""}

        titleElement = item.find("h2", {"class":"product-grid-box__title"})
        if titleElement != None:
            title = titleElement.get_text()
            title.strip()
        else:
            title = ""

        descrElement = item.find("div", {"class":"product-grid-box__desc"})
        if descrElement != None:
            description = descrElement.get_text()
            description.strip()
        else:
            description = ""
        
        dateElement = item.find("p", {"class":"image-ribbons__ribbon--blue"})
        if dateElement != None:
            date = dateElement.get_text()
        else:
            date = ""

        priceElement = item.find("div", {"class":"m-price__price--small"})
        if priceElement != None:
            price = priceElement.get_text()
        else:
            price = ""

        priceLabelElement = item.find("div", {"class":"m-price__label"})
        if priceLabelElement != None:
            priceLabel = priceLabelElement.get_text()
        else:
            priceLabel = ""

        # TODO creating collection: add product image
        # TODO creating collection: parse start and end date
        # TODO creating collection: add offer info
        # TODO add product url


        offer.update({"product": title })
        offer.update({"productInfo": description + ". " + priceLabel})

        category = categorize.findCategoryForProduct(title, description)
        offer.update({"category": category})

        offer.update({"shop": SHOP})
        # offer.update({"deal": i['tag']})
        # offer.update({"image": image})
        # offer.update({"dateStart": str(startDate)})
        # offer.update({"dateEnd": str(endDate)})
        # offer.update({"link": "https://jumbo.com/aanbiedingen/" + i['id']})

        print(title + " - " + price + " - " + date)

        collection.append(offer)

    return collection