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

        title = ""
        description = ""
        date = ""
        price = ""
        oldPrice = ""
        priceLabel = ""
        priceLowerLabel = ""
        priceLabelOnImage = ""
        imageUrl = ""
        link = ""

        titleElement = item.find("h2", {"class":"product-grid-box__title"})
        if titleElement != None:
            title = titleElement.get_text().strip()  

        descrElement = item.find("div", {"class":"product-grid-box__desc"})
        if descrElement != None:
            description = descrElement.get_text().strip()
        
        dateElement = item.find("p", {"class":"image-ribbons__ribbon--blue"})
        if dateElement != None:
            date = dateElement.get_text().strip()

        priceElement = item.find("div", {"class":"m-price__price--small"})
        if priceElement != None:
            price = priceElement.get_text().strip()

        oldPriceElement = item.find("span", {"class":"m-price__rrp"})
        if oldPriceElement != None:
            oldPrice = oldPriceElement.get_text().strip()

        priceLabelElement = item.find("div", {"class":"m-price__label"})
        if priceLabelElement != None:
            priceLabel = priceLabelElement.get_text().lower().strip()

        priceLowerLabelElement = item.find("div", {"class":"m-price__base--labelled"})
        if priceLowerLabelElement != None:
            priceLowerLabel = priceLowerLabelElement.get_text().lower().strip()

        imageLabelElement = item.find("p", {"class":"image-labels__label--red"})
        if imageLabelElement != None:
            priceLabelOnImage = imageLabelElement.get_text().lower().strip()

        imageElement = item.find("img", {"class":"product-grid-box__image"})
        if imageElement != None:
            imageUrl = imageElement['src']

        linkElement = item.find("a", {"class":"product-grid-box"})
        if linkElement != None:
            link = linkElement['href']

        # collect and concat product information from description and lower price label
        if description != "":
            concatDescription = description
        else:
            concatDescription = ""
        if priceLowerLabel != "":
            concatDescription = concatDescription + " " + priceLowerLabel

        # find information about the discount and add it to field "deal"
        if (priceLabel.find("gratis") != -1) or (priceLabel.find("korting") != -1):
            offer.update({"deal": priceLabel.replace(".-", "")}) # most often contains the discount info
        else:
            if priceLabelOnImage != "":
                offer.update({"deal": priceLabelOnImage.replace(".-", "")}) # sometimes contains the discount
            elif oldPrice != "" and price != "":
                oldPrice = oldPrice.replace(".-", "")
                price = price.replace(".-", "")
                calculateDeal = int((1 - (float(price)/float(oldPrice))) * 100)
                offer.update({"deal": str(calculateDeal) + "% korting"}) # no discount info, then calculate the discount

            concatDescription = concatDescription + " " + priceLabel # add pricelabel contents to the description
            
        offer.update({"productInfo": concatDescription.strip()})

        category = categorize.findCategoryForProduct(title, description)
        offer.update({"category": category})
        offer.update({"product": title })
        offer.update({"shop": SHOP})
        offer.update({"price": price})
        offer.update({"image": imageUrl})
        offer.update({"link": "https://www.lidl.nl" + link})

        collection.append(offer)

    return collection