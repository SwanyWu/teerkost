import requests
from datetime import datetime
from cleanup import categorize, cleantext

def returnOffers(): 
    SHOP = "dirk"

    api_key = "6d3a42a3-6d93-4f98-838d-bcc0ab2307fd"
    categories = [1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,18]

    collection = []

    # TODO vanaf woensdag aanbiedings ook
    for categorie in categories:
        categorieString = str(categorie)
        
        URL = "https://api.dirk.nl/v1/offerscache/department/66/"+categorieString+"?api_key=" + api_key

        r = requests.get(url = URL)
        
        data = r.json()

        for i in data:
            offer = {"productId": "","product":"", "productInfo":"", "category":"", "image":"", "deal":"", "price": 0, "dateStart":"", "dateEnd":"", "link": "", "shop":""}

            offer.update({"productId": i['OfferID']})

            cleanTitle = cleantext.cleanUpTitle(i['HeaderText'])
            offer.update({"product": cleanTitle})

            description = i['Packaging']
            if description != None:
                cleanInfo = cleantext.cleanUpInfo(description)
                offer.update({"productInfo": cleanInfo})

            price = i['OfferPrice'];
            offer.update({"price": float(price)})

            if i['NormalPrice'] != None:
                oldPrice = i['NormalPrice']
                calculateDeal = int((1 - (float(price)/float(oldPrice))) * 100)
                offer.update({"deal": str(calculateDeal) + "% korting" })
            else:
                offer.update({"deal": "€" +str(price) })
                # FIXME misschien zijn er andere type deals
            
            fullDateStart = i['StartDate']
            startDate = datetime.fromisoformat(fullDateStart).date()
            offer.update({"dateStart": str(startDate)})

            fullDateEnd = i['EndDate']
            endDate = datetime.fromisoformat(fullDateEnd).date()
            offer.update({"dateEnd": str(endDate)})

            if i['ProductOffers'][0]['Product']['ProductPicture']['Url'] != None:
                imageUrl = i['ProductOffers'][0]['Product']['ProductPicture']['Url'] + "?width=170&height=170&mode=crop"
                offer.update({"image": imageUrl})

            if i['OfferUrls'][0]['Url'] != None:
                # https://www.dirk.nl/aanbiedingen/ambachtelijke-salade/84338
                offerId = str(i['OfferID'])
                offerUrl = i['OfferUrls'][0]['Url']
                url = "https://www.dirk.nl/aanbiedingen/" + offerUrl + "/" + offerId
                offer.update({"link": url})

            category = categorize.findCategoryForProduct(cleanTitle, cleanInfo)
            offer.update({"category": category})

            offer.update({"shop": SHOP})

            collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de Dirk bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    returnOffers()