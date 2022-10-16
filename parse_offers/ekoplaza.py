from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from bs4 import BeautifulSoup
from cleanup import categorize, cleantext
from offer import offer

def return_month_number(monthString):

    months = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november','december']
    month_number = months.index(monthString) + 1

    month_number_string = format(month_number, '02')
    return month_number_string

def return_offers():

    SHOP = "ekoplaza"
    URL = "https://www.ekoplaza.nl/nl/aanbiedingen"

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

    try:
        driver.get(URL)
        element = WebDriverWait(driver, 40).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "product-tile"))
        )
    finally:
        random_title_webelement = element.find_element(By.CSS_SELECTOR, 'h4')
        random_title_innerhtml = random_title_webelement.get_attribute("innerHTML")
        if type(random_title_innerhtml) == str:
            productsection_webelement = driver.find_element(By.CLASS_NAME, "aanbiedingen-page")
            productsection_outerhtml = productsection_webelement.get_attribute('outerHTML')

        driver.quit()

    soup = BeautifulSoup(productsection_outerhtml, "html.parser")
    collection = []

    date_start = ""
    date_end = ""

    date_element = soup.find("div", {"class": "sub-wrapper"}).find("span", {"class": "sub-title"})
    if date_element is not None:
        full_date_string = date_element.get_text().strip()
        full_date_string = full_date_string.replace("\n", "").split(' ')
        while '' in full_date_string:
            full_date_string.remove('')

        current_year = datetime.datetime.now().year

        if full_date_string[0] == 'Vandaag':
            start_day = datetime.datetime.now().day
            start_month = datetime.datetime.now().month
        else:
            start_day = full_date_string[0]
            full_date_string_month_start = full_date_string[1]
            start_month = return_month_number(full_date_string_month_start)

        formatted_start_date = str(current_year) + "-" + str(start_month) + "-" + str(start_day)
        date_start = formatted_start_date

        if full_date_string[3] == 'Vandaag':
            end_day = datetime.datetime.now().day
            end_month = datetime.datetime.now().month
        elif full_date_string[0] == 'Vandaag':
            end_day = full_date_string[2]
            full_date_string_month = full_date_string[3]
            end_month = return_month_number(full_date_string_month)
        else:
            end_day = full_date_string[3]
            full_date_string_month = full_date_string[4]
            end_month = return_month_number(full_date_string_month)

        formatted_end_date = str(current_year) + "-" + str(end_month) + "-" + str(end_day)
        date_end = formatted_end_date

    product_tile = "product-tile"
    for product in soup.find_all("div", {"class": product_tile}):

        title = ""
        info = ""
        image_link = ""
        price = ""
        deal = ""
        label = ""
        link = ""

        title_element = product.find("h4", {"class", "title"})
        if title_element is not None:
            title = title_element.get_text().strip()

        info_element = product.find("p", {"class", "mb-0"})
        if info_element is not None:
            info = info_element.get_text().strip()

        primary_label = product.find("span", {"class", "label-primary"})
        if primary_label is not None:
            label = primary_label.get_text().strip()

        price_main_digit = product.find("strong", {"class", "price-integer"}).get_text().strip()
        price_main_digit_small = product.find("sup", {"class", "price-digit"}).get_text().strip()
        if price_main_digit is not None and price_main_digit_small is not None:
            price = price_main_digit + "." + price_main_digit_small

        old_price = product.find("small", {"class", "price-list"})
        if old_price is not None:
            old_price = old_price.get_text().strip()
            old_price = old_price.replace(",", ".") # make it convertable to float

            if old_price != "" and price != "": # calculate a discount
                calculate_deal = int((1 - (float(price)/float(old_price))) * 100)
                deal = str(calculate_deal) + "% korting"
        else: # or use the label for the discount
            deal = label.lower()

        image_element = product.find("img")
        if image_element != None:
            image_src = image_element['data-src']
            image_link = image_src

        link_element = product.find("a", {"class", "link-contnet"})
        if link_element != None:
            link_href = link_element['href']
            link = "https://www.ekoplaza.nl" + link_href
            # Example /nl/producten/product/groene-asperges-0001184648
            link_elements_list = link_href.split("-")
            link_elements_list.reverse()
            productId = link_elements_list[0]

        if "voor" in deal.lower() and "€" not in deal:
            deal = deal.replace('voor', 'voor €')

        clean_title = cleantext.clean_up_title(title)
        clean_info = cleantext.clean_up_info(info)
        offer.update({"productId": productId})
        offer.update({"product": clean_title})
        offer.update({"productInfo": clean_info})
        offer.update({"category": categorize.find_category(clean_title, clean_info)})
        offer.update({"deal": deal})
        offer.update({"dateStart": date_start})
        offer.update({"dateEnd": date_end})
        offer.update({"price": float(price)})
        offer.update({"image": image_link})
        offer.update({"link": link})
        offer.update({"shop": SHOP})

        if offer.get('deal') != "": # if no deal is found, don't add it
            collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de " + SHOP + " bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    return_offers()