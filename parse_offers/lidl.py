import requests
from cleanup import categorize, cleantext, cleandate
import datetime
import json
from bs4 import BeautifulSoup

def return_offers():

    SHOP = "lidl"
    URL = "https://www.lidl.nl/c/aanbiedingen/a10008785"


    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")

    collection = []

    for item in soup.find_all("li", {"class": "ACampaignGrid__item--product"}):
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

        product_id = ""
        title = ""
        description = ""
        date = ""
        percentage = 0
        image_url = ""
        link = ""

        detail_element = item.find("div", {"class":"detail__grids"})
        detail_element_data = detail_element.attrs['data-grid-data']
        load_jsonlist = json.loads(detail_element_data)

        title = load_jsonlist[0]['fullTitle']
        clean_title = cleantext.clean_up_title(title)
        offer.update({"product": clean_title})

        deal = load_jsonlist[0]['gridLabel']
        if type(deal) != type(None):
            deal = deal.lower()
        else:
            discount = load_jsonlist[0]['price']['discount']
            if type(discount) != type(None):
                discount_percentage = load_jsonlist[0]['price']['discount']['percentageDiscount']
                if type(discount_percentage) != type(None):
                    percentage = int(float(discount_percentage))
                    deal = str(discount_percentage) + "% korting"
                else:
                    deal = ""
                    # no percentage or deal found, so use discountText
                    deal = str(load_jsonlist[0]['price']['discount']['discountText']).lower()

            else:
              deal = ""
              print("Geen aanbieding gevonden voor " + title)
              # deal is on the image

        price = float(0)
        price = load_jsonlist[0]['price']['price']
        if type(price) == type(None):
            price = float(0)

        image_url = load_jsonlist[0]['image']

        canonical_url = load_jsonlist[0]['canonicalUrl']
        link = "https://www.lidl.nl" + canonical_url

        link_element = canonical_url.split("/")
        link_element.reverse()
        product_id = link_element[0]

        description = load_jsonlist[0]['keyfacts']['description']
        clean_info = ""

        if type(description) != type(None):
            clean_info = cleantext.clean_up_info(description.strip())

        offer.update({"productInfo": clean_info})
        category = categorize.find_category(clean_title, clean_info)
        offer.update({"category": category})

        offer.update({"productId": product_id})

        offer.update({"shop": SHOP})
        offer.update({"price": float(price)})
        offer.update({"percentage": percentage})
        offer.update({"image": image_url})
        offer.update({"link": link})

        date = load_jsonlist[0]['ribbons'][0]['text']
        if len(date) != 0: # check if something of a date is found
            if "vanaf" in date: # check if only the startdate is provided
                date = date.replace("vanaf ", "")
                date = date.split(" ")
                date = date[1].split("/")
                day_start = date[0]
                month_start = date[1]
                current_year = str(datetime.datetime.now().year)
                full_date_start = cleandate.return_full_datestring(current_year, month_start, day_start)

                offer.update({"dateStart": full_date_start})
            else: # start and end date is provided
                if "/" in date:
                    date = date.split(" - ")
                    date_string_end = date[1].split(" ")
                    date_string_end = date_string_end[1].split("/")
                    day_end = date_string_end[0]
                    month_end = date_string_end[1]

                    date_string_start = date[0].split(" ")
                    date_string_start = date_string_start[1].split("/")
                    day_start = date_string_start[0]
                    month_start = date_string_start[1]

                    current_year = str(datetime.datetime.now().year)

                    full_date_end = cleandate.return_full_datestring(current_year, month_end, day_end)
                    full_date_start = cleandate.return_full_datestring(current_year, month_start, day_start)

                    offer.update({"dateStart": full_date_start})
                    offer.update({"dateEnd": full_date_end})
                else:
                    deal = "" # no deal because no date is found
                    print("Geen datum gevonden voor " + title)

        offer.update({"deal": deal})

        if offer.get('deal') != "": # if no deal is found, don't add it
            collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de Lidl bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    return_offers()