
def clean_up_title(title):
    """Removes words from a string that are not useful."""

    badWords = ['PLUS ', 'Alle AH ', 'Diverse AH ', 'Alle ', 'AH ', '*', 'Jumbo ', '1 de beste ', '1 de Beste ']

    title = title.replace("’", "'") # sanitize different kinds of apostrophes
    title = title.replace(" ", " ") # sanitize U+00a0
    title = title.replace("­", "") # sanitize U+00ad

    for word in badWords:
        title = title.replace(word, '')

    clean_title = title.strip().capitalize()

    return clean_title

def clean_up_info(info_text):
    """Removes words from a string that are not useful."""

    if 'Bijv.' in info_text:
        info_text = ""
    else:
        bad_words = ['PLUS ', 'Jumbo ', 'Alle soorten\n3 verpakkingen',
                    'Alle soorten\n2 verpakkingen',
                    'Alle soorten ', 'Alle soorten\n', 'Alle soorten',
                    'Alle soorten\n2 ', 'Alle soorten\n3 ', 'Alle soorten, ',
                    'Alle combinaties mogelijk ', 'Diverse soorten',
                    'Alle varianten', 'Per stuk', 'Alle verpakkingen',
                    'Diverse varianten, combineren mogelijk', '<ul><li>',
                    '<li>', '</li><li>', '</li>', '</ul>', '&nbsp;', '&oslash;',
                    '</li></ul>', '<p>', '</p>', 'prijsvoorbeeld:']

        info_text = info_text.replace("’", "'") # sanitize different kinds of apostrophes
        info_text = info_text.replace(" ", " ") # sanitize weird space character

        for word in bad_words:
            info_text = info_text.replace(word, '')

    if len(info_text) == 1:
        info_text = ""

    clean_info_text = info_text.strip().rstrip(".").capitalize()

    return clean_info_text
