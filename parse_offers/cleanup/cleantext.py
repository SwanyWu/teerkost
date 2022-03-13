
def cleanUpTitle(title):
    """Removes words from a string that are not useful."""

    badWords = ['Alle AH ', 'Diverse AH ', 'Alle ', 'AH ', '*', 'Jumbo ']

    for word in badWords:
        title = title.replace(word, '')

    cleanTitle = title.strip().capitalize()
    
    return cleanTitle

def cleanUpInfo(infoText):
    """Removes words from a string that are not useful."""

    badWords = ['Alle soorten ', 'Alle combinaties mogelijk ']

    for word in badWords:
        infoText = infoText.replace(word, '')

    cleanInfoText = infoText.strip().capitalize()
    
    return cleanInfoText
