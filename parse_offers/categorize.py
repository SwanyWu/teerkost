import json

def findCategoryForProduct(title, description):

    CATEGORIES_JSON = "parse_offers/categories.json"

    with open(CATEGORIES_JSON, 'r') as jsonFile:
        data=jsonFile.read()

    categories = json.loads(data)
    
    wordsList = title.lower().replace(',', '').split(' ')
    descriptionWordList = description.lower().replace(',', '').split(' ')
    wordsList.extend(descriptionWordList)

    foundCategory = ""

    for word in wordsList:
        for k in categories:
            for keyword in k['keywords']:
                if keyword.lower() == word:
                    print("Product gevonden in categorie: " + k['name'])
                    foundCategory = k['name']
    
    return foundCategory
