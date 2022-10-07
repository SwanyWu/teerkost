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

    # 1 Select the categories to ignore when a bad word is found
    categoriesToIgnore = []
    for word in wordsList:
        for category in categories:
            for ignore in category['ignore']:
                if ignore.lower() == word:
                    categoriesToIgnore.append(category['name'])

    # 2 Find and select the right category if matched to a singular keyword
    for word in wordsList:
        for category in categories:                
            for keyword in category['keywords']:
                if keyword.lower() == word and category['name'] not in categoriesToIgnore:
                    foundCategory = category['name']

    # 3 If no category found, try and match with a string with whitespace in it.
    if foundCategory == "":
        completeString = title.lower().replace(',', '') + description.lower().replace(',', '')
        for category in categories:
            for keywordWithSpace in category['keywordsWithSpace']:
                if keywordWithSpace.lower() in completeString and category['name'] not in categoriesToIgnore:
                    foundCategory = category['name']

    # If no category found, then use the nothing-found category
    if foundCategory == "":
        foundCategory = "geen-categorie"

    return foundCategory
