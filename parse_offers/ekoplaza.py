from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from bs4 import BeautifulSoup
from cleanup import categorize, cleantext

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
        randomTitleWebElement = element.find_element(By.CSS_SELECTOR, 'h4')
        randomTitleInnerHTML = randomTitleWebElement.get_attribute("innerHTML")
        if type(randomTitleInnerHTML) == str:
            productSectionWebElement = driver.find_element(By.CLASS_NAME, "aanbiedingen-page")
            productSectionHTML = productSectionWebElement.get_attribute('outerHTML')

        driver.quit()

    soup = BeautifulSoup(productSectionHTML, "html.parser")
    collection = []

    date_start = ""
    date_end = ""

    dateElement = soup.find("div", {"class": "sub-wrapper"}).find("span", {"class": "sub-title"})
    if dateElement is not None:
        fullDateString = dateElement.get_text().strip()
        fullDateString = fullDateString.replace("\n", "").split(' ')
        while '' in fullDateString:
            fullDateString.remove('')

        currentYear = datetime.datetime.now().year

        if fullDateString[0] == 'Vandaag':
            startDay = datetime.datetime.now().day
            startMonth = datetime.datetime.now().month
        else:
            startDay = fullDateString[0]
            fullDateStringMonthStart = fullDateString[1]
            startMonth = return_month_number(fullDateStringMonthStart)

        formattedStartDate = str(currentYear) + "-" + str(startMonth) + "-" + str(startDay)
        date_start = formattedStartDate

        if fullDateString[3] == 'Vandaag':
            endDay = datetime.datetime.now().day
            endMonth = datetime.datetime.now().month
        elif fullDateString[0] == 'Vandaag':
            endDay = fullDateString[2]
            fullDateStringMonth = fullDateString[3]
            endMonth = return_month_number(fullDateStringMonth)
        else:
            endDay = fullDateString[3]
            fullDateStringMonth = fullDateString[4]
            endMonth = return_month_number(fullDateStringMonth)

        formattedEndDate = str(currentYear) + "-" + str(endMonth) + "-" + str(endDay)
        date_end = formattedEndDate

    productTile = "product-tile"
    for product in soup.find_all("div", {"class": productTile}):

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

        offer = {
            "productId":"",
            "product":"",
            "productInfo":"",
            "category":"",
            "image":"",
            "deal":"",
            "price": 0,
            "dateStart":"",
            "dateEnd":"",
            "link": "",
            "shop":""}

        if "voor" in deal.lower() and "€" not in deal:
            deal = deal.replace('voor', 'voor €')

        clean_title = cleantext.clean_up_title(title)
        clean_info = cleantext.clean_up_info(info)
        offer.update({"productId": productId})
        offer.update({"product": clean_title})
        offer.update({"productInfo": clean_info})
        offer.update({"category": categorize.find_category_for_product(clean_title, clean_info)})
        offer.update({"deal": deal})
        offer.update({"dateStart": date_start})
        offer.update({"dateEnd": date_end})
        offer.update({"price": float(price)})
        offer.update({"image": image_link})
        offer.update({"link": link})
        offer.update({"shop": SHOP})

        if(offer.get('deal') != ""): # if no deal is found, don't add it
            collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de " + SHOP + " bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    return_offers()