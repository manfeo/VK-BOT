def upDayAndMonth(month, day):
    if month == 3 or month == 5 or month == 8 or month == 10 or month == 1 or month == 7 or month == 12:
        if day == 31:
            day = 1;
            if month == 12:
                month = 1
            else:
                month += 1
        else:
            day += 1
    if month == 4 or month == 6 or month == 9 or month == 11:
        if day == 30:
            day = 1
            month += 1
        else:
            day += 1
    if month == 2:
        if year % 4 == 0:
            if day == 29:
                day = 1
                month += 1
            else:
                day += 1
        else:
            if day == 28:
                day = 1
                month += 1
            else:
                day += 1
    return (day, month)