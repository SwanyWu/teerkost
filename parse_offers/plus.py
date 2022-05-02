from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from bs4 import BeautifulSoup
from cleanup import categorize, cleantext
  
def returnMonthNumber(monthString):
    
    months = ['januari', 'februari', 'maart', 'april', 'mei', 'juni', 'juli', 'augustus', 'september', 'oktober', 'november','december']
    monthInt = months.index(monthString) + 1

    monthNumberString = format(monthInt, '02')
    return monthNumberString

def formatNumberAsFloat(number):
    numberAsList = list(number)
    numberAsList.reverse()
    numberAsList.insert(2, ".")
    numberAsList.reverse()

    floatNumber = "".join(str(x) for x in numberAsList)
    return floatNumber

def returnOffers():

    SHOP = "plus"
    URL = "https://www.plus.nl/aanbiedingen"

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

    try: 
        driver.get(URL)
        WebDriverWait(driver, 120).until(
            EC.visibility_of_element_located((By.ID, "_baby-en-drogisterij")) # wait for the last category

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
    finally:    
        driver.quit()
    

    soup = BeautifulSoup(productSectionHTML, "html.parser")
    collection = []

    dateStart = ""
    dateEnd = ""
    
    productTile = "ish-productList-item"
    i = 0
    for product in soup.find_all("li", {"class": productTile}):
        i = i + 1

        # print(product)
        productId = ""
        title = ""
        info = ""
        imageLink = ""
        price = ""
        deal = ""
        label = ""
        link = ""

        titleElement = product.find("div", {"class":"product-tile__info"})
        if titleElement != None:
            titleElement = titleElement.find("p")
            title = titleElement.get_text().strip()

        infoElement = product.find("span", {"class": "product-tile__quantity"})
        if infoElement != None:
            info = infoElement.get_text().strip()


        oldPrice = ""
        priceAboveCloverElement = product.find("div", {"class": "price-desktop"})
        if priceAboveCloverElement != None:
            oldPrice = priceAboveCloverElement.get_text().strip()   

        currentprice = ""
        print("----")

        clover = ""
        cloverElement = product.find("div", {"class": "clover"})
        if cloverElement != None:
            clover = cloverElement.get_text().strip()
            if "KORTING" in clover:
                splitClover = clover.split("KORTING")
                if "%" in splitClover[0]:
                    percentage = splitClover[0]
                    deal = percentage + " korting"
                else:
                    deal = "EEN BEDRAG KORTING" 
                    # TODO percentage berekenen met old price   
                # TODO nieuwe prijs berekenen
            elif "VOOR" in clover:
                splitClover = clover.split("VOOR")
                formattedPrice = formatNumberAsFloat(splitClover[1])
                deal = splitClover[0] + "voor " + formattedPrice
                # TODO prijs berekenen
            elif "+1GRATIS" in clover:
                splitClover = clover.split("+")
                deal = splitClover[0] + "+1 gratis"
                # TODO prijs berekenenen
            elif "GRAM" in clover or "KILO" in clover:
                deal = "IETS MET gram/kilo " + clover
                # TODO prijs en deal berekenen (en info updaten?)
            elif "2eHALVEPRIJS" in clover:
                deal = "2e halve prijs"
                # TODO prijs berekenen
            else: 
                try:
                    int(clover)
                    deal = "GEWOON DE PRIJS " + formatNumberAsFloat(clover) 
                    # TODO korting berekenen
                except:
                    deal = "IETSA NDERS DAN PRIJS?" + clover
                # TODO dan maar gewoon prijs en deal berekenen     

        print("-> deal: " + deal)

        imageElement = product.find("img")
        if imageElement != None:
            imageSrc = imageElement['data-src']
            imageLink = "https://www.plus.nl/" + imageSrc

        linkElement = product.find("a", {"class": "product-tile"})
        if linkElement != None:
            href = linkElement['href']
            # Example https://www.plus.nl/aanbiedingen/3159-37
            linkElementsList = href.split("/")
            linkElementsList.reverse()
            productId = linkElementsList[0]
            link = href

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

        cleanTitle = cleantext.cleanUpTitle(title)
        cleanInfo = cleantext.cleanUpInfo(info)
        offer.update({"productId": productId})
        offer.update({"product": cleanTitle})
        offer.update({"productInfo": cleanInfo})
        # offer.update({"category": categorize.findCategoryForProduct(cleanTitle, cleanInfo)})
        offer.update({"deal": deal})
        offer.update({"dateStart": dateStart})
        offer.update({"dateEnd": dateEnd})
        offer.update({"price": price})
        offer.update({"image": imageLink})
        offer.update({"link": link})
        offer.update({"shop": SHOP})

        if(offer.get('deal') != ""): # if no deal is found, don't add it
            collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de " + SHOP + " bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    returnOffers()