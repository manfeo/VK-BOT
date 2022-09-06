#Полное расписание для определённой группы
import requests
from bs4 import BeautifulSoup
import xlrd
from datetime import datetime
def get_schedule(group):
    page = requests.get("https://www.mirea.ru/schedule/")
    soup = BeautifulSoup(page.text, "html.parser")
    result = soup.find_all('a', {"class": "uk-link-toggle"})
    needed_link = ""
    #year = str(datetime.today().year % 100 - int(group.split('-')[2]))
    for links in result:
        if "IIT-" + str(3) in links.get(
                "href") and "зач_" not in links.get("href"):
            needed_link = links.get("href")
            break
    list = []
    resp = requests.get(needed_link)
    f = open("file.xlsx", "wb")
    f.write(resp.content)
    f.close()
    book = xlrd.open_workbook("file.xlsx")
    sheet_names = book.sheet_names()
    sheet = book.sheet_by_index(0)
    num_cols = sheet.ncols
    num_rows = sheet.nrows
    list = []
    i = 5
    raspisanie = {}
    for k in range(len(sheet_names)):
        sheet = book.sheet_by_index(k)
        while i < num_cols:
            needed = sheet.cell(1, i).value
            if needed == group:
                founder = i
                founderTwo = i
                while sheet.cell(3, founder).value != "ПОНЕДЕЛЬНИК":
                    founder -= 1
                while sheet.cell(3, founderTwo).value != "I":
                    founderTwo -= 1
                day = sheet.cell(3, founder).value.lower()
                j = 3
                while j < 76:
                    dayToCheck = sheet.cell(j, founder).value
                    if (dayToCheck == '' or dayToCheck.lower() == day) and j != 75:
                        one = sheet.cell(j, i + 1).value
                        two = sheet.cell(j, i + 2).value
                        three = sheet.cell(j, i + 3).value
                        four = sheet.cell(j, founderTwo).value
                        if one == "":
                            one = "-"
                        if two == "":
                            two = "-"
                        if three == "":
                            three = "-"
                        list.append(((sheet.cell(j, i).value + ", " + one + ", " + two + ", " + three), four))
                        j += 1
                        continue
                    else:
                        if list == []:
                            break
                        raspisanie[day] = list
                        list = []
                        day = dayToCheck.lower()
                        continue
                    j += 1
                break
            i += 5
        if raspisanie != {}:
            break;
        i = 5
    return raspisanie