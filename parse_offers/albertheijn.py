import requests
from datetime import datetime
from cleanup import categorize, cleantext, cleandeal

def return_offers():
    SHOP = "ah"
    URL = "https://www.ah.nl/bonus/api/segments?segmentType=-PREMIUM"

    r = requests.get(url = URL)
    data = r.json()
    collection = []

    for i in data['collection']:

        try:
            if i['segmentType'] == "AH" and i['category'] != 'Koken, tafelen, vrije tijd' and "bezorging" not in i['shields'][0]['text'] and "miles" not in i['shields'][0]['text']:
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
                offer.update({"productId": i['id']})
                clean_title = cleantext.clean_up_title(i['title'])
                offer.update({"product": clean_title})

                clean_info = cleantext.clean_up_info(i['description'])
                offer.update({"productInfo": clean_info})

                category = categorize.find_category(clean_title, clean_info)
                offer.update({"category": category})

                offer.update({"shop": SHOP})

                calculated_deal = ""
                percentage = 0
                if "price" in i:
                    price_now = i['price']['now']
                    price_now = "{:.2f}".format(price_now)
                    try:
                        price_old = i['price']['was']
                        calculated_deal = cleandeal.calculate_percentage(price_old, price_now)
                        percentage = int(float(calculated_deal))
                    except KeyError:
                        pass

                    offer.update({"price": float(price_now)})


                if "shields" in i:
                    shield = i['shields'][0]['text']
                    deal_string = " ".join(str(x) for x in shield)
                    if "nu voor" in deal_string and calculated_deal != "": # when "nu voor" is found, use discount percentage as deal
                        deal = calculated_deal + "% korting"
                    else:
                        deal = deal_string

                    if "2e gratis" in deal_string:
                        deal = "1+1 gratis"
                        percentage = 50

                if "voor" in deal.lower() and "€" not in deal:
                    deal = deal.replace('voor', 'voor €')

                offer.update({"deal": deal})
                offer.update({"percentage": percentage})
                offer.update({"image": i['image']['src']})

                href = i['href']

                start_date_validity = i['validityPeriod']['start']
                end_date_validity = i['validityPeriod']['end']

                offer.update({"dateStart": start_date_validity})
                offer.update({"dateEnd": end_date_validity})

                offer.update({"link": "https://ah.nl" + i['href']})
                collection.append(offer)
        except IndexError:
            print("Aanbieding met titel " + i['title'] + " heeft een element niet, dus overgeslagen.")


    print("📄 " + str(len(collection)) + " aanbiedingen van de Albert Heijn bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    return_offers()