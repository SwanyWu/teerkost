
def cleanUpTitle(title):

    badWords = ['Alle AH ', 'Diverse AH ', 'Alle ', 'AH ', '*', 'Jumbo ']

    for word in badWords:
        title = title.replace(word, '')

    cleanTitle = title.strip().capitalize()
    
    return cleanTitle

def cleanUpInfo(infoText):

    badWords = ['Alle soorten ', 'Alle combinaties mogelijk ']

    for word in badWords:
        infoText = infoText.replace(word, '')

    cleanInfoText = infoText.strip().capitalize()
    
    return cleanInfoText
