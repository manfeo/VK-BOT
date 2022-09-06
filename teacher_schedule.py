import requests
from bs4 import BeautifulSoup
import xlrd
from datetime import datetime
import re
from constants import allMonths,days
from current_week import get_current_week
from up_day_and_month import upDayAndMonth
def findAllLessonsForTeacher(nameTwo):
    page = requests.get("https://www.mirea.ru/schedule/")
    soup = BeautifulSoup(page.text, "html.parser")
    result = soup.find_all('a', {"class": "uk-link-toggle"})
    listOne = []
    for links in result:
        link = links.get("href")
        if "IIT-3" in link and "зач_" not in link:
            listOne.append(link)
    schedule = []
    raspisanie = {}
    resp = requests.get(listOne[0])
    f = open("file.xlsx", "wb")
    f.write(resp.content)
    f.close()
    book = xlrd.open_workbook("file.xlsx")
    sheet = book.sheet_by_index(0)
    sheet_names = book.sheet_names()
    num_cols = sheet.ncols
    num_rows = sheet.nrows
    stolb = 0
    strok = 0
    for k in range(len(sheet_names)):
        sheet = book.sheet_by_index(k)
        stolb = 7
        strok = 3
        while stolb < num_cols:
            founder = stolb
            founderTwo = stolb
            founderThree = stolb
            while sheet.cell(3, founder).value != "ПОНЕДЕЛЬНИК":
                founder -= 1
            while sheet.cell(3, founderTwo).value != "I":
                founderTwo -= 1
            while sheet.cell(3, founderThree).value != "1":
                founderThree -= 1
            day = sheet.cell(3, founder).value.lower()
            while strok < 76:
                group = sheet.cell(1, stolb - 2).value
                dayToCheck = sheet.cell(strok, founder).value
                if (dayToCheck == '' or dayToCheck.lower() == day) and strok != 75:
                    check = sheet.cell(strok, stolb).value
                    if re.fullmatch("\d+\.\d+", str(sheet.cell(strok, stolb).value)):
                        strok += 1
                        continue
                    if nameTwo in sheet.cell(strok, stolb).value and (
                            len(sheet.cell(strok, stolb).value.split()) > 2 or len(
                            sheet.cell(strok, stolb).value.split("\n")) > 2 or len(
                            sheet.cell(strok, stolb).value.split("/")) > 2):
                        temp = sheet.cell(strok, stolb).value
                        temp = temp.replace(",", "")
                        temp = temp.replace("/", "")
                        temp = temp.replace("\n", " ")
                        temp = temp.split()
                        tempTwo = sheet.cell(strok, stolb - 2).value
                        tempTwo = tempTwo.replace(",", "")
                        for strin in range(len(tempTwo)):
                            if tempTwo[strin] == "/":
                                if not re.fullmatch("\п\/\г", tempTwo[strin - 1] + tempTwo[strin] + tempTwo[strin + 1]):
                                    tempTwo[strin] = tempTwo[strin].replace("/", "")
                        tempTwo = tempTwo.split("\n")
                        tempThree = sheet.cell(strok, stolb + 1).value
                        tempThree = tempThree.replace(",", "")
                        tempThree = tempThree.replace("/", "")
                        tempThree = tempThree.replace("\n", " ")
                        tempThree = tempThree.split()
                        tempFour = sheet.cell(strok, stolb - 1).value
                        tempFour = tempFour.replace(",", "")
                        tempFour = tempFour.replace("/", "")
                        tempFour = tempFour.replace("\n", " ")
                        tempFour = tempFour.split()
                        u = 0
                        counterOthers = 0
                        while u < len(temp):
                            if temp[u] + " " + temp[u + 1] == nameTwo:
                                one = ""
                                if len(tempTwo) != 1:
                                    one = tempTwo[counterOthers]
                                else:
                                    one = tempTwo[0]
                                two = ""
                                if len(tempFour) != 1:
                                    if counterOthers >= len(tempFour):
                                        two = tempFour[counterOthers - 1]
                                    else:
                                        two = tempFour[counterOthers]
                                else:
                                    two = tempFour[0]
                                three = ""
                                if len(tempThree) == 1:
                                    three = tempThree[0]
                                else:
                                    if counterOthers >= len(tempThree):
                                        three = tempThree[counterOthers - 1]
                                    else:
                                        three = tempThree[counterOthers]
                                four = sheet.cell(strok, founderTwo).value
                                five = 0
                                if sheet.cell(strok, founderThree).value == "":
                                    five = sheet.cell(strok - 1, founderThree).value
                                else:
                                    five = sheet.cell(strok, founderThree).value
                                if one == "":
                                    one = "-"
                                if two == "":
                                    two = "-"
                                if three == "":
                                    three = "-"
                                schedule.append(((one + ", " + two + ", " + group + ", " + three), four, five))
                                strok += 1
                                break
                            else:
                                u += 2
                                counterOthers += 1
                        continue
                    if sheet.cell(strok, stolb).value == nameTwo:
                        one = sheet.cell(strok, stolb - 2).value
                        two = sheet.cell(strok, stolb - 1).value
                        three = sheet.cell(strok, stolb + 1).value
                        four = sheet.cell(strok, founderTwo).value
                        five = 0
                        if sheet.cell(strok, founderThree).value == "":
                            five = sheet.cell(strok - 1, founderThree).value
                        else:
                            five = sheet.cell(strok, founderThree).value
                        if one == "":
                            one = "-"
                        if two == "":
                            two = "-"
                        if three == "":
                            three = "-"
                        schedule.append(((one + ", " + two + ", " + group + ", " + three), four, five))
                        strok += 1
                        continue
                    else:
                        strok += 1
                        continue
                else:
                    if schedule == []:
                        strok += 1
                        day = dayToCheck.lower()
                        continue
                    if day in raspisanie:
                        for k in range(len(schedule)):
                            raspisanie[day].append(schedule[k])
                    else:
                        raspisanie[day] = schedule
                    schedule = []
                    day = dayToCheck.lower()
                    continue
                strok += 1
            strok = 3
            stolb += 5
            if stolb > num_cols:
                break
            if sheet.cell(strok - 1, stolb).value == "Нач.\nзанятий":
                stolb += 5
    return raspisanie

def getScheduleForTeacher(teacher, courses, when):
    weekNow = get_current_week()
    getSchedule = findAllLessonsForTeacher(teacher)
    end = []
    for every in getSchedule:
        for values in getSchedule[every]:
            end.append(values)
        end.sort(key=lambda x: x[-1])
        getSchedule[every] = end
        end = []
    sortedDic = {}
    for today in days:
        for day in getSchedule:
            if today == day:
                sortedDic[today] = getSchedule[day]
                break
    if when == "на сегодня" or when == "на завтра":
        strToReturn = ""
        day = 0
        now = 0
        if when == "на сегодня":
            day = datetime.today().weekday()
            now = datetime.today().day
            if day == 6:
                return "Сегодня нет пар у преподавателя"
        else:
            now = datetime.today().day + 1
            day = datetime.today().weekday() + 1
        if day == 6:
            return "Сегодня нет пар у преподавателя"
        if day == 7:
            day == 0
        strToReturn = "Расписание на " + str(now) + " " + allMonths[datetime.today().month - 1] + "\n"
        today = days[day]
        howToCount = 0
        if weekNow % 2 == 0:
            if today in sortedDic:
                for i in sortedDic[today]:
                    if i[1] == "II":
                        counterToCheck = howToCount
                        howToCount = round(i[2])
                        if howToCount - counterToCheck > 1:
                            for l in range(counterToCheck + 1, howToCount):
                                strToReturn += str(l) + ") - \n"
                        strToReturn += str(howToCount) + ")" + i[0] + "\n"
            else:
                strToReturn += "У преподавателя нет пар\n"
        else:
            if today in sortedDic:
                for i in sortedDic[today]:
                    if i[1] == "I":
                        counterToCheck = howToCount
                        howToCount = round(i[2])
                        if howToCount - counterToCheck > 1:
                            for l in range(counterToCheck + 1, howToCount):
                                strToReturn += str(l) + ") - \n"
                        strToReturn += str(howToCount) + ")" + i[0] + "\n"
            else:
                strToReturn += "У преподавателя нет пар\n"
        return strToReturn
    if when == "на эту неделю" or when == "на следующую неделю":
        neededWeek = 0
        flag = False
        if when == "на эту неделю":
            neededWeek = weekNow
        else:
            neededWeek = weekNow + 1
            flag = True
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
        counter = 0
        monthly = 0
        strToReturn = ""
        for dayss in sortedDic:
            while days[monthly] != dayss:
                if days[monthly] == "среда":
                    strToReturn += "Расписание на среду " + str(day) + " " + allMonths[
                        month - 1] + "\nУ преподавателя нет пар\n\n"
                    monthly += 1
                    cortege = upDayAndMonth(month, day)
                    month = cortege[1]
                    day = cortege[0]
                elif days[monthly] == "пятница":
                    strToReturn += "Расписание на пятницу" + str(day) + " " + allMonths[
                        month - 1] + "\nУ преподавателя нет пар\n\n"
                    monthly += 1
                    cortege = upDayAndMonth(month, day)
                    month = cortege[1]
                    day = cortege[0]
                elif days[monthly] == "суббота":
                    strToReturn += "Расписание на субботу" + str(day) + " " + allMonths[
                        month - 1] + "\nУ преподавателя нет пар\n\n"
                    monthly += 1
                    cortege = upDayAndMonth(month, day)
                    month = cortege[1]
                    day = cortege[0]
                else:
                    strToReturn += "Расписание на " + days[monthly] + " " + str(day) + " " + allMonths[
                        month - 1] + "\nУ преподавателя нет пар\n\n"
                    monthly += 1
                    cortege = upDayAndMonth(month, day)
                    month = cortege[1]
                    day = cortege[0]
            if dayss == "среда":
                strToReturn += "Расписание на среду " + str(day) + " " + allMonths[month - 1] + "\n"
            elif dayss == "пятница":
                strToReturn += "Расписание на пятницу " + str(day) + " " + allMonths[month - 1] + "\n"
            elif dayss == "суббота":
                strToReturn += "Расписание на субботу " + str(day) + " " + allMonths[month - 1] + "\n"
            else:
                strToReturn += "Расписание на " + dayss + " " + str(day) + " " + allMonths[month - 1] + "\n"
            added = False
            if neededWeek % 2 == 0:
                for lessons in sortedDic[dayss]:
                    if lessons[1] == "II":
                        added = True
                        counterToCheck = counter
                        counter = int(lessons[2])
                        if counter - counterToCheck > 1:
                            for l in range(counterToCheck + 1, counter):
                                strToReturn += str(l) + ") - \n"
                        strToReturn += str(counter) + ")" + lessons[0] + "\n"
                if not added:
                    strToReturn += "У преподавателя нет пар\n"
                strToReturn += "\n"
            else:
                for lessons in sortedDic[dayss]:
                    if lessons[1] == "I":
                        added = True
                        counterToCheck = counter
                        counter = int(lessons[2])
                        if counter - counterToCheck > 1:
                            for l in range(counterToCheck + 1, counter):
                                strToReturn += str(l) + ") - \n"
                        strToReturn += str(counter) + ")" + lessons[0] + "\n"
                if not added:
                    strToReturn += "У преподавателя нет пар\n"
                strToReturn += "\n"
            monthly += 1
            counter = 0
            cortege = upDayAndMonth(month, day)
            month = cortege[1]
            day = cortege[0]
        for en in range(monthly, len(days) - 1):
            if days[en] == "среда":
                strToReturn += "Расписание на среду " + str(day) + " " + allMonths[
                    month - 1] + "\nУ преподавателя нет пар\n\n"
                monthly += 1
                cortege = upDayAndMonth(month, day)
                month = cortege[1]
                day = cortege[0]
            elif days[en] == "пятница":
                strToReturn += "Расписание на пятницу " + str(day) + " " + allMonths[
                    month - 1] + "\nУ преподавателя нет пар\n\n"
                monthly += 1
                cortege = upDayAndMonth(month, day)
                month = cortege[1]
                day = cortege[0]
            elif days[en] == "суббота":
                strToReturn += "Расписание на субботу " + str(day) + " " + allMonths[
                    month - 1] + "\nУ преподавателя нет пар\n\n"
                monthly += 1
                cortege = upDayAndMonth(month, day)
                month = cortege[1]
                day = cortege[0]
            else:
                strToReturn += "Расписание на " + days[monthly] + " " + str(day) + " " + allMonths[
                    month - 1] + "\nУ преподавателя нет пар\n\n"
                monthly += 1
                cortege = upDayAndMonth(month, day)
                month = cortege[1]
                day = cortege[0]
        return strToReturn