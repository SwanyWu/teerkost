import json
import sys
import os

def findCategoryForProduct(title, description):

    CATEGORIES_JSON = os.path.join(os.path.dirname(__file__), "categories.json")

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
                    foundCategory = k['name']
    
    return foundCategory
