import requests
from datetime import datetime
from cleanup import categorize, cleantext

def returnOffers(): 
    SHOP = "ah"

    URL = "https://www.ah.nl/bonus/api/segments?segmentType=-PREMIUM"
    
    r = requests.get(url = URL)
    
    data = r.json()

    collection = []

    for i in data['collection']:
        offer = {"productId": "","product":"", "productInfo":"", "category":"", "image":"", "deal":"", "price": 0, "dateStart":"", "dateEnd":"", "link": "", "shop":""}
        try:
            if i['segmentType'] == "AH" and i['category'] != 'Koken, tafelen, vrije tijd' and "bezorging" not in i['shields'][0]['text'] and "miles" not in i['shields'][0]['text']:
                
                offer.update({"productId": i['id']})
                cleanTitle = cleantext.cleanUpTitle(i['title'])
                offer.update({"product": cleanTitle})
                
                cleanInfo = cleantext.cleanUpInfo(i['description'])
                offer.update({"productInfo": cleanInfo})

                category = categorize.findCategoryForProduct(cleanTitle, cleanInfo)
                offer.update({"category": category})

                offer.update({"shop": SHOP})

                calculateDeal = 0
                if('price' in i):
                    priceNow = i['price']['now']
                    priceNow = "{:.2f}".format(priceNow)
                    try:
                        priceOld = i['price']['was']

                        calculateDeal = int((1 - (float(priceNow)/float(priceOld))) * 100)
                    except KeyError:
                        pass
                    
                    offer.update({"price": float(priceNow)})
                

                if('shields' in i):
                    shield = i['shields'][0]['text']
                    dealString = " ".join(str(x) for x in shield)
                    if "nu voor" in dealString and calculateDeal != 0: # when "nu voor" is found, use discount percentage as deal
                        deal = str(calculateDeal) + "% korting"
                    else:
                        deal = dealString

                    if "2e gratis" in dealString:
                        deal = "1+1 gratis"

                if "voor" in deal.lower() and "€" not in deal:
                    deal = deal.replace('voor', 'voor €')
                    
                offer.update({"deal": deal})

                offer.update({"image": i['image']['src']})

                href = i['href']

                startDateValidity = i['validityPeriod']['start']
                endDateValidity = i['validityPeriod']['end']

                offer.update({"dateStart": startDateValidity})
                offer.update({"dateEnd": endDateValidity})

                offer.update({"link": "https://ah.nl" + i['href']})
                collection.append(offer)
        except IndexError:
            print("Aanbieding met titel " + i['title'] + " heeft een element niet, dus overgeslagen.")


    print("📄 " + str(len(collection)) + " aanbiedingen van de Albert Heijn bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    returnOffers()