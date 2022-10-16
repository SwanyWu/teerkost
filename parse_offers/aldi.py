from optparse import TitledHelpFormatter
import requests
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from cleanup import categorize, cleantext

def return_weekday(date_string):
    date_string = date_string.split("-")
    year = int(date_string[0])
    month = int(date_string[1])
    day = int(date_string[2])

    date = datetime(year,month,day)

    days = ["maandag", "dinsdag", "woensdag",
        "donderdag", "vrijdag", "zaterdag", "zondag"]

    weekday = date.weekday()

    return days[weekday]

def return_first_sunday_startdate_string(date_string):
    date_string = date_string.split("-")
    year = int(date_string[0])
    month = int(date_string[1])
    day = int(date_string[2])

    date = datetime(year,month,day)

    weekday_start = date.weekday()
    days_remaining = 6 - weekday_start

    new_date = date + timedelta(days=days_remaining)
    new_date_string = new_date.strftime('%Y-%m-%d')

    return str(new_date_string)

def return_month(date_string):
    date_string = date_string.split("-")
    year = int(date_string[0])
    month = int(date_string[1])
    day = int(date_string[2])

    date = datetime(year,month,day)

    months = ["januari", "februari", "maart", "april", "mei",
    "juni", "juli", "augustus", "september", "oktober", "november", "december"]

    month = date.month()

    return months[month]

def return_calculated_date(date_string, plusDays):
    date_string = date_string.split("-")
    year = int(date_string[0])
    month = int(date_string[1])
    day = int(date_string[2])

    date = datetime(year,month,day)
    new_date = date + timedelta(days=plusDays)
    new_date_string = new_date.strftime('%Y-%m-%d')

    return str(new_date_string)

def return_offers():

    SHOP = "aldi"
    URL = "https://www.aldi.nl/aanbiedingen.html"

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")

    collection = []

    section_div = "mod-offers__day"
    article_div = "mod-article-tile"
    article_title_class = "mod-article-tile__title"

    section_index = 0
    for section in soup.find_all("div", {"class": section_div}):
        start_date_section = section['data-rel']

        if "zaterdag" in return_weekday(start_date_section):
            continue # Aldi offers only non-food on saturday, so skip collecting these

        section_index = section_index + 1

        for article in section.find_all("div", {"class", article_div}):

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

            title = ""
            info = ""
            image_link = ""
            price = ""
            old_price = ""
            price_label = ""
            deal = ""
            date_start = return_calculated_date(start_date_section, 0)
            date_end = return_first_sunday_startdate_string(start_date_section)
            link = ""

            title_element = article.find("span", {"class",article_title_class})
            if title_element is not None:
                title = title_element.get_text().strip()

            info_element = article.find("div", {"class", "price__meta"})
            if info_element is not None:
                info = info_element.get_text().strip()

            price_element = article.find("span", {"class", "price__wrapper"})
            if price_element is not None:
                price = price_element.get_text().strip()

            old_price_element = article.find("s", {"class", "price__previous"})
            if old_price_element is not None:
                old_price = old_price_element.get_text().strip()

            price_label_element = article.find("span", {"class", "price__previous-percentage"})
            if price_label_element is not None:
                price_label = price_label_element.get_text().strip()

            image_element = article.find("img", {"class", "img-responsive"})
            if image_element is not None:
                image_src = image_element['data-srcset']
                image_src = image_src.split(" 288w")
                image_link = "https://www.aldi.nl" + image_src[0] # extract a link from the srcset attribute

            link_element = article.find("a", {"class", "mod-article-tile__action"})
            if link_element is not None:
                link = "https://www.aldi.nl" + link_element['href']
                # Example: /aanbiedingen/wk15_vanaf_maandag_11-04/kaiser-en-schnittbroodjes-wit-4790-1-0.article.html
                link_elements_list = link_element['href'].split("-")
                link_elements_list.reverse()
                product_id_from_link = link_elements_list[2] # get the productId part from the href

            deal = ""
            if "%" in price_label: # a percentage is known, use it as the deal
                price_label = price_label.replace("-", "").lower().replace(" korting", "")
                deal = str(price_label) + " korting"
            else:
                if old_price != "" and price != "": # calculate the deal when old and new price is found
                    if len(price) == 8: # when price to large to convert to float
                        price = price.replace(".", "", 1)
                    if len(old_price) == 8:
                        old_price = old_price.replace(".", "", 1)
                    calculated_deal = int((1 - (float(price)/float(old_price))) * 100)
                    deal = str(calculated_deal) + "% korting"
                else:
                    if "voor" in price_label.lower() or "vanaf" in price_label.lower():
                        deal = str(price_label.strip() + " " + price)
                    else:
                        deal = str(price_label)
                    deal = deal.lower()

            if "op=op" in deal:
                deal = "op = op"

            if "voor" in deal.lower() and "€" not in deal:
                deal = deal.replace('voor', 'voor €')

            clean_title = cleantext.clean_up_title(title)
            clean_info = cleantext.clean_up_info(info)


            if price.count('.') == 2:
                price = price.replace(".", "", 1)

            price = float(format(float(price), '.2f'))

            offer.update({"productId": product_id_from_link})
            offer.update({"product": clean_title})
            offer.update({"productInfo": clean_info})
            offer.update({"category": categorize.find_category(clean_title, clean_info)})
            offer.update({"image": image_link})
            offer.update({"price": price})
            offer.update({"deal": deal})
            offer.update({"dateStart": date_start})
            offer.update({"dateEnd": date_end})
            offer.update({"link": link})
            offer.update({"shop": SHOP})

            if offer.get('deal') != "": # if no deal is found, don't add it
                collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de Aldi bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    return_offers()