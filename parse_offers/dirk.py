import requests
from datetime import datetime
from cleanup import categorize, cleantext, cleandeal

def return_offers():
    SHOP = "dirk"
    API_KEY = "6d3a42a3-6d93-4f98-838d-bcc0ab2307fd"
    CATEGORIES = [1,2,3,4,5,6,7,8,9,10,11,13,14,15,16,18]

    collection = []

    # TODO vanaf woensdag aanbiedings ook
    for categorie in CATEGORIES:
        category_string = str(categorie)

        URL = "https://api.dirk.nl/v1/offerscache/department/66/"+category_string+"?api_key=" + API_KEY

        r = requests.get(url = URL)
        data = r.json()

        for i in data:
            offer = {
                "productId": "",
                "product":"", 
                "productInfo":"", 
                "category":"", 
                "image":"", 
                "deal":"",
                "price": float(0), 
                "dateStart":"", 
                "dateEnd":"", 
                "link": "", 
                "shop":""
            }
            offer.update({"productId": i['OfferID']})

            clean_title = cleantext.clean_up_title(i['HeaderText'])
            offer.update({"product": clean_title})

            description = i['Packaging']
            if description is not None:
                clean_info = cleantext.clean_up_info(description)
                offer.update({"productInfo": clean_info})

            price = i['OfferPrice'];
            offer.update({"price": float(price)})

            if i['NormalPrice'] is not None:
                old_price = i['NormalPrice']
                calculate_deal = cleandeal.calculate_percentage(old_price, price)
                deal = calculate_deal + "% korting"
            else:
                deal = "€" +str(price)
                # TODO misschien zijn er andere type deals

            offer.update({"deal": deal})

            full_date_start = i['StartDate']
            start_date = datetime.fromisoformat(full_date_start).date()
            offer.update({"dateStart": str(start_date)})

            full_date_end = i['EndDate']
            end_date = datetime.fromisoformat(full_date_end).date()
            offer.update({"dateEnd": str(end_date)})

            if i['ProductOffers'][0]['Product']['ProductPicture']['Url'] is not None:
                imageurl = i['ProductOffers'][0]['Product']['ProductPicture']['Url'] + "?width=170&height=170&mode=crop"
                offer.update({"image": imageurl})

            if i['OfferUrls'][0]['Url'] is not None:
                # https://www.dirk.nl/aanbiedingen/ambachtelijke-salade/84338
                offer_id = str(i['OfferID'])
                offer_url = i['OfferUrls'][0]['Url']
                url = "https://www.dirk.nl/aanbiedingen/" + offer_url + "/" + offer_id
                offer.update({"link": url})

            category = categorize.find_category(clean_title, clean_info)
            
            offer.update({"category": category})
            offer.update({"shop": SHOP})
            
            collection.append(offer)
            
    print("📄 " + str(len(collection)) + " aanbiedingen van de Dirk bij elkaar verzameld.")

    return collection

if __name__ == "__main__":
    return_offers()