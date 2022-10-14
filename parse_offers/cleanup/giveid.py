
def giveIdToOffers(offers):
    """Adds a id to each offer in the offers dictionary."""

    key = "id"
    value = 0

    for offer in offers:
        value = value + 1
        offer[key] = value

    return offers;