from xml.etree.ElementTree import ElementTree
import requests
from cleanup import categorize, cleantext
from datetime import datetime
from bs4 import BeautifulSoup

def returnOffers():

    SHOP = "spar"
    URL = "https://www.spar.nl/aanbiedingen/"


    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")

    elementWithDates = soup.select_one(".c-featured-promo__content")
    if elementWithDates != None:
        content = elementWithDates.find("div", {"class":"content"}).get_text().strip()
        if "de aanbiedingen uit deze folder zijn geldig van" in content:
            splitContent = content.split(" ")
            # de aanbiedingen uit deze folder zijn geldig van 21-07-2022 t/m 03-08-2022
            splitContent.reverse()
            # 03-08-2022 t/m 21-07-2022 van geldig zijn folder deze uit aanbiedingen de
            dateStart = splitContent[2]
            dateStartString = datetime.strptime(dateStart, "%d-%m-%Y").date()
            dateEnd = splitContent[0]
            dateEndString = datetime.strptime(dateEnd, "%d-%m-%Y").date()
        else:
            print("Kan geen info vinden over start- en einddatum!")


    collection = []
    for item in soup.find_all("div", {"class": "c-product-tile"}):
        offer = {"productId":"", 
        "product":"", 
        "productInfo":"", 
        "category":"", 
        "image":"", 
        "deal":"", 
        "price": float("0"), 
        "dateStart":"",
        "dateEnd":"", 
        "link": "", 
        "shop":""}

        cleanTitle = ""
        cleanInfoText = ""

        metaElement = item.find("div", {"class":"c-product-tile__meta"})
        titleElement = metaElement.find("a")
        if titleElement != None:
            title = titleElement.get_text().strip()  
            cleanTitle = cleantext.cleanUpTitle(title)
            offer.update({"product": cleanTitle})

        descrElement = metaElement.find("span")
        if descrElement != None:
            description = descrElement.get_text().strip()
            cleanInfoText = cleantext.cleanUpInfo(description)
            offer.update({"productInfo": cleanInfoText})
        
        category = categorize.findCategoryForProduct(cleanTitle, cleanInfoText)
        offer.update({"category": category})

        imageTile = item.find("div", {"class":"c-product-tile__image"})
        imageSrc = imageTile.find("img")
        if imageSrc != None:
            imageUrl = imageSrc['data-src']
            offer.update({"image": imageUrl})

        fullLink = ""
        linkElement = imageTile.find("a")
        if linkElement != None:
            link = linkElement['href']
            # https://www.spar.nl/aanbiedingen/kip-aanbieding-6861/
            fullLink = "https://spar.nl" + link
            offer.update({"link": fullLink})

            idFromLink = link.split("/")
            idFromLink.reverse()
            productId = idFromLink[1]
            offer.update({"productId": productId})
        
        offer.update({"shop": SHOP})

        priceElement = item.find("div", {"class":"c-product-tile__image--pricing"})
        if priceElement != None:
            oldPrice = priceElement.find("span", {"class":"c-price__old"})
            if oldPrice != None:
                newPrice = priceElement.find("span", {"class":"is-danger"})
                if newPrice != None:
                    base = newPrice.find("span", {"class":"c-price__base"}).get_text().strip()
                    decimal = newPrice.find("span", {"class":"c-price__mod"}).get_text().strip()
                    newPrice = base + decimal
                    newPrice = newPrice.rstrip(".-")
                    oldPrice = oldPrice.get_text().strip().rstrip(".-")
                    offer.update({"price": float(newPrice)})

                    calculateDeal = int((1 - (float(newPrice)/float(oldPrice))) * 100)
                    deal = str(calculateDeal) + "% korting"
                    offer.update({"deal": deal })    
                else:
                    print("Geen nieuwe prijs, geen deal")
            else:
                print("geen oude prijs, geen deal")
        else:
            # Geen prijs te zien, dus pagina van aanbieding zelf openen
            # FIXME prijs berekenen op basis van promotion tekst
            if fullLink != "":
                r = requests.get(fullLink)
                soup = BeautifulSoup(r.content, "html.parser")
                promotionSummary = soup.find("div", {"class":"c-promotion-summary__content"})
                promotionSummaryDeal = promotionSummary.select_one("strong")
                if promotionSummaryDeal != None:
                    promotion = promotionSummary.get_text().strip()
                    if len(promotion) > 20:
                        promotionSplitted = promotion.split("voor")
                        promotionSplitted.reverse()
                        deal = "voor" + promotionSplitted[0]
                        offer.update({"deal": deal })    
                    else:    
                        deal = promotion
                        offer.update({"deal": deal })
                else:
                    print("Kan geen deal vinden op productpagina!")            
            else:
                print("Geen prijs en geen URL")

        offer.update({"dateStart": str(dateStartString)})
        offer.update({"dateEnd": str(dateEndString)})
        if(offer.get('deal') != ""): # if no deal is found, don't add it
            collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de "+SHOP+" bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    returnOffers() 