import albertheijn
import jumbo
import lidl
import aldi
import ekoplaza
import dirk
import plus
import json
import shutil
import requests
from PIL import Image
from cleanup import giveid
import os
import time
import uuid

def updateImageUrlForOffer(url, offer):
    """Update the field for image in the json object"""

    if(offer['image'] == url):
        print("     🤔 De remote URL blijven we gebruiken: " + url)
    else:    
        offer.update({"image": url})
        print("     ✅ De lokale URL wordt gebruikt: " + url)


def tryAndSaveTheImage(url, destination):
    """Tries to download and save the image and convert it to webp format."""

    domain = "https://teerkost.nl/img/"
    resultingUrl = url

    try:
        response = requests.get(imageUrl,timeout=5)
        if response.status_code == 200:
            try:
                imageData = requests.get(imageUrl, headers=headers).content
                newFileName = str(uuid.uuid4().hex)
                with open(destination + '/'+ newFileName +'.png', 'wb') as i:
                    i.write(imageData)
                    print("     ✅ Afbeelding " + newFileName + " opslaan.")
                    
                    try:
                        img = Image.open(destination + '/' + newFileName +'.png')
                        img.save(destination + '/'+newFileName+'.webp', format="webp")
                        print("     ✅ Afbeelding geconverteerd naar webp.")
                        resultingUrl = domain + '' + newFileName + '.webp'
                        os.remove(destination + '/' + newFileName + '.png')
                    except Exception as e:
                        print("     " + e)
                        print("     🤔 Converteren naar webp mislukt, we blijven bij png.")
                        resultingUrl = domain + '' + newFileName + '.png'
            except Exception as e:
                print("     🟥 Opslaan is mislukt, we gaan verder.")
                pass
        else:
            print("     🟥 Antwoord " + str(response.status_code) + ", laat maar zitten.")
    except requests.exceptions.Timeout:
        print("     🟥 Time out ontvangen, laat maar zitten.")
            
    return resultingUrl

def moveFolder(folderPath, destination):
    """Moves the provided folder to the destination."""

    print(" ")
    if os.path.exists(destination):
        shutil.rmtree(destination)
        print("🧹 Folder " + folderPath + " bestaat op " + destination + ", die gooien we eerst weg.")

    shutil.move(folderPath, destination)
    if os.path.exists(destination):
        print("✅ Folder " + folderPath + " uit project verplaatst naar " + destination + ".")
    else:
        raise Exception("     🟥 Verplaatsen niet gelukt: folder " +folderPath + " niet gevonden op " + destination + ".")    

def moveFile(file, destination):
    """Moves the provided file to the destination."""

    if os.path.exists(destination + file):
        os.remove(destination + file)
        print("🧹 " + file + " bestaat op " + destination + ", die gooien we eerst weg.")
    
    print("🚀 Verplaats " + file + " uit het project naar " + destination + ".")
    shutil.move(file, destination + file)

if __name__ == "__main__":

    take_it_easy = 0

    allOffers = []
    try:
        jumboOffers = jumbo.returnOffers()
        allOffers = allOffers + jumboOffers
    except:
        print("🟥 Aanbiedingen ophalen voor Jumbo mislukt, wordt overgeslagen.")

    try:    
        ahOffers = albertheijn.returnOffers()
        allOffers = allOffers + ahOffers
    except:
        print("🟥 Aanbiedingen ophalen voor Jumbo mislukt, wordt overgeslagen.")

    try:
        lidlOffers = lidl.returnOffers()
        allOffers = allOffers + lidlOffers
    except:
        print("🟥 Aanbiedingen ophalen voor Lidl mislukt, wordt overgeslagen.")
    
    try:
        aldiOffers = aldi.returnOffers()
        allOffers = allOffers + aldiOffers
    except:
        print("🟥 Aanbiedingen ophalen voor Aldi mislukt, wordt overgeslagen.")

    try:
        dirkOffers = dirk.returnOffers()
        allOffers = allOffers + dirkOffers
    except:
        print("🟥 Aanbiedingen ophalen voor Dirk mislukt, wordt overgeslagen.")

    try:
        ekoplazaOffers = ekoplaza.returnOffers()
        allOffers = allOffers + ekoplazaOffers
    except:
        print("🟥 Aanbiedingen ophalen voor Ekoplaza mislukt, wordt overgeslagen.")

    try:
        plusOffers = plus.returnOffers()
        allOffers = allOffers + plusOffers
    except:
        print("🟥 Aanbiedingen ophalen voor Plus mislukt, wordt overgeslagen.")


    allOffers = giveid.giveIdToOffers(allOffers)
    allOffers = sorted(allOffers, key=lambda p: p['category'])

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
        }

    print("📄 Er zijn " + str(len(allOffers)) + " aanbiedingen gevonden.")
    time.sleep(take_it_easy)
    print("✊ Aan de slag met afbeeldingen downloaden en converteren naar webp.")
    time.sleep(take_it_easy)

    try:
        shutil.rmtree('parse_offers/img')
        print("🧹 Img folder met inhoud verwijderen uit het project.")
    except FileNotFoundError:
        print("🤔 Geen img folder gevonden in dit project om te verwijderen.")
    
    os.mkdir('parse_offers/img')
    print("✅ Schone img folder gemaakt in het project.")

    time.sleep(take_it_easy)
    index = 0    
    try:
        for offer in allOffers:
            print(" ")
            print("# " + str(index+1))
            index = index+1
            imageUrl = offer['image']
            destination = 'parse_offers/img'
            resultingUrl = tryAndSaveTheImage(imageUrl, destination)
            updateImageUrlForOffer(resultingUrl, offer)

    except Exception as e:
        print(e)

    time.sleep(take_it_easy)

    moveFolder('parse_offers/img', 'kortings-app/public/img')

    time.sleep(take_it_easy)
    print("✅ Dump de aanbiedingen in een JSON bestand.")
    with open('offers.json', 'a+', encoding='utf-8') as f:
            json.dump(allOffers, f, indent=4,ensure_ascii = False)
    
    moveFile('offers.json', 'kortings-app/src/')
