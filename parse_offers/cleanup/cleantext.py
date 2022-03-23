
def cleanUpTitle(title):
    """Removes words from a string that are not useful."""

    badWords = ['Alle AH ', 'Diverse AH ', 'Alle ', 'AH ', '*', 'Jumbo ']

    for word in badWords:
        title = title.replace(word, '')

    cleanTitle = title.strip().capitalize()
    
    return cleanTitle

def cleanUpInfo(infoText):
    """Removes words from a string that are not useful."""

    badWords = ['Jumbo ', 'Alle soorten\n3 verpakkingen', 'Alle soorten\n2 verpakkingen',
    'Alle soorten ', 'Alle soorten\n',
    'Alle soorten\n2 ', 'Alle soorten\n3 ', 'Alle soorten, ', 'Alle combinaties mogelijk ']

    for word in badWords:
        infoText = infoText.replace(word, '')

    cleanInfoText = infoText.strip().capitalize()
    
    return cleanInfoText
