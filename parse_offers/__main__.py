import albertheijn
import jumbo
import shutil


if __name__ == "__main__":
    albertheijn
    jumbo

    shutil.move('offer-ah.json', 'kortings-app/src/offer-ah.json')
    shutil.move('offer-jumbo.json', 'kortings-app/src/offer-jumbo.json')