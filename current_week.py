#Получить текущую неделю
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from calendar import monthrange
def get_current_week():
    total_weeks = 0
    current_month = datetime.today().month
    current_year = datetime.today().year
    current_day = datetime.today().day
    iterator_day = 1
    iterator_month = 9
    while iterator_month != current_month or iterator_day != current_day:
        stringi = "{}/{}/{}".format(iterator_day, iterator_month, current_year)
        if datetime.weekday(datetime.strptime(stringi, "%d/%m/%Y")) == 6:
            total_weeks += 1
        if iterator_day == monthrange(current_year, iterator_month)[1]:
            iterator_month += 1
            iterator_day = 1
        iterator_day += 1
    return total_weeks + 1