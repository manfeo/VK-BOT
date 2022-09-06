from get_schedule_for_group import get_schedule
def getScheduleDay(day, group):
    group = "-".join(group.split("-")[:2]) + "-20"
    schedule = get_schedule(group)
    strToReturn = ""
    if day == "среда":
        strToReturn = "Расписание на чётную " + "среду" + "\n"
    elif day == "пятница":
        strToReturn = "Расписание на чётную " + "пятницу" + "\n"
    elif day == "суббота":
        strToReturn = "Расписание на чётную " + "субботу" + "\n"
    elif day == "воскресенье":
        return "В воскресенье нет пар! Отдыхаем" + "\n"
    else:
        strToReturn = "Расписание на чётный " + day + "\n"
    counter = 1
    counterTwo = 1
    for i in schedule[day]:
        if i[1] == "II":
            if i[0][0] == ",":
                strToReturn += str(counter) + ")" + " -" + "\n"
            else:
                strToReturn += str(counter) + ")" + i[0] + "\n"
            need = False
            for j in range(counterTwo, len(schedule[day])):
                if schedule[day][j][0][0] == ",":
                    need = True
                elif schedule[day][j][1] != "I":
                    need = False
                    break
            if need:
                break
            counter += 1
            counterTwo += 1
            continue
        counterTwo += 1
    strToReturn += "\n"
    if day == "среда":
        strToReturn += "Расписание на нечётную " + "среду" + "\n"
    elif day == "пятница":
        strToReturn += "Расписание на нечётную " + "пятницу" + "\n"
    elif day == "суббота":
        strToReturn += "Расписание на нечётную " + "субботу" + "\n"
    else:
        strToReturn += "Расписание на нечётный " + day + "\n"
    counter = 1
    counterTwo = 1
    for i in schedule[day]:
        if i[1] == "I":
            if i[0][0] == ",":
                strToReturn += str(counter) + ")" + " -" + "\n"
            else:
                strToReturn += str(counter) + ")" + i[0] + "\n"
            need = False
            for j in range(counterTwo, len(schedule[day])):
                if schedule[day][j][0][0] == ",":
                    need = True
                elif schedule[day][j][1] != "II":
                    need = False
                    break
            if need:
                break
            counter += 1
            counterTwo += 1
            continue
        counterTwo += 1
    strToReturn = "Расписание " + group + "\n" + strToReturn
    return strToReturn