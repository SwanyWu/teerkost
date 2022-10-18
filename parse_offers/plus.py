from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from bs4 import BeautifulSoup
from cleanup import categorize, cleantext, cleandate, cleandeal

def format_number_float(number):
    number = number.replace("\n", "") # character appears sometimes
    number_as_list = list(number)
    number_as_list.reverse()
    if "." not in number_as_list:
        number_as_list.insert(2, ".")
    number_as_list.reverse()

    float_number = float("".join(str(x) for x in number_as_list))
    float_number = round(float_number, 2)
    return str(float_number)

def get_page_content(URL, driver, element_to_be_located):
    driver.get(URL)
    WebDriverWait(driver, 300).until(
            EC.visibility_of_element_located((By.ID, element_to_be_located)) # wait for the last category
        )
    try:
        element = WebDriverWait(driver, 120).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "promotion-marketing-container")) # some more waiting, but probably not needed
            )
    finally:
        randomTitleWebElement = element.find_element(By.CLASS_NAME, "pageTitel")
        randomTitleInnerHTML = randomTitleWebElement.get_attribute("innerHTML")
        if type(randomTitleInnerHTML) == str:
            productSectionWebElement = driver.find_element(By.CLASS_NAME, "promotion-block-container")
            productSectionHTML = productSectionWebElement.get_attribute('outerHTML')
    return productSectionHTML

def return_offers():

    SHOP = "plus"
    URL = "https://www.plus.nl/aanbiedingen"

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

    try:
        productSectionHTML = get_page_content(URL, driver, "_baby-drogisterij")
    except Exception:
        print("Kan element nog niet zien, nog één keer proberen.")
        productSectionHTML = get_page_content(URL, driver, "_huishouden")
    finally:
        driver.quit()


    soup = BeautifulSoup(productSectionHTML, "html.parser")
    collection = []

    dateElement = soup.find("h3", {"class": "promotion-search-titelH3"})
    if dateElement is not None:
        date = dateElement.get_text().strip()
        date = date.split("t/m")
        date_start_string = date[0]
        date_end_string = date[1]

        date_start_day = date_start_string.split(" ")[1]
        date_start_month = date_start_string.split(" ")[2]

        date_end_day = date_end_string.split(" ")[1]
        date_end_month = date_end_string.split(" ")[2]

        year = datetime.datetime.now().year

        date_start = str(year) +"-"+ cleandate.return_index_by_full_month_text(date_start_month) +"-"+ date_start_day
        date_end = str(year) +"-"+ cleandate.return_index_by_full_month_text(date_end_month) +"-"+ date_end_day

    product_tile = "ish-productList-item"
    for product in soup.find_all("li", {"class": product_tile}):
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
        info = ""
        image_link = ""
        price = 0
        percentage = 0
        deal = ""
        link = ""

        title_element = product.find("div", {"class":"product-tile__info"})
        if title_element is not None:
            title_element = title_element.find("p")
            title = title_element.get_text().strip()

        info_element = product.find("span", {"class": "product-tile__quantity"})
        if info_element is not None:
            info = info_element.get_text().strip()

        old_price = ""
        price_clover_element = product.find("div", {"class": "price-desktop"})
        if price_clover_element is not None:
            old_price = price_clover_element.get_text().strip()
            if "\n" in old_price:
                oldPriceSplit = old_price.split("\n")
                old_price = oldPriceSplit[0]

        clover = ""
        clover_element = product.find("div", {"class": "clover"})
        if clover_element is not None:
            clover = clover_element.get_text().strip()
            if "KORTING" in clover:
                split_clover = clover.split("KORTING")
                if "%" in split_clover[0]: # a percentage is found
                    percentage_found = split_clover[0]
                    deal = percentage_found + " korting"
                    percentage = int(float(percentage_found.replace("%", "")))
                    # TODO nieuwe prijs berekenen
                else:
                    discount = format_number_float(split_clover[0]) # a discount is found
                    new_price = float(old_price) - float(discount)
                    calculated_deal = cleandeal.calculate_percentage(old_price, new_price)
                    deal = calculated_deal + "% korting"
                    percentage = int(float(calculated_deal))
                    price = float(str(new_price))
            elif "VOOR" in clover:
                split_clover = clover.split("VOOR")
                formatted_price = format_number_float(split_clover[1])
                deal = split_clover[0] + "voor " + formatted_price
                price = float(formatted_price)
            elif "+1GRATIS" in clover:
                split_clover = clover.split("+")
                deal = split_clover[0] + "+1 gratis"
                calculate_percentage = 1 / (int(split_clover[0]) + 1)
                percentage = int(float(calculate_percentage))
                # TODO prijs berekenenen
            elif "GRAM" in clover:
                split_clover = clover.split("GRAM")
                prijs_kilo = split_clover[1]
                new_price = format_number_float(prijs_kilo)
                calculated_deal = cleandeal.calculate_percentage(old_price, new_price)
                price = float(new_price)
                if float(calculated_deal) < 0.0:
                    print("Wait wut, korting van " + calculated_deal + "%")
                else:
                    deal = calculated_deal + "% korting"

                percentage = int(float(calculated_deal))    
            elif "KILO" in clover:
                split_clover = clover.split("KILO")
                prijs_kilo = split_clover[1]
                new_price = format_number_float(prijs_kilo)
                calculated_deal = cleandeal.calculate_percentage(old_price, new_price)
                price = float(new_price)
                if float(calculated_deal) < 0.0:
                    print("Wait wut, korting van " + calculated_deal + "%")
                else:
                    deal = calculated_deal + "% korting"

                percentage = int(float(calculated_deal))
            elif "2eHALVEPRIJS" in clover:
                deal = "2e halve prijs"
                percentage = 25
                # TODO prijs berekenen
            elif "HALEN" in clover and "BETALEN" in clover:
                clover = clover.replace("HALEN", "HALEN ")
                clover = clover.split(" ")
                hoeveel_halen = int(clover[0])
                hoeveel_betalen = int(clover[2])

                deal = clover[0] + " halen " + clover[2] + " betalen"

                calculate_percentage = (1 - (hoeveel_betalen/hoeveel_halen)) * 100
                percentage = int(float(calculate_percentage))
                print(deal)
                print(percentage)
            else:
                try:
                    new_price = format_number_float(clover)
                    calculated_deal = cleandeal.calculate_percentage(old_price, new_price)
                    percentage = int(float(calculated_deal))
                    deal = calculated_deal + "% korting"
                    # TODO prijs berekenen
                except Exception as e:
                    print("Geen idee wat de deal is hiervan: " + clover)
                    deal = ""

        image_element = product.find("img")
        if image_element is not None:
            imageSrc = image_element['data-src']
            image_link = "https://www.plus.nl" + imageSrc

        link_element = product.find("a", {"class": "product-tile"})
        if link_element is not None:
            href = link_element['href']
            # Example https://www.plus.nl/aanbiedingen/3159-37
            link_element_list = href.split("/")
            link_element_list.reverse()
            product_id = link_element_list[0]
            link = href

        #FIXME als weekendpakker bij staan de start en einddatum aanpassen
        product_label_top = product.find("span",  {"class": "product-tile__label--top"})
        if product_label_top != None:
            product_label_text = product_label_top.get_text().strip()
            if "weekendpakker" in product_label_text.lower():
                print("He, " + title + " is een weekendpakker!")
                # datetime = datetime.datetime.strptime(dateStart, "%Y-%m-%d")
                # print(datetime.date().

        if price != '':
            price_as_float = float(price)
            price = str(round(price_as_float, 2))

        if "voor" in deal.lower() and "€" not in deal:
            deal = deal.replace('voor', 'voor €')

        clean_title = cleantext.clean_up_title(title)
        clean_info = cleantext.clean_up_info(info)
        offer.update({"productId": product_id})
        offer.update({"product": clean_title})
        offer.update({"productInfo": clean_info})
        offer.update({"category": categorize.find_category(clean_title, clean_info)})
        offer.update({"deal": deal})
        offer.update({"dateStart": date_start})
        offer.update({"dateEnd": date_end})
        offer.update({"price": float(price)})
        offer.update({"percentage": percentage})
        offer.update({"image": image_link})
        offer.update({"link": link})
        offer.update({"shop": SHOP})
        if offer.get('deal') != "": # if no deal is found, don't add it
            collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de " + SHOP + " bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    return_offers()