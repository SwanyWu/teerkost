import requests
from cleanup import categorize, cleantext
import datetime
from bs4 import BeautifulSoup

def returnOffers():

    SHOP = "Lidl"
    URL = "https://www.lidl.nl/c/aanbiedingen/a10008785"


    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")

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

        # try and find information about the discount
        if (priceLabel.find("gratis") != -1) or (priceLabel.find("korting") != -1):
            offer.update({"deal": priceLabel.replace(".-", "")}) # option 1: pricelabel contains the discount info
        else:
            if priceLabelOnImage != "": # option 2: the discount is displayed on the image
                offer.update({"deal": priceLabelOnImage.replace(".-", "")})
            elif oldPrice != "" and price != "": # option 3: calculate the discount based on the price displayed
                oldPrice = oldPrice.replace(".-", "")
                price = price.replace(".-", "")
                calculateDeal = int((1 - (float(price)/float(oldPrice))) * 100)
                offer.update({"deal": str(calculateDeal) + "% korting"})

            concatDescription = concatDescription + " " + priceLabel # add pricelabel contents to the description
            
        cleanInfoText = cleantext.cleanUpInfo(concatDescription.strip())
        cleanTitle = cleantext.cleanUpTitle(title)
        offer.update({"productInfo": cleanInfoText})

        category = categorize.findCategoryForProduct(cleanTitle, description)
        offer.update({"category": category})
        offer.update({"product": cleanTitle})
        offer.update({"shop": SHOP})
        offer.update({"price": price})
        offer.update({"image": imageUrl})
        offer.update({"link": "https://www.lidl.nl" + link})

        if len(date) != 0: # check if something of a date is found
            if "vanaf" in date: # check if only the startdate is provided
                date = date.replace("vanaf ", "")
                date = date.split(" ")
                date = date[1].split("/")
                currentYear = datetime.datetime.now().year
                fullDateEnd = str(currentYear) + "-" + monthEnd + "-" + dayEnd
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