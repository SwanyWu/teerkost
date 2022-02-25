
def cleanUpTitle(title):

    badWords = ['Alle AH ', 'Diverse AH ', 'Alle ', 'AH ', '*']

    for word in badWords:
        title = title.replace(word, '')

    cleanTitle = title.strip().capitalize()
    
    return cleanTitle