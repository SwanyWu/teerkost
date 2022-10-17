from datetime import datetime, timedelta

class CleandateException(Exception):
    """Exception raised for errors in cleandate"""

    def __init__(self):
        super().__init__("Cleandate could not handle whatever was expected.")

def return_full_datestring(year: str, month: str, day: str):
    ''' Returns yyyy-mm-dd formatted string '''
    datestring = year + "-" + month + "-" + day
    
    return datestring

def return_index_by_full_month_text(month: str):
    ''' Returns month index by full month text '''

    try:
        month = month.replace("\xa0", "")
        months = ["januari", "februari", "maart", "april", "mei",
        "juni", "juli", "augustus", "september", "oktober", "november", "december"]

        month_number = months.index(month) + 1
        month_number_string = format(month_number, '02')
    except:
        raise CleandateException()

    return month_number_string

def return_first_sunday_startdate_string(date_string: str):
    ''' Returns the coming week's starting sunday date from yyyy-mm-dd '''

    try:
        date_string = date_string.split("-")
        year = int(date_string[0])
        month = int(date_string[1])
        day = int(date_string[2])

        date = datetime(year,month,day)

        weekday_start = date.weekday()
        days_remaining = 6 - weekday_start

        new_date = date + timedelta(days=days_remaining)
        new_date_string = new_date.strftime('%Y-%m-%d')
    except:
        raise CleandateException()

    return str(new_date_string)

def return_weekday_string(date_string: str):
    ''' Returns weekday by yyyy-mm-dd formatted string '''

    try:
        date_string = date_string.split("-")
        year = int(date_string[0])
        month = int(date_string[1])
        day = int(date_string[2])

        date = datetime(year,month,day)

        days = ["maandag", "dinsdag", "woensdag",
            "donderdag", "vrijdag", "zaterdag", "zondag"]

        weekday = date.weekday()
    except:
        raise CleandateException()

    return days[weekday]

def return_calculated_date(date_string: str, plusDays: int):
    ''' Returns calculated yyyy-mm-dd string by adding days to yyyy-mm-dd date string'''

    try:
        date_string = date_string.split("-")
        year = int(date_string[0])
        month = int(date_string[1])
        day = int(date_string[2])

        date = datetime(year,month,day)
        new_date = date + timedelta(days=plusDays)
        new_date_string = new_date.strftime('%Y-%m-%d')
    except:
        raise CleandateException()

    return str(new_date_string)