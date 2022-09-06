from get_schedule_for_group import get_schedule
from constants import allMonths, days
from datetime import datetime
from current_week import get_current_week
#Расписание для группы на сегодня/завтра
def getScheduleForDay(group, daySet):
    day = 0
    if daySet == "на сегодня":
        day = datetime.today().weekday()
        if day == 6:
            return "Сегодня нет пар! Отдыхаем!"
    else:
        day = datetime.today().weekday() + 1
        if day == 6:
            return "Сегодня нет пар! Отдыхаем!"
        if day == 7:
            day = 0
    """
    if daySet == "на сегодня":
        day_toDay = datetime.now().day
    else:
        day_toDay = datetime.now().day + 1
    """
    day_toDay = datetime.now().day
    strToReturn = "Расписание на " + str(day_toDay) + " " + allMonths[datetime.today().month - 1] + "\n"
    raspisanie = get_schedule(group)
    today = days[day]
    weekNow = get_current_week()
    if weekNow % 2 == 0:
        counter = 1
        counterTwo = 1
        for i in raspisanie[today]:
            if i[1] == "II":
                if i[0][0] == ",":
                    strToReturn += str(counter) + ")" + " -" + "\n"
                else:
                    strToReturn += str(counter) + ")" + i[0] + "\n"
                need = False
                for j in range(counterTwo, len(raspisanie[today])):
                    if raspisanie[today][j][0][0] == ",":
                        need = True
                    elif raspisanie[today][j][1] != "I":
                        need = False
                        break
                if need:
                    break
                counter += 1
                counterTwo += 1
                continue
            counterTwo += 1
    else:
        counter = 1
        counterTwo = 1
        for i in raspisanie[today]:
            if i[1] == "I":
                if i[0][0] == ",":
                    strToReturn += str(counter) + ")" + " -" + "\n"
                else:
                    strToReturn += str(counter) + ")" + i[0] + "\n"
                need = False
                for j in range(counterTwo, len(raspisanie[today])):
                    if raspisanie[today][j][0][0] == ",":
                        need = True
                    elif raspisanie[today][j][1] != "II":
                        need = False
                        break
                if need:
                    break
                counter += 1
                counterTwo += 1
                continue
            counterTwo += 1
    return strToReturn
