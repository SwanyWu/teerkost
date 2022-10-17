from xml.etree.ElementTree import ElementTree
import requests
from cleanup import categorize, cleantext
from datetime import datetime
from bs4 import BeautifulSoup

def return_offers():

    SHOP = "spar"
    URL = "https://www.spar.nl/aanbiedingen/"

    r = requests.get(URL)
    soup = BeautifulSoup(r.content, "html.parser")

    element_with_dates = soup.select_one(".c-featured-promo__content")
    if element_with_dates is not None:
        content = element_with_dates.find("div", {"class":"content"}).get_text().strip()
        if "de aanbiedingen uit deze folder zijn geldig van" in content:
            splitcontent = content.split(" ")
            # de aanbiedingen uit deze folder zijn geldig van 21-07-2022 t/m 03-08-2022
            splitcontent.reverse()
            # 03-08-2022 t/m 21-07-2022 van geldig zijn folder deze uit aanbiedingen de
            date_start = splitcontent[2]
            date_start_string = datetime.strptime(date_start, "%d-%m-%Y").date()
            date_end = splitcontent[0]
            date_end_string = datetime.strptime(date_end, "%d-%m-%Y").date()
        else:
            print("Kan geen info vinden over start- en einddatum!")


    collection = []
    for item in soup.find_all("div", {"class": "c-product-tile"}):
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

        clean_title = ""
        clean_info = ""

        meta_element = item.find("div", {"class":"c-product-tile__meta"})
        title_element = meta_element.find("a")
        if title_element is not None:
            title = title_element.get_text().strip()
            clean_title = cleantext.clean_up_title(title)


        description_element = meta_element.find("span")
        if description_element is not None:
            description = description_element.get_text().strip()
            clean_info = cleantext.clean_up_info(description)

        category = categorize.find_category(clean_title, clean_info)

        image_tile = item.find("div", {"class":"c-product-tile__image"})
        image_src = image_tile.find("img")
        image_url = ""
        if image_src is not None:
            image_url = image_src['data-src']

        full_href = ""
        product_id = ""

        link_element = image_tile.find("a")
        if link_element is not None:
            link = link_element['href']
            # https://www.spar.nl/aanbiedingen/kip-aanbieding-6861/
            full_href = "https://spar.nl" + link

            id_from_link = link.split("/")
            id_from_link.reverse()
            product_id = id_from_link[1]

        price_element = item.find("div", {"class":"c-product-tile__image--pricing"})
        if price_element is not None:
            old_price = price_element.find("span", {"class":"c-price__old"})
            if old_price is not None:
                new_price = price_element.find("span", {"class":"is-danger"})
                if new_price is not None:
                    base = new_price.find("span", {"class":"c-price__base"}).get_text().strip()
                    decimal = new_price.find("span", {"class":"c-price__mod"}).get_text().strip()
                    new_price = base + decimal
                    new_price = new_price.rstrip(".-")
                    old_price = old_price.get_text().strip().rstrip(".-")
                    offer.update({"price": float(new_price)})

                    calculate_deal = int((1 - (float(new_price)/float(old_price))) * 100)
                    deal = str(calculate_deal) + "% korting"
                else:
                    print("Geen nieuwe prijs, geen deal")
            else:
                print("geen oude prijs, geen deal")
        else:
            # Geen prijs te zien, dus pagina van aanbieding zelf openen
            # FIXME prijs berekenen op basis van promotion tekst
            if full_href != "":
                r = requests.get(full_href)
                soup = BeautifulSoup(r.content, "html.parser")
                promotion_summary = soup.find("div", {"class":"c-promotion-summary__content"})
                promotion_summar_deal = promotion_summary.select_one("h4")
                if promotion_summar_deal is not None:
                    promotion = promotion_summar_deal.get_text().strip()
                    if len(promotion) > 20:
                        if 'nu met' in deal:
                            deal = deal.replace('nu met', '')
                        else:
                            if 'voor' in deal:
                                promotion_splitted = promotion.split("voor")
                                promotion_splitted.reverse()
                                deal = "voor" + promotion_splitted[0]
                    else:
                        deal = promotion
                else:
                    print("Kan geen deal vinden op " + full_href)
            else:
                print("Geen prijs en geen URL")

        deal = deal.replace('!', '')
        deal = deal.replace('Nu ', '')
        deal = deal.replace('nu ', '')
        deal = deal.replace('stuks voor', 'voor')

        offer.update({"productId": product_id})
        offer.update({"product": clean_title})
        offer.update({"productInfo": clean_info})
        offer.update({"category": category})
        offer.update({"link": full_href})
        offer.update({"deal": deal })
        offer.update({"image": image_url})
        offer.update({"dateStart": str(date_start_string)})
        offer.update({"dateEnd": str(date_end_string)})
        offer.update({"shop": SHOP})

        if offer.get('deal') != "": # if no deal is found, don't add it
            collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de "+SHOP+" bij elkaar verzameld.")

    return collection

if __name__ == "__main__":
    return_offers()