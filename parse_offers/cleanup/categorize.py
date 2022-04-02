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

    for word in wordsList:
        for category in categories:
            for keyword in category['keywords']:
                if keyword.lower() == word: # keyword matched, so use the relevant category
                    foundCategory = category['name']
                        
    if foundCategory != "": # if category found, check for words that should be ignored
        for word in wordsList:
            for category in categories:
                if category['name'] == foundCategory:
                    for ignore in category['ignore']:
                        if ignore.lower() == word: # bad word found, so remove category
                            foundCategory = ""

    return foundCategory
