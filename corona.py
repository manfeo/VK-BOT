import requests
import json
from get_picture import getPictures, getOnePicture, getWholePicture
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import re
def getWholeKorona(upload):
    attachment = []
    photo = upload.photo_messages("covid.png")
    owner_id = photo[0]["owner_id"]
    photo_id = photo[0]["id"]
    access_key = photo[0]["access_key"]
    attachment.append(f"photo{owner_id}_{photo_id}_{access_key}")
    return attachment


def getKorona(type, upload):
    needed_town = type.split()
    if len(needed_town) == 1:
        needed_town = "Москва"
    else:
        needed_town = " ".join(needed_town[1:])
        if "область" in needed_town:
            needed_town = needed_town.replace("область", "обл.")
        """
        for i in range(1, len(needed_town)):
            if needed_town[i] == "край" or needed_town[i] == "округ" or needed_town[i] == "республика" or needed_town[i] == "область" \
                    or needed_town[i] == "автономный" or needed_town[i] == "автономная":
                if needed_town[i] == "край" or needed_town[i] == "округ":
                    if needed_town_str != "":
                        needed_town_str += " " + needed_town[i]
                    else:
                        needed_town_str += needed_town[i]
                if needed_town[i] == "область":
                    if needed_town_str != "":
                        needed_town_str += " обл."
                    else:
                        needed_town_str += "обл."
                if needed_town[i] == "республика":
                    if needed_town_str != "":
                        needed_town_str += " " + needed_town[i].title()
                    else:
                        needed_town_str += needed_town[i].title()
                if needed_town[i] == "автономный" or needed_town[i] == "автономный":
                    if needed_town_str != "":
                        needed_town_str += " " + needed_town[i]
                    else:
                        needed_town_str += needed_town[i]
                """
    page = requests.get("https://coronavirusstat.ru/country/russia/")
    soup = BeautifulSoup(page.text, "html.parser")
    text = soup.get_text()
    when = soup.find("h6", {"class": "text-muted"}).get_text()
    when = when[:when.find("Обновление")]
    text = text[text.find("1 Москва"):]
    text = text[:text.find("Сводный график")]
    text = text.split("\n\n\n")
    oneToCreate = text[0].split("\n")
    dictionaryForCities = {}
    for i in range(len(oneToCreate)):
        oneToCreate[i] = oneToCreate[i].split()
    oneToCreate = list(filter(None, oneToCreate))
    oneToCreate.pop(-1)
    oneToCreate.pop(-1)
    oneToCreate.pop(-1)
    for i in range(len(oneToCreate)):
        counter = 0
        place = ""
        for k in oneToCreate[i]:
            if k == "Активных":
                break
            if counter != 0:
                place += k + " "
            counter = 1
        if needed_town.lower() in place.lower():
            dictionaryForCities[place] = "регион: {}\n".format(place)
            if oneToCreate[i][oneToCreate[i].index("Случаев") + 1] != oneToCreate[i][len(oneToCreate[i]) - 1]:
                dictionaryForCities[place] += "Случаев: {} ({} за сегодня)\n".format(
                    oneToCreate[i][oneToCreate[i].index("Случаев") + 1],
                    oneToCreate[i][oneToCreate[i].index("Случаев") + 2])
            else:
                dictionaryForCities[place] += "Случаев: {}\n".format(oneToCreate[i][oneToCreate[i].index("Случаев") + 1])
            if oneToCreate[i][oneToCreate[i].index("Активных") + 2][0] == "+":
                dictionaryForCities[place] += "Активных: {} ({} за сегодня)\n".format(
                    oneToCreate[i][oneToCreate[i].index("Активных") + 1],
                    oneToCreate[i][oneToCreate[i].index("Активных") + 2])
            else:
                dictionaryForCities[place] += "Активных: {}\n".format(oneToCreate[i][oneToCreate[i].index("Активных") + 1])
            if oneToCreate[i][oneToCreate[i].index("Вылечено") + 2][0] == "+":
                dictionaryForCities[place] += "Вылечено: {} ({} за сегодня)\n".format(
                    oneToCreate[i][oneToCreate[i].index("Вылечено") + 1],
                    oneToCreate[i][oneToCreate[i].index("Вылечено") + 2])
            else:
                dictionaryForCities[place] += "Вылечено: {}\n".format(oneToCreate[i][oneToCreate[i].index("Вылечено") + 1],
                                                                      oneToCreate[i][oneToCreate[i].index("Вылечено") + 2])
            if oneToCreate[i][oneToCreate[i].index("Умерло") + 2][0] == "+":
                dictionaryForCities[place] += "Умерло: {} ({} за сегодня)\n".format(
                    oneToCreate[i][oneToCreate[i].index("Умерло") + 1], oneToCreate[i][oneToCreate[i].index("Умерло") + 2])
            else:
                dictionaryForCities[place] += "Умерло: {}\n".format(oneToCreate[i][oneToCreate[i].index("Умерло") + 1])
            break
    if len(dictionaryForCities) == 0:
        return "Такого города/области/края/республики на найдено..."
    str_to_return = "".join(dictionaryForCities.values())
    """
    twoToCreate.pop()
    twoToCreate = twoToCreate[0].split()
    for i in range(9):
        twoToCreate.pop(0)
    listYActive = []
    listYCured = []
    listYDead = []
    listX = []
    i = 0
    if twoToCreate[2][0] != "+":
        while i < len(twoToCreate):
            if "%" in twoToCreate[i] or "+" in twoToCreate[i] or twoToCreate[i][0] == "-":
                twoToCreate.pop(i)
            else:
                i += 1
        strToReturn = when + "\n" + "Случаев: {}\nАктивных: {}\nВылечено: {}\nУмерло: {}\n".format(twoToCreate[4],
                                                                                                   twoToCreate[1],
                                                                                                   twoToCreate[2],
                                                                                                   twoToCreate[3])
    else:
        strToReturn = when + "\n" + "Случаев: {} ({} за сегодня)\nАктивных: {} ({} за сегодня)\nВылечено: {} ({} за сегодня)\nУмерло: {} ({} за сегодня)\n".format(
            twoToCreate[10], twoToCreate[11], twoToCreate[1], twoToCreate[2], twoToCreate[4], twoToCreate[5],
            twoToCreate[7], twoToCreate[8])
    while i < len(twoToCreate):
        if "%" in twoToCreate[i] or "+" in twoToCreate[i] or twoToCreate[i][0] == "-":
            twoToCreate.pop(i)
        else:
            i += 1
    i = 0
    count = 0
    while count < 10:
        listX.append(twoToCreate[i])
        listYActive.append(twoToCreate[i + 1])
        listYCured.append(twoToCreate[i + 2])
        listYDead.append(twoToCreate[i + 3])
        i += 1
        count += 1
        if i + 3 == len(twoToCreate) - 1:
            break
        while not re.fullmatch("[0-9][0-9]\.[0-9][0-9]\.[0-9][0-9][0-9][0-9]", twoToCreate[i]):
            i += 1
    allInformation = ["Активных", "Вылечено", "Умерло"]
    fig, ax = plt.subplots()
    for i in range(len(listYCured)):
        listYActive[i] = float(listYActive[i])
        listYCured[i] = float(listYCured[i])
        listYDead[i] = float(listYDead[i])
    ax.stackplot(listX, listYActive, listYCured, listYDead, labels=allInformation)
    ax.legend(loc='upper left')
    ax.set_title("Россия - детальная статистика - короновирус")
    plt.xticks(rotation=20)
    fig.savefig("covid.png")
    attachments = getWholeKorona(upload)
    """
    return str_to_return