import json

def findCategoryForProduct(title, description):

    CATEGORIES_JSON = "parse_offers/categories.json"

    with open(CATEGORIES_JSON, 'r') as jsonFile:
        data=jsonFile.read()

    categories = json.loads(data)

    title.lower()
    description.lower()
    
    wordsList = title.split(' ')
    descriptionWordList = description.split(' ')
    wordsList.extend(descriptionWordList)

    foundCategory = ""

    for word in wordsList:
        for k in categories:
            for keyword in k['keywords']:
                if keyword == word:
                    print("Product gevonden in categorie: " + k['name'])
                    foundCategory = k['name']
    
    return foundCategory
