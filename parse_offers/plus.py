from posixpath import split
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
    number = number.replace("\n", "") # character appears sometimes
    numberAsList = list(number)
    numberAsList.reverse()
    if "." not in numberAsList:
        numberAsList.insert(2, ".")
    numberAsList.reverse()

    floatNumber = float("".join(str(x) for x in numberAsList))
    floatNumber = round(floatNumber, 2)
    return str(floatNumber)

def calculatePercentage(oldPrice, newPrice):
    calculateDeal = int((1 - (float(newPrice)/float(oldPrice))) * 100)
    return str(calculateDeal)

def returnMonth(monthString):
    monthString = monthString.replace("\xa0", "")
    months = ["januari", "februari", "maart", "april", "mei",
    "juni", "juli", "augustus", "september", "oktober", "november", "december"]

    monthInt = months.index(monthString) + 1
    monthNumberString = format(monthInt, '02')

    return monthNumberString

def getPageContent(URL, driver, element_to_be_located):
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

def returnOffers():

    SHOP = "plus"
    URL = "https://www.plus.nl/aanbiedingen"

    options = Options()
    options.headless = True

    driver = webdriver.Firefox(options=options, executable_path=GeckoDriverManager().install())

    try:
        productSectionHTML = getPageContent(URL, driver, "_baby-drogisterij")
    except Exception:
        print("Kan element nog niet zien, nog één keer proberen.")
        productSectionHTML = getPageContent(URL, driver, "_huishouden")
    finally:
        driver.quit()


    soup = BeautifulSoup(productSectionHTML, "html.parser")
    collection = []

    dateElement = soup.find("h3", {"class": "promotion-search-titelH3"})
    if dateElement != None:
        date = dateElement.get_text().strip()
        date = date.split("t/m")
        dateStartString = date[0]
        dateEndString = date[1]

        dateStartDay = dateStartString.split(" ")[1]
        dateStartMonth = dateStartString.split(" ")[2]

        dateEndDay = dateEndString.split(" ")[1]
        dateEndMonth = dateEndString.split(" ")[2]

        year = datetime.datetime.now().year

        dateStart = str(year) +"-"+ returnMonth(dateStartMonth) +"-"+ dateStartDay
        dateEnd = str(year) +"-"+ returnMonth(dateEndMonth) +"-"+ dateEndDay

    productTile = "ish-productList-item"
    for product in soup.find_all("li", {"class": productTile}):

        productId = ""
        title = ""
        info = ""
        imageLink = ""
        price = 0
        deal = ""
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
            if "\n" in oldPrice:
                oldPriceSplit = oldPrice.split("\n")
                oldPrice = oldPriceSplit[0]

        clover = ""
        cloverElement = product.find("div", {"class": "clover"})
        if cloverElement != None:
            clover = cloverElement.get_text().strip()
            if "KORTING" in clover:
                splitClover = clover.split("KORTING")
                if "%" in splitClover[0]: # a percentage is found
                    percentage = splitClover[0]
                    deal = percentage + " korting"
                    # TODO nieuwe prijs berekenen
                else:
                    discount = formatNumberAsFloat(splitClover[0]) # a discount is found
                    newPrice = float(oldPrice) - float(discount)
                    deal = calculatePercentage(oldPrice, newPrice) + "% korting"
                    price = float(str(newPrice))
            elif "VOOR" in clover:
                splitClover = clover.split("VOOR")
                formattedPrice = formatNumberAsFloat(splitClover[1])
                deal = splitClover[0] + "voor " + formattedPrice
                price = float(formattedPrice)
            elif "+1GRATIS" in clover:
                splitClover = clover.split("+")
                deal = splitClover[0] + "+1 gratis"
                # TODO prijs berekenenen
            elif "GRAM" in clover:
                splitClover = clover.split("GRAM")
                prijsKilo = splitClover[1]
                newPrice = formatNumberAsFloat(prijsKilo)
                percentage = calculatePercentage(oldPrice, newPrice)
                price = float(newPrice)
                if float(percentage) < 0.0:
                    print("Wait wut, korting van " + str(percentage) + "%")
                else:
                    deal = percentage + "% korting"
            elif "KILO" in clover:
                splitClover = clover.split("KILO")
                prijsKilo = splitClover[1]
                newPrice = formatNumberAsFloat(prijsKilo)
                percentage = calculatePercentage(oldPrice, newPrice)
                price = float(newPrice)
                if float(percentage) < 0.0:
                    print("Wait wut, korting van " + str(percentage) + "%")
                else:
                    deal = percentage + "% korting"
            elif "2eHALVEPRIJS" in clover:
                deal = "2e halve prijs"
                # TODO prijs berekenen
            else:
                try:
                    newPrice = formatNumberAsFloat(clover)
                    deal = calculatePercentage(oldPrice, newPrice) + "% korting"
                    # TODO prijs berekenen
                except Exception as e:
                    print("Geen idee wat de deal is hiervan: " + clover)
                    deal = ""

        imageElement = product.find("img")
        if imageElement != None:
            imageSrc = imageElement['data-src']
            imageLink = "https://www.plus.nl" + imageSrc

        linkElement = product.find("a", {"class": "product-tile"})
        if linkElement != None:
            href = linkElement['href']
            # Example https://www.plus.nl/aanbiedingen/3159-37
            linkElementsList = href.split("/")
            linkElementsList.reverse()
            productId = linkElementsList[0]
            link = href

        #FIXME als weekendpakker bij staan de start en einddatum aanpassen
        productLabelTop = product.find("span",  {"class": "product-tile__label--top"})
        if productLabelTop != None:
            productLabelText = productLabelTop.get_text().strip()
            if "weekendpakker" in productLabelText.lower():
                print("He, " + title + " is een weekendpakker!")
                # datetime = datetime.datetime.strptime(dateStart, "%Y-%m-%d")

                # print(datetime.date().

        if price != '':
            priceAsFloat = float(price)
            price = str(round(priceAsFloat, 2))

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

        cleanTitle = cleantext.cleanUpTitle(title)
        cleanInfo = cleantext.cleanUpInfo(info)
        offer.update({"productId": productId})
        offer.update({"product": cleanTitle})
        offer.update({"productInfo": cleanInfo})
        offer.update({"category": categorize.findCategoryForProduct(cleanTitle, cleanInfo)})
        offer.update({"deal": deal})
        offer.update({"dateStart": dateStart})
        offer.update({"dateEnd": dateEnd})
        offer.update({"price": float(price)})
        offer.update({"image": imageLink})
        offer.update({"link": link})
        offer.update({"shop": SHOP})
        if(offer.get('deal') != ""): # if no deal is found, don't add it
            collection.append(offer)

    print("📄 " + str(len(collection)) + " aanbiedingen van de " + SHOP + " bij elkaar verzameld.")
    return collection

if __name__ == "__main__":
    returnOffers()