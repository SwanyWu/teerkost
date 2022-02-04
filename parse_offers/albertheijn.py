import requests
from datetime import datetime
import categorize

def returnOffers(): 
    SHOP = "AH"

    URL = "https://www.ah.nl/bonus/api/segments?segmentType=-PREMIUM"
    
    r = requests.get(url = URL)
    
    data = r.json()

    collection = []

    for i in data['collection']:
        offer = {"product":"", "productInfo":"", "category":"", "image":"", "deal":"", "price": 0, "dateStart":"", "dateEnd":"", "link": "", "shop":""}
        offer.update({"product": i['title']})
        offer.update({"productInfo": i['description']})

        category = categorize.findCategoryForProduct(i['title'], i['description'])
        offer.update({"category": category})

        offer.update({"shop": SHOP})

        calculateDeal = 0
        if('price' in i):
            priceNow = i['price']['now']
            try:
                priceOld = i['price']["was"]
                calculateDeal = int((1 - (float(priceNow)/float(priceOld))) * 100)
            except KeyError:
                print("Geen oude prijs gevonden, we berekenen geen korting.")

            offer.update({"price": priceNow})
        

        if('shields' in i):
            shield = i['shields'][0]['text']
            dealString = " ".join(str(x) for x in shield)
            if "nu voor" in dealString and calculateDeal != 0: # indien "nu voor" wordt de korting in de deal gezet
                offer.update({"deal": str(calculateDeal) + "% korting"})
            else:
                offer.update({"deal": dealString })

        offer.update({"image": i['image']['src']})

        href = i['href']
        weekNumber = href.split("week=")[-1]
        now = datetime.now()
        startDate = str(datetime.fromisocalendar(now.year, int(weekNumber), 1))
        endDateTime = str(datetime.fromisocalendar(now.year, int(weekNumber), 7))

        startDate = endDateTime.split(" ")
        endDate = endDateTime.split(" ")
        offer.update({"dateStart": startDate[0]})
        offer.update({"dateEnd": endDate[0]})
        
        offer.update({"link": "https://ah.nl" + i['href']})
        collection.append(offer)

    return collection