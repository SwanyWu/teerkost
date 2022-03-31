from optparse import TitledHelpFormatter
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from cleanup import categorize, cleantext
  
def returnWeekday(datestring):
    datestring = datestring.split("-")
    year = int(datestring[0])
    month = int(datestring[1])
    day = int(datestring[2])

    date = datetime(year,month,day)

    days = ["maandag", "dinsdag", "woensdag",
        "donderdag", "vrijdag", "zaterdag", "zondag"]

    weekday = date.weekday()

    return days[weekday]

def returnCalculatedDate(datestring, plusDays):
    datestring = datestring.split("-")
    year = int(datestring[0])
    month = int(datestring[1])
    day = int(datestring[2])

    date = datetime(year,month,day)
    newDate = date + timedelta(days=plusDays)
    newDateString = newDate.strftime('%Y-%m-%d')

    return str(newDateString)

def returnOffers():

    SHOP = "Aldi"
    URL = "https://www.aldi.nl/aanbiedingen.html?ftl-pty=Weekactie"

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")

    collection = []

    sectionDiv = "mod-offers__day"
    articleDiv = "mod-article-tile"
    articleTitleClass = "mod-article-tile__title"

    sectionIndex = 0
    for section in soup.find_all("div", {"class": sectionDiv}):
        startDateSection = section['data-rel']
        sectionIndex = sectionIndex + 1
        if returnWeekday(startDateSection) == 'maandag': # weekoffers only start on monday, ignore the rest
            for article in section.find_all("div", {"class", articleDiv}):
                offer = {"product":"", "productInfo":"", "category":"", "image":"", "deal":"", "price": 0, "dateStart":"", "dateEnd":"", "link": "", "shop":""}

                title = ""
                info = ""
                imageLink = ""
                price = ""
                oldPrice = ""
                priceLabel = ""
                deal = ""
                dateStart = startDateSection
                dateEnd = returnCalculatedDate(startDateSection, 6)
                link = ""

                titleElement = article.find("span", {"class",articleTitleClass})
                if titleElement != None:
                    title = titleElement.get_text().strip()

                infoElement = article.find("div", {"class", "price__meta"})
                if infoElement != None:
                    info = infoElement.get_text().strip()

                priceElement = article.find("span", {"class", "price__wrapper"})
                if priceElement != None:
                    price = priceElement.get_text().strip()

                oldPriceElement = article.find("s", {"class", "price__previous"})
                if oldPriceElement != None:
                    oldPrice = oldPriceElement.get_text().strip()

                priceLabelElement = article.find("span", {"class", "price__previous-percentage"})
                if priceLabelElement != None:
                    priceLabel = priceLabelElement.get_text().strip()

                imageElement = article.find("img", {"class", "img-responsive"})
                if imageElement != None:
                    imageSrcSet = imageElement['data-srcset']
                    imageSrcSet = imageSrcSet.split(" 288w")
                    imageLink = "https://www.aldi.nl" + imageSrcSet[0] # extract a link from the srcset attribute

                linkElement = article.find("a", {"class", "mod-article-tile__action"}) 
                if linkElement != None:
                    link = "https://www.aldi.nl" + linkElement['href']

                deal = ""
                if "%" in priceLabel: # a percentage is known, use it as the deal
                    priceLabel = priceLabel.replace("-", "").replace(" korting", "")
                    deal = str(priceLabel) + " korting"
                else:
                    if oldPrice != "" and price != "": # calculate the deal when old and new price is found
                        calculateDeal = int((1 - (float(price)/float(oldPrice))) * 100)
                        deal = str(calculateDeal) + "% korting"
                    else:
                        if "VOOR" in priceLabel or "Vanaf" in priceLabel:
                            deal = str(priceLabel.strip() + " " + price)
                        else:
                            deal = str(priceLabel)
                        deal = deal.lower()

                cleanTitle = cleantext.cleanUpTitle(title)
                cleanInfo = cleantext.cleanUpInfo(info)
                offer.update({"product": cleanTitle})
                offer.update({"productInfo": cleanInfo})
                offer.update({"category": categorize.findCategoryForProduct(cleanTitle, cleanInfo)})
                offer.update({"image": imageLink})
                offer.update({"deal": deal})
                offer.update({"price": price})
                offer.update({"dateStart": dateStart})
                offer.update({"dateEnd": dateEnd})
                offer.update({"link": link})
                offer.update({"shop": SHOP})
                
                if(offer.get('deal') != ""): # if no deal is found, don't add it
                    collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de Aldi bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    returnOffers()