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
            productSectionWebElement = driver.find_element(By.CLASS_NAME, "aanbiedingen-page")
            productSectionHTML = productSectionWebElement.get_attribute('outerHTML')

        driver.quit()

    soup = BeautifulSoup(productSectionHTML, "html.parser")
    collection = []

    dateStart = ""
    dateEnd = ""

    dateElement = soup.find("div", {"class": "sub-wrapper"}).find("span", {"class": "sub-title"})
    if dateElement != None:
        fullDateString = dateElement.get_text().strip()
        fullDateString = fullDateString.replace("\n", "").split(' ')
        while '' in fullDateString:
            fullDateString.remove('')

        currentYear = datetime.datetime.now().year

        startDay = fullDateString[0]
        fullDateStringMonthStart = fullDateString[1]
        startMonth = returnMonthNumber(fullDateStringMonthStart)
        
        if fullDateString[3] == 'Vandaag':
            endDay = datetime.datetime.now().day
            endMonth = datetime.datetime.now().month

            formattedEndDate = str(currentYear) + "-" + str(endMonth) + "-" + str(endDay)
            dateEnd = formattedEndDate
        else:    
            endDay = fullDateString[3]
            fullDateStringMonth = fullDateString[4]
            endMonth = returnMonthNumber(fullDateStringMonth)

            formattedEndDate = str(currentYear) + "-" + endMonth + "-" + endDay
            dateEnd = formattedEndDate

        formattedStartDate = str(currentYear) + "-" + startMonth + "-" + startDay
        dateStart = formattedStartDate

    productTile = "product-tile"
    for product in soup.find_all("div", {"class": productTile}):

        title = ""
        info = ""
        imageLink = ""
        price = ""
        deal = ""
        label = ""
        link = ""

        titleElement = product.find("h4", {"class", "title"})
        if titleElement != None:
            title = titleElement.get_text().strip()
        
        infoElement = product.find("p", {"class", "mb-0"})
        if infoElement != None:
            info = infoElement.get_text().strip()

        primaryLabel = product.find("span", {"class", "label-primary"})
        if primaryLabel != None:
            label = primaryLabel.get_text().strip()

        priceMainDigit = product.find("strong", {"class", "price-integer"}).get_text().strip()
        priceMainDigitSmall = product.find("sup", {"class", "price-digit"}).get_text().strip()
        if priceMainDigit != None and priceMainDigitSmall != None:
            price = priceMainDigit + "." + priceMainDigitSmall

        oldPrice = product.find("small", {"class", "price-list"})
        if oldPrice != None:
            oldPrice = oldPrice.get_text().strip()
            oldPrice = oldPrice.replace(",", ".") # make it convertable to float

            if oldPrice != "" and price != "": # calculate a discount
                calculateDeal = int((1 - (float(price)/float(oldPrice))) * 100)
                deal = str(calculateDeal) + "% korting" 
        else: # or use the label for the discount
            deal = label.lower()

        imageElement = product.find("img")
        if imageElement != None:
            imageSrc = imageElement['data-src']
            imageLink = imageSrc

        linkElement = product.find("a", {"class", "link-contnet"})
        if linkElement != None:
            linkHref = linkElement['href']
            link = "https://www.ekoplaza.nl" + linkHref

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

        cleanTitle = cleantext.cleanUpTitle(title)
        cleanInfo = cleantext.cleanUpInfo(info)
        offer.update({"product": cleanTitle})
        offer.update({"productInfo": cleanInfo})
        offer.update({"category": categorize.findCategoryForProduct(cleanTitle, cleanInfo)})
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