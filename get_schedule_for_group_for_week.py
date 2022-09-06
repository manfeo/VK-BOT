from constants import allMonths, days
from get_schedule_for_group import get_schedule
from current_week import get_current_week
from datetime import datetime
def getForWeek(week, schedule, date, day, month):
    if date == "воскресенье":
        return "Расписание на " + date + " " + str(day) + " " + allMonths[
            month - 1] + "\n" + "Сегодня выходной! Отдыхаем!"
    strReturn = ""
    if week % 2 == 0:
        if date == "срeда":
            strReturn = "Расписание на " + "среду" + " " + str(day) + " " + allMonths[month - 1] + "\n"
        elif date == "пятница":
            strReturn = "Расписание на " + "пятницу" + " " + str(day) + " " + allMonths[month - 1] + "\n"
        elif date == "суббота":
            strReturn = "Расписание на " + "субботу" + " " + str(day) + " " + allMonths[month - 1] + "\n"
        else:
            strReturn = "Расписание на " + date + " " + str(day) + " " + allMonths[month - 1] + "\n"
        counter = 1
        counterTwo = 1
        for i in schedule[date]:
            if i[1] == "II":
                if i[0][0] == ",":
                    strReturn += str(counter) + ")" + " -" + "\n"
                else:
                    strReturn += str(counter) + ")" + i[0] + "\n"
                need = False
                for j in range(counterTwo, len(schedule[date])):
                    if schedule[date][j][0][0] == ",":
                        need = True
                    elif schedule[date][j][1] != "I":
                        need = False
                        break
                if need:
                    break
                counter += 1
                counterTwo += 1
                continue
            counterTwo += 1
    else:
        if date == "среда":
            strReturn = "Расписание на " + "среду" + " " + str(day) + " " + allMonths[month - 1] + "\n"
        elif date == "пятница":
            strReturn = "Расписание на " + "пятницу" + " " + str(day) + " " + allMonths[month - 1] + "\n"
        elif date == "суббота":
            strReturn = "Расписание на " + "субботу" + " " + str(day) + " " + allMonths[month - 1] + "\n"
        else:
            strReturn = "Расписание на " + date + " " + str(day) + " " + allMonths[month - 1] + "\n"
        counter = 1
        counterTwo = 1
        for i in schedule[date]:
            if i[1] == "I":
                if i[0][0] == ",":
                    strReturn += str(counter) + ")" + " -" + "\n"
                else:
                    strReturn += str(counter) + ")" + i[0] + "\n"
                need = False
                for j in range(counterTwo, len(schedule[date])):
                    if schedule[date][j][0][0] == ",":
                        need = True
                    elif schedule[date][j][1] != "II":
                        need = False
                        break
                if need:
                    break
                counter += 1
                counterTwo += 1
                continue
            counterTwo += 1
    return strReturn


def getScheduleForWeek(week, group):
    neededWeek = 0
    flag = False
    weekNow = get_current_week()
    if week == "на эту неделю":
        neededWeek = weekNow
    else:
        neededWeek = weekNow + 1
        flag = True
    schedule = get_schedule(group)
    strToReturn = ""
    today = datetime.today().weekday()
    day = datetime.today().day
    month = datetime.today().month
    year = datetime.today().year
    if flag:
        day += 7
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            if day > 31:
                day = day - 31
                if month == 12:
                    month = 1
                else:
                    month += 1
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day > 30:
                day = day - 30
                month += 1
        if month == 2:
            if year % 4 == 0:
                if day > 29:
                    day = day - 29
                    month += 1
            else:
                if day > 28:
                    day = day - 28
                    month += 1
    if day < today + 1:
        if month == 2 or month == 4 or month == 6 or month == 9 or month == 11 or month == 8 or month == 1:
            day = 31 + day - today
            if month == 1:
                month = 12
            else:
                month -= 1
        elif month == 5 or month == 7 or month == 10 or month == 12:
            day = 30 + day - today
            month -= 1
        elif month == 3:
            if year % 4 == 0:
                day = 29 + day - today
                month -= 1
            else:
                day = 28 + day - today
                month -= 1
    else:
        day -= today
    for i in days:
        strToReturn += getForWeek(neededWeek, schedule, i, day, month) + "\n"
        if month == 3 or month == 5 or month == 8 or month == 10 or month == 1 or month == 7 or month == 12:
            if day == 31:
                day = 1;
                if month == 12:
                    month = 1
                    continue
                else:
                    month += 1
                    continue
            else:
                day += 1
        if month == 4 or month == 6 or month == 9 or month == 11:
            if day == 30:
                day = 1
                month += 1
                continue
            else:
                day += 1
        if month == 2:
            if year % 4 == 0:
                if day == 29:
                    day = 1
                    month += 1
                    continue
                else:
                    day += 1
            else:
                if day == 28:
                    day = 1
                    month += 1
                    continue
                else:
                    day += 1
    return strToReturn