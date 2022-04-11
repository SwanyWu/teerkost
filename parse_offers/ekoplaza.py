from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
# from cleanup import categorize, cleantext
  
def returnOffers():

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
            print("Er is een titelelement, dus parsen die handel.")
            productSectionWebElement = driver.find_element(By.ID, "product-section-group")
            productSectionHTML = productSectionWebElement.get_attribute('outerHTML')

        driver.quit()

    soup = BeautifulSoup(productSectionHTML, "html.parser")
    collection = []

    productTile = "product-tile"
    for product in soup.find_all("div", {"class": productTile}):

        title = ""
        info = ""
        imageLink = ""
        price = ""
        deal = ""
        dateStart = ""
        dateEnd = ""
        link = ""

        titleElement = product.find("h4", {"class", "title"})
        if titleElement != None:
            title = titleElement.get_text().strip()
        
        infoElement = product.find("p", {"class", "mb-0"})
        if infoElement != None:
            info = infoElement.get_text().strip()

        priceMainDigit = product.find("strong", {"class", "price-integer"}).get_text().strip()
        priceMainDigitSmall = product.find("sup", {"class", "price-digit"}).get_text().strip()
        if priceMainDigit != None and priceMainDigitSmall != None:
            price = priceMainDigit + "." + priceMainDigitSmall

        # FIXME element vinden
        priceOld = product.find("small", {"class", "price-list"})
        if priceOld != None:
            priceOld = priceOld.get_text().strip()

        imageElement = product.find("img")
        if imageElement != None:
            imageSrc = imageElement['data-src']
            imageLink = imageSrc

        linkElement = product.find("a", {"class", "link-contnet"})
        if linkElement != None:
            linkHref = linkElement['href']
            link = "https://www.ekoplaze.nl" + linkHref

        offer = {
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

        # cleanTitle = cleantext.cleanUpTitle(title)
        # cleanInfo = cleantext.cleanUpInfo(info)
        cleanTitle = title
        cleanInfo = info
        offer.update({"product": cleanTitle})
        offer.update({"productInfo": cleanInfo})
        # offer.update({"category": categorize.findCategoryForProduct(cleanTitle, cleanInfo)})
        offer.update({"price": price})
        offer.update({"image": imageLink})
        offer.update({"link": link})
        offer.update({"shop": SHOP})

        print(offer)
        print(" ")
                
        # if(offer.get('deal') != ""): # if no deal is found, don't add it
        collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de " + SHOP + " bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    returnOffers()