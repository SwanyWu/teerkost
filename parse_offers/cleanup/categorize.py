import json
import sys
import os
import re

def find_category(title, description):
    """Finds and returns a category based on two provided strings."""

    CATEGORIES_JSON = os.path.join(os.path.dirname(__file__), "categories.json")

    with open(CATEGORIES_JSON, 'r') as jsonFile:
        data=jsonFile.read()

    categories = json.loads(data)
    words_list = []

    if ' ' in title: # space found, so split string by space
        words_list = re.split(' ', title.lower().replace(',', ''))
    else: # no space, just one word
        words_list.append(title.lower())

    description_word_list = re.split(' ', description.lower().replace(',', ''))
    words_list.extend(description_word_list)

    found_category = ""

    # 1 Select the categories to ignore when a bad word is found
    categories_to_ignore = []
    for word in words_list:
        for category in categories:
            for ignore in category['ignore']:
                if ignore.lower() == word:
                    categories_to_ignore.append(category['name'])

    # 2 Find and select the right category if matched to a singular keyword
    for word in words_list:
        for category in categories:
            for keyword in category['keywords']:
                if keyword.lower() == word and category['name'] not in categories_to_ignore:
                    found_category = category['name']

    # 3 If no category found, try and match with a string with whitespace in it.
    if found_category == "":
        complete_string = title.lower().replace(',', '') + description.lower().replace(',', '')
        for category in categories:
            for keywordWithSpace in category['keywordsWithSpace']:
                if keywordWithSpace.lower() in complete_string and category['name'] not in categories_to_ignore:
                    found_category = category['name']

    # If no category found, then use the nothing-found category
    if found_category == "":
        found_category = "geen-categorie"

    return found_category
