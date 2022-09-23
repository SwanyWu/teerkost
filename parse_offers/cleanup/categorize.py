import json
import sys
import os
import re

def findCategoryForProduct(title, description):
    """Finds and returns a category based on two provided strings."""

    CATEGORIES_JSON = os.path.join(os.path.dirname(__file__), "categories.json")

    with open(CATEGORIES_JSON, 'r') as jsonFile:
        data=jsonFile.read()

    categories = json.loads(data)
    wordsList = []

    if ' ' in title: # space found, so split string by space
        wordsList = re.split(' ', title.lower().replace(',', ''))
    else: # no space, just one word
        wordsList.append(title.lower()) 

    descriptionWordList = re.split(' ', description.lower().replace(',', ''))
    wordsList.extend(descriptionWordList)

    foundCategory = ""

    categoriesToIgnore = []
    for word in wordsList:
        for category in categories:
            for ignore in category['ignore']:
                if ignore.lower() == word: # bad word found, add category to ignoreList
                    categoriesToIgnore.append(category['name'])

    for word in wordsList:
        for category in categories:                
            for keyword in category['keywords']:
                if keyword.lower() == word and category['name'] not in categoriesToIgnore: # keyword matched and not an ignored category
                    foundCategory = category['name']
    
    if foundCategory is "":
        foundCategory = "geen-categorie"

    return foundCategory
