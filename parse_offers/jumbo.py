import requests
from datetime import datetime
from cleanup import categorize, cleantext
  

def returnOffers():
    SHOP = "Jumbo"
    URL = "https://mobileapi.jumbo.com/v17/promotions"
    
    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0'
    }

    r = requests.get(url=URL, headers=HEADERS)
    
    data = r.json()

    collection = []

    for i in data['sections'][0]['current']['promotions']:
        if "bezorgkorting" not in i['tag'] and "bestelkosten" not in i['tag']:
            offer = {"product":"", "productInfo":"", "category":"", "image":"", "deal":"", "price": 0, "dateStart":"", "dateEnd":"", "link": "", "shop":""}
            
            cleanTitle = cleantext.cleanUpTitle(i['name'])
            offer.update({"product": cleanTitle})
            offer.update({"productInfo": i['summary']})

            category = categorize.findCategoryForProduct(cleanTitle, i['summary'])
            offer.update({"category": category})

            offer.update({"shop": SHOP})

            deal = i['tag']
            offer.update({"deal": deal})
            if "voor € " in deal: # when "voor €" is found, the price can be calculated
                deal = deal.split("voor € ")
                price = deal[1]
                offer.update({"price": price.replace(",", ".")})

            offer.update({"image": i['promotionImage']['main']})

            startDate = datetime.fromtimestamp(i['fromDate']/1000).strftime('%Y-%m-%d')
            endDate = datetime.fromtimestamp(i['toDate']/1000).strftime('%Y-%m-%d')
            offer.update({"dateStart": str(startDate)})
            offer.update({"dateEnd": str(endDate)})
            
            offer.update({"link": "https://jumbo.com/aanbiedingen/" + i['id']})
            collection.append(offer)

    return collection