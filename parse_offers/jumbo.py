import requests
from datetime import datetime
from cleanup import categorize, cleantext

def return_offers():
    SHOP = "jumbo"
    URL = "https://mobileapi.jumbo.com/v17/promotions"

    HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:81.0) Gecko/20100101 Firefox/81.0'
    }

    r = requests.get(url=URL, headers=HEADERS)
    data = r.json()

    collection = []

    for i in data['sections'][0]['current']['promotions']:
        if "zegels" not in i['tag'] and "bezorgkorting" not in i['tag'] and "bestelkosten" not in i['tag']:
            offer = {
                "productId": "",
                "product":"", 
                "productInfo":"", 
                "category":"", 
                "image":"", 
                "deal":"",
                "price": float(0), 
                "percentage":0,
                "dateStart":"", 
                "dateEnd":"", 
                "link": "", 
                "shop":""
            }

            clean_title = cleantext.clean_up_title(i['name'])
            offer.update({"product": clean_title})

            clean_info = cleantext.clean_up_info(i['summary'])
            offer.update({"productInfo": clean_info})

            offer.update({"productId": i['id']})

            category = categorize.find_category(clean_title, clean_info)
            offer.update({"category": category})

            offer.update({"shop": SHOP})

            deal = i['tag']
            percentage = 0
            if "2e halve prijs" in deal:
                percentage = 25
            elif "gratis" in deal and "+" in deal:
                deal_split = deal.replace(" gratis", "").split("+")
                hoeveel_betalen = int(deal_split[0])
                hoeveel_halen = int(deal_split[0]) + int(deal_split[1])
                calculate_percentage = (1 - (hoeveel_betalen/hoeveel_halen)) * 100
                percentage = int(float(calculate_percentage))
            elif "% korting" in deal:
                deal = deal.replace(" stuks", "")
                deal_split = deal.split("%")
                if len(deal_split) <= 2:
                    percentage = int(deal_split[0])

            offer.update({"deal": deal})

            price = float(0)
            if "voor € " in deal: # when "voor €" is found, the price can be calculated
                deal = deal.split("voor € ")
                price = deal[1]
                price = price.replace(",", ".")
                price = price.replace(" euro", "")
                price = float(price)
                price = float(format(price, '.2f'))
            
            offer.update({"price": price})

            if "promotionImage" in i:
                offer.update({"image": i['promotionImage']['main']})
            else:
                print("Geen afbeelding gevonden bij " + clean_title + ".")

            start_date = datetime.fromtimestamp(i['fromDate']/1000).strftime('%Y-%m-%d')
            end_date = datetime.fromtimestamp(i['toDate']/1000).strftime('%Y-%m-%d')
            offer.update({"dateStart": str(start_date)})
            offer.update({"dateEnd": str(end_date)})

            offer.update({"link": "https://jumbo.com/aanbiedingen/" + i['id']})
            collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de Jumbo bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    return_offers()