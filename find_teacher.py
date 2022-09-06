import requests
from bs4 import BeautifulSoup
import xlrd
from datetime import datetime
def findTeacher(name):
    page = requests.get("https://www.mirea.ru/schedule/")
    soup = BeautifulSoup(page.text, "html.parser")
    hrefs = soup.find_all('a', {"class": "uk-link-toggle"})
    result = []
    for links in hrefs:
        link = links.get("href")
        if "IIT-" in link and "зач_" not in link and "экз_" not in link:
            result.append(link)
    dictionary = {}
    for j in result:
        resp = requests.get(j)
        f = open("file.xlsx", "wb")
        f.write(resp.content)
        f.close()
        book = xlrd.open_workbook("file.xlsx")
        sheet_names = book.sheet_names()
        sheet = book.sheet_by_index(0)
        num_cols = sheet.ncols
        num_rows = sheet.nrows
        stolb = 7
        strok = 3
        for k in range(len(sheet_names)):
            sheet = book.sheet_by_index(k)
            stolb = 7
            strok = 3
            while stolb < num_cols:
                while strok < 75:
                    if name in sheet.cell(strok, stolb).value:
                        """
                        if len(sheet.cell(strok, stolb).value.split()) > 2:
                            find = sheet.cell(strok, stolb).value.split()
                            iterator = 0
                            while iterator < len(find):
                                if find[iterator] == name:
                                    if "\n" in find[iterator]:
                                        find[iterator] = find[iterator].replace("\n", "")
                                    if len(find[iterator + 1]) > 4:
                                        for each in range(len(find[iterator + 1])):
                                            if find[iterator + 1][each] == ".":
                                                if find[iterator + 1][each + 1] == ".":
                                                    find[iterator + 1] = find[iterator + 1][:each + 1] + find[iterator + 1][
                                                                                                         each + 2:]
                                                    break
                                    if len(find[iterator + 1]) > 4:
                                        for each in range(len(find[iterator + 1])):
                                            if find[iterator + 1][each] == ".":
                                                if find[iterator + 1][each + 2] == ".":
                                                    find[iterator + 2] = find[iterator + 1][each + 3:] + " " + find[
                                                        iterator + 2]
                                                    find[iterator + 1] = find[iterator + 1][:each + 2]
                                                    break
                                    if find[iterator + 1][2] == ".":
                                        find[iterator + 1] = find[iterator + 1][:2] + find[iterator + 1][3:]
                                    if find[iterator + 1][-1] != ".":
                                        find[iterator + 1] += "."
                                    if find[iterator] + " " + find[iterator + 1] not in dictionary:
                                        dictionary[find[iterator] + " " + find[iterator + 1]] = [cours]
                                    else:
                                        if cours not in dictionary[find[iterator] + " " + find[iterator + 1]]:
                                            dictionary[find[iterator] + " " + find[iterator + 1]].append(cours)
                                iterator += 2
                            strok += 1
                            continue
                        """
                        teacher = sheet.cell(strok, stolb).value
                        if len(teacher.split("\n")) > 1:
                            teacher = teacher.split("\n")
                            for one in teacher:
                                if one == name:
                                    if one not in dictionary:
                                        dictionary[one] = [j]
                                    else:
                                        if j not in dictionary[one]:
                                            dictionary[one].append(j)
                        else:
                            if teacher not in dictionary:
                                dictionary[teacher] = [j]
                            else:
                                if j not in dictionary[teacher]:
                                    dictionary[teacher].append(j)
                    strok += 1
                strok = 3
                stolb += 5
                if stolb > num_cols:
                    break
    return dictionary