
def calculate_percentage(old_price: str, new_price: str):
    ''' Returns calculate percentage string by old and new price '''
    calculated_deal = int((1 - (float(new_price)/float(old_price))) * 100)
    
    return str(calculated_deal)