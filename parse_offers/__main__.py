import os
import time
import uuid
import albertheijn
import jumbo
import lidl
import aldi
import ekoplaza
import dirk
import plus
import spar
import json
import shutil
import requests
from PIL import Image
from cleanup import giveid

def update_image_url_offer(url, offer):
    """Update the field for image in the json object"""

    if offer['image'] == url:
        print("     🤔 De remote URL blijven we gebruiken: " + url)
    else:
        offer.update({"image": url})
        print("     ✅ De lokale URL wordt gebruikt: " + url)


def try_and_save_image(url, destination):
    """Tries to download and save the image and convert it to webp format."""

    domain = "https://teerkost.nl/img/"
    resulting_url = url

    try:
        response = requests.get(imageUrl,timeout=5)
        if response.status_code == 200:
            try:
                imageData = requests.get(imageUrl, headers=headers).content
                new_filename = str(uuid.uuid4().hex)
                with open(destination + '/'+ new_filename +'.png', 'wb') as i:
                    i.write(imageData)
                    print("     ✅ Afbeelding " + new_filename + " opslaan.")

                    try:
                        img = Image.open(destination + '/' + new_filename +'.png')
                        img.save(destination + '/'+new_filename+'.webp', format="webp")
                        print("     ✅ Afbeelding geconverteerd naar webp.")
                        resulting_url = domain + '' + new_filename + '.webp'
                        os.remove(destination + '/' + new_filename + '.png')
                    except Exception as e:
                        print("     " + e)
                        print("     🤔 Converteren naar webp mislukt, we blijven bij png.")
                        resulting_url = domain + '' + new_filename + '.png'
            except Exception as e:
                print("     🟥 Opslaan is mislukt, we gaan verder.")
                pass
        else:
            print("     🟥 Antwoord " + str(response.status_code) + ", laat maar zitten.")
    except requests.exceptions.Timeout:
        print("     🟥 Time out ontvangen, laat maar zitten.")

    return resulting_url

def move_folder(folder_path, destination):
    """Moves the provided folder to the destination."""

    print(" ")
    if os.path.exists(destination):
        shutil.rmtree(destination)
        print("🧹 Folder " + folder_path + " bestaat op " + destination + ", die gooien we eerst weg.")

    shutil.move(folder_path, destination)
    if os.path.exists(destination):
        print("✅ Folder " + folder_path + " uit project verplaatst naar " + destination + ".")
    else:
        raise Exception("     🟥 Verplaatsen niet gelukt: folder " + folder_path + " niet gevonden op " + destination + ".")

def move_file(file, destination):
    """Moves the provided file to the destination."""

    if os.path.exists(destination + file):
        os.remove(destination + file)
        print("🧹 " + file + " bestaat op " + destination + ", die gooien we eerst weg.")

    print("🚀 Verplaats " + file + " uit het project naar " + destination + ".")
    shutil.move(file, destination + file)

if __name__ == "__main__":

    TAKE_IT_EASY = 0

    all_offers = []
    try:
        jumbo_offers = jumbo.return_offers()
        all_offers = all_offers + jumbo_offers
    except Exception:
        print("🟥 Aanbiedingen ophalen voor Jumbo mislukt, wordt overgeslagen.")

    try:
        ah_offers = albertheijn.return_offers()
        all_offers = all_offers + ah_offers
    except Exception:
        print("🟥 Aanbiedingen ophalen voor Jumbo mislukt, wordt overgeslagen.")

    try:
        lidl_offers = lidl.return_offers()
        all_offers = all_offers + lidl_offers
    except Exception:
        print("🟥 Aanbiedingen ophalen voor Lidl mislukt, wordt overgeslagen.")

    try:
        aldi_offers = aldi.return_offers()
        all_offers = all_offers + aldi_offers
    except Exception:
        print("🟥 Aanbiedingen ophalen voor Aldi mislukt, wordt overgeslagen.")

    try:
        dirk_offers = dirk.return_offers()
        all_offers = all_offers + dirk_offers
    except Exception:
        print("🟥 Aanbiedingen ophalen voor Dirk mislukt, wordt overgeslagen.")

    try:
        spar_offers = spar.return_offers()
        all_offers = all_offers + spar_offers
    except Exception:
        print("🟥 Aanbiedingen ophalen voor Spar mislukt, wordt overgeslagen.")

    try:
        ekoplaza_offers = ekoplaza.return_offers()
        all_offers = all_offers + ekoplaza_offers
    except Exception:
        print("🟥 Aanbiedingen ophalen voor Ekoplaza mislukt, wordt overgeslagen.")

    try:
        plus_offers = plus.return_offers()
        all_offers = all_offers + plus_offers
    except Exception:
        print("🟥 Aanbiedingen ophalen voor Plus mislukt, wordt overgeslagen.")


    all_offers = giveid.give_id_to_offers(all_offers)
    all_offers = sorted(all_offers, key=lambda p: p['category'])

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:97.0) Gecko/20100101 Firefox/97.0"
        }

    print("📄 Er zijn " + str(len(all_offers)) + " aanbiedingen gevonden.")
    time.sleep(TAKE_IT_EASY)
    print("✊ Aan de slag met afbeeldingen downloaden en converteren naar webp.")
    time.sleep(TAKE_IT_EASY)

    try:
        shutil.rmtree('parse_offers/img')
        print("🧹 Img folder met inhoud verwijderen uit het project.")
    except FileNotFoundError:
        print("🤔 Geen img folder gevonden in dit project om te verwijderen.")

    os.mkdir('parse_offers/img')
    print("✅ Schone img folder gemaakt in het project.")

    time.sleep(TAKE_IT_EASY)
    index = 0
    try:
        for offer in all_offers:
            print(" ")
            print("# " + str(index+1))
            index = index+1
            imageUrl = offer['image']
            destination = 'parse_offers/img'
            resulting_url = try_and_save_image(imageUrl, destination)
            update_image_url_offer(resulting_url, offer)

    except Exception as e:
        print(e)

    time.sleep(TAKE_IT_EASY)

    move_folder('parse_offers/img', 'kortings-app/public/img')

    time.sleep(TAKE_IT_EASY)
    print("✅ Dump de aanbiedingen in een JSON bestand.")
    with open('offers.json', 'a+', encoding='utf-8') as f:
        json.dump(all_offers, f, indent=4,ensure_ascii = False)

    move_file('offers.json', 'kortings-app/src/')
