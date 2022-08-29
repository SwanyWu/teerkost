import requests
from cleanup import categorize, cleantext
import datetime
import json
from bs4 import BeautifulSoup

def returnOffers():

    SHOP = "lidl"
    URL = "https://www.lidl.nl/c/aanbiedingen/a10008785"


    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")

    collection = []

    for item in soup.find_all("li", {"class": "ACampaignGrid__item--product"}):
        
        offer = { "productId":"", 
                "product":"", 
                "productInfo":"", 
                "category":"", 
                "image":"", 
                "deal":"", 
                "price": 0, 
                "dateStart":"", 
                "dateEnd":"", 
                "link": "", 
                "shop":""
                }

        productId = ""
        title = ""
        description = ""
        date = ""
        price = 0
        imageUrl = ""
        link = ""

        detailElement = item.find("div", {"class":"detail__grids"})
        detailElementData = detailElement.attrs['data-grid-data']
        loadJsonList = json.loads(detailElementData)

        title = loadJsonList[0]['fullTitle']
        cleanTitle = cleantext.cleanUpTitle(title)
        offer.update({"product": cleanTitle})

        deal = loadJsonList[0]['gridLabel']
        if type(deal) != type(None):
            deal = deal.lower()
        else:
            discount = loadJsonList[0]['price']['discount']
            if type(discount) != type(None):
                discountPercentage = loadJsonList[0]['price']['discount']['percentageDiscount']
                if type(discountPercentage) != type(None):
                    deal = str(discountPercentage) + "% korting"
                else:
                    deal = ""
                    print("geen percentage voor "+ title)
                    print(loadJsonList[0])
            else:
              deal = ""

        price = loadJsonList[0]['price']['price']
        if type(price) == type(None):
            price = 0

        imageUrl = loadJsonList[0]['image']
        
        canonicalUrl = loadJsonList[0]['canonicalUrl']
        link = "https://www.lidl.nl" + canonicalUrl

        linkElement = canonicalUrl.split("/")
        linkElement.reverse()
        productId = linkElement[0]

        description = loadJsonList[0]['keyfacts']['description']
        if type(description) != type(None):
            cleanInfoText = cleantext.cleanUpInfo(description.strip())
        else:
            cleanInfoText = ""
        
        offer.update({"productInfo": cleanInfoText})
        category = categorize.findCategoryForProduct(cleanTitle, cleanInfoText)
        offer.update({"category": category})

        offer.update({"productId": productId})

        offer.update({"shop": SHOP})
        offer.update({"price": float(price)})
        offer.update({"image": imageUrl})
        offer.update({"link": link})
        offer.update({"deal": deal})

        date = loadJsonList[0]['ribbons'][0]['text']
        if len(date) != 0: # check if something of a date is found
            if "vanaf" in date: # check if only the startdate is provided
                date = date.replace("vanaf ", "")
                date = date.split(" ")
                date = date[1].split("/")
                dayStart = date[0]
                monthStart = date[1]
                currentYear = datetime.datetime.now().year
                fullDateStart = str(currentYear) + "-" + monthStart + "-" + dayStart
                offer.update({"dateStart": fullDateStart})
            else: # start and end date is provided
                date = date.split(" - ")
                dateStringEnd = date[1].split(" ")
                dateStringEnd = dateStringEnd[1].split("/")
                dayEnd = dateStringEnd[0]
                monthEnd = dateStringEnd[1]

                dateStringStart = date[0].split(" ")
                dateStringStart = dateStringStart[1].split("/")
                dayStart = dateStringStart[0]
                monthStart = dateStringStart[1]

                currentYear = datetime.datetime.now().year

                fullDateEnd = str(currentYear) + "-" + monthEnd + "-" + dayEnd
                fullDateStart = str(currentYear) + "-" + monthStart + "-" + dayStart 
                
                offer.update({"dateStart": fullDateStart})
                offer.update({"dateEnd": fullDateEnd})

        if(offer.get('deal') != ""): # if no deal is found, don't add it
            collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de Lidl bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    returnOffers() 