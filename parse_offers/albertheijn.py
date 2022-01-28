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
        if('price' in i):
            offer.update({"price": i['price']['now']})
        
        if('shields' in i):
            shield = i['shields'][0]['text']
            toString = " ".join(str(x) for x in shield)
            offer.update({"deal": toString })

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