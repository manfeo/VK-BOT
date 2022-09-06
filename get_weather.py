import requests
import json
from get_picture import getPictures, getOnePicture, getWholePicture
def getWeatherNow(info):
    strToReturn = ""
    if info["weather"][0]["description"] == "thunderstorm with light rain":
        strToReturn += "Гроза с небольшим дождем, "
    elif info["weather"][0]["description"] == "thunderstorm with rain":
        strToReturn += "Гроза с дождем, "
    elif info["weather"][0]["description"] == "thunderstorm with heavy rain":
        strToReturn += "Гроза с сильным дождем, "
    elif info["weather"][0]["description"] == "light thunderstorm":
        strToReturn += "Легкая гроза, "
    elif info["weather"][0]["description"] == "thunderstorm":
        strToReturn += "Гроза, "
    elif info["weather"][0]["description"] == "heavy thunderstorm":
        strToReturn += "Сильная гроза, "
    elif info["weather"][0]["description"] == "ragged thunderstorm":
        strToReturn += "Переменная гроза, "
    elif info["weather"][0]["description"] == "thunderstorm with light drizzle":
        strToReturn += "Гроза с легкой моросью, "
    elif info["weather"][0]["description"] == "thunderstorm with drizzle":
        strToReturn += "Гроза с моросью, "
    elif info["weather"][0]["description"] == "thunderstorm with heavy drizzle":
        strToReturn += "Гроза с сильным дождем, "
    elif info["weather"][0]["description"] == "light intensity drizzle":
        strToReturn += "Слабая морось, "
    elif info["weather"][0]["description"] == "drizzle":
        strToReturn += "Морось, "
    elif info["weather"][0]["description"] == "heavy intensity drizzle":
        strToReturn += "Сильный дождь, "
    elif info["weather"][0]["description"] == "light intensity drizzle rain":
        strToReturn += "Моросящий дождь лёгкой интенсивности, "
    elif info["weather"][0]["description"] == "drizzle rain":
        strToReturn += "Моросящий дождь, "
    elif info["weather"][0]["description"] == "heavy intensity drizzle rain":
        strToReturn += "Сильный моросящий дождь, "
    elif info["weather"][0]["description"] == "shower rain and drizzle":
        strToReturn += "Ливень, дождь и изморось, "
    elif info["weather"][0]["description"] == "shower drizzle":
        strToReturn += "Изморось, "
    elif info["weather"][0]["description"] == "light rain":
        strToReturn += "Легкий дождь, "
    elif info["weather"][0]["description"] == "moderate rain":
        strToReturn += "Умеренный дождь, "
    elif info["weather"][0]["description"] == "heavy intensity rain":
        strToReturn += "Сильный дождь, "
    elif info["weather"][0]["description"] == "very heavy rain":
        strToReturn += "Очень сильный дождь, "
    elif info["weather"][0]["description"] == "extreme rain":
        strToReturn += "Сильнейший дождь, "
    elif info["weather"][0]["description"] == "freezing rain":
        strToReturn += "Ледяной дождь, "
    elif info["weather"][0]["description"] == "light intensity shower rain":
        strToReturn += "Ливень лёгкой интенсивности, "
    elif info["weather"][0]["description"] == "shower rain":
        strToReturn += "Ливень, "
    elif info["weather"][0]["description"] == "heavy intensity shower rain":
        strToReturn += "Сильный ливневый дождь, "
    elif info["weather"][0]["description"] == "ragged shower rain":
        strToReturn += "Переменный ливень, "
    elif info["weather"][0]["description"] == "light snow":
        strToReturn += "Легкий снег, "
    elif info["weather"][0]["description"] == "Snow":
        strToReturn += "Снег, "
    elif info["weather"][0]["description"] == "Heavy snow":
        strToReturn += "Снегопад, "
    elif info["weather"][0]["description"] == "Sleet":
        strToReturn += "Мокрый снег, "
    elif info["weather"][0]["description"] == "Light shower sleet":
        strToReturn += "Слабый дождь, "
    elif info["weather"][0]["description"] == "Shower sleet":
        strToReturn += "Дождь, "
    elif info["weather"][0]["description"] == "Light rain and snow":
        strToReturn += "Небольшой дождь со снегом, "
    elif info["weather"][0]["description"] == "Rain and snow":
        strToReturn += "Дождь со снегом, "
    elif info["weather"][0]["description"] == "Light shower snow":
        strToReturn += "Легкий снегопад, "
    elif info["weather"][0]["description"] == "Shower snow":
        strToReturn += "Снегопад, "
    elif info["weather"][0]["description"] == "Heavy shower snow":
        strToReturn += "Сильный снегопад, "
    elif info["weather"][0]["description"] == "mist":
        strToReturn += "Лёгкий туман, "
    elif info["weather"][0]["description"] == "Smoke":
        strToReturn += "Дымка, "
    elif info["weather"][0]["description"] == "Haze":
        strToReturn += "Туман, "
    elif info["weather"][0]["description"] == "sand/ dust whirls":
        strToReturn += "Песчано-пыльные вихри, "
    elif info["weather"][0]["description"] == "fog":
        strToReturn += "Густой туман, "
    elif info["weather"][0]["description"] == "sand":
        strToReturn += "Песчано, "
    elif info["weather"][0]["description"] == "dust":
        strToReturn += "Пыльно, "
    elif info["weather"][0]["description"] == "volcanic ash":
        strToReturn += "Вулканический пепел, "
    elif info["weather"][0]["description"] == "squalls":
        strToReturn += "Шквал, "
    elif info["weather"][0]["description"] == "tornado":
        strToReturn += "Торнадо, "
    elif info["weather"][0]["description"] == "clear sky":
        strToReturn += "Ясное небо, "
    elif info["weather"][0]["description"] == "few clouds":
        strToReturn += "Рассеянная облачность, "
    elif info["weather"][0]["description"] == "scattered clouds":
        strToReturn += "Разбросанная облачность, "
    elif info["weather"][0]["description"] == "broken clouds":
        strToReturn += "Значительная облачность, "
    elif info["weather"][0]["description"] == "overcast clouds":
        strToReturn += "Сплошная облачность, "
    if str(round(info["main"]["temp_min"])) != str(round(info["main"]["temp_max"])):
        strToReturn += "температура: " + str(round(info["main"]["temp_min"])) + "-" + str(
            round(info["main"]["temp_max"])) + "°C\n"
    else:
        strToReturn += "температура: " + str(round(info["main"]["temp_min"])) + "°C\n"
    strToReturn += "Давление: " + str(info["main"]["pressure"]) + " мм рт.ст., влажность: " + str(
        info["main"]["humidity"]) + "%\n"
    wind = ""
    direction = ""
    if info["wind"]["speed"] <= 0.2:
        wind = "штиль"
    elif info["wind"]["speed"] >= 0.3 and info["wind"]["speed"] <= 1.5:
        wind = "тихий"
    elif info["wind"]["speed"] >= 1.6 and info["wind"]["speed"] <= 3.3:
        wind = "лёгкий"
    elif info["wind"]["speed"] >= 3.4 and info["wind"]["speed"] <= 5.4:
        wind = "слабый"
    elif info["wind"]["speed"] >= 5.5 and info["wind"]["speed"] <= 7.9:
        wind = "умеренный"
    elif info["wind"]["speed"] >= 8.0 and info["wind"]["speed"] <= 10.7:
        wind = "свежий"
    elif info["wind"]["speed"] >= 10.8 and info["wind"]["speed"] <= 13.8:
        wind = "сильный"
    elif info["wind"]["speed"] >= 13.9 and info["wind"]["speed"] <= 17.1:
        wind = "крепкий"
    elif info["wind"]["speed"] >= 17.2 and info["wind"]["speed"] <= 20.7:
        wind = "сильный"
    elif info["wind"]["speed"] >= 20.8 and info["wind"]["speed"] <= 24.4:
        wind = "шторм"
    elif info["wind"]["speed"] >= 24.5 and info["wind"]["speed"] <= 28.4:
        wind = "сильный шторм"
    elif info["wind"]["speed"] >= 28.5 and info["wind"]["speed"] <= 32.9:
        wind = "жестокий шторм"
    elif info["wind"]["speed"] >= 33.0:
        wind = "ураган"
    strToReturn += "Ветер: " + wind
    if info["wind"]["deg"] >= 0.0 and info["wind"]["deg"] < 45.0:
        direction = "северный"
    elif info["wind"]["deg"] >= 45.0 and info["wind"]["deg"] < 90.0:
        direction = "северо-восточный"
    elif info["wind"]["deg"] >= 90.0 and info["wind"]["deg"] < 135.0:
        direction = "восточный"
    elif info["wind"]["deg"] >= 135.0 and info["wind"]["deg"] < 180.0:
        direction = "юго-восточный"
    elif info["wind"]["deg"] >= 180.0 and info["wind"]["deg"] < 225.0:
        direction = "южный"
    elif info["wind"]["deg"] >= 225.0 and info["wind"]["deg"] < 270.0:
        direction = "юго-западный"
    elif info["wind"]["deg"] >= 270.0 and info["wind"]["deg"] < 315.0:
        direction = "западный"
    elif info["wind"]["deg"] >= 315.0 and info["wind"]["deg"] <= 359.0:
        direction = "северо-западный"
    strToReturn += ", " + str(info["wind"]["speed"]) + "м/с, " + direction
    all = (strToReturn, info["weather"][0]["icon"])
    return all

def getWeather(upload, time):
    response = requests.get(
        "http://api.openweathermap.org/data/2.5/forecast?q=moscow,ru&appid=819594ee113fd641ce4469f5c5f16dd5&units=metric")
    info = response.json()
    if time == "сейчас":
        strToReturn = getWeatherNow(info["list"][0])
        return strToReturn
    elif time == "сегодня":
        list = []
        temp = "/"
        strToReturn = ""
        today = info["list"][0]["dt_txt"].split()[0].split("-")[2]
        for i in info["list"]:
            if i["dt_txt"].split()[0].split("-")[2] != today:
                break
            if i["dt_txt"].split()[1].split(":")[0] == "09":
                strToReturn += "\n\nУТРО\n"
            elif i["dt_txt"].split()[1].split(":")[0] == "12":
                strToReturn += "\n\nДЕНЬ\n"
            elif i["dt_txt"].split()[1].split(":")[0] == "15":
                strToReturn += "\n\nПОЛДНИК\n"
            elif i["dt_txt"].split()[1].split(":")[0] == "18":
                strToReturn += "\n\nВЕЧЕР\n"
            elif i["dt_txt"].split()[1].split(":")[0] == "21":
                strToReturn += "\n\nНОЧЬ\n"
            elif i["dt_txt"].split()[1].split(":")[0] == "00" or i["dt_txt"].split()[1].split(":")[0] == "03" or \
                    i["dt_txt"].split()[1].split(":")[0] == "06":
                continue
            strchik = getWeatherNow(i)
            strToReturn += strchik[0]
            list.append(strchik[1])
            temp += "......." + str(round(i["main"]["temp"])) + "°С......./"
        getOnePicture(list)
        attachment = getWholePicture(upload)
        temp += strToReturn
        return (temp, attachment)
    elif time == "завтра":
        list = []
        temp = "/"
        strToReturn = ""
        today = info["list"][1]["dt_txt"].split()[0].split("-")[2]
        tommorow = ""
        if today[0] == "0":
            if today == "09":
                tommorow = str(int(today[1]) + 1)
            else:
                tommorow = "0" + str(int(today[1]) + 1)
        else:
            tommorow = str(int(today) + 1)
        j = 0
        while info["list"][j]["dt_txt"].split()[0].split("-")[2] != tommorow:
            j += 1
        while j < len(info["list"]):
            if info["list"][j]["dt_txt"].split()[0].split("-")[2] != tommorow:
                break
            if info["list"][j]["dt_txt"].split()[1].split(":")[0] == "09":
                strToReturn += "\n\nУТРО\n"
            elif info["list"][j]["dt_txt"].split()[1].split(":")[0] == "12":
                strToReturn += "\n\nДЕНЬ\n"
            elif info["list"][j]["dt_txt"].split()[1].split(":")[0] == "15":
                strToReturn += "\n\nПОЛДНИК\n"
            elif info["list"][j]["dt_txt"].split()[1].split(":")[0] == "18":
                strToReturn += "\n\nВЕЧЕР\n"
            elif info["list"][j]["dt_txt"].split()[1].split(":")[0] == "21":
                strToReturn += "\n\nНОЧЬ\n"
            elif info["list"][j]["dt_txt"].split()[1].split(":")[0] == "00" or \
                    info["list"][j]["dt_txt"].split()[1].split(":")[0] == "03" or \
                    info["list"][j]["dt_txt"].split()[1].split(":")[0] == "06":
                j += 1
                continue
            strchik = getWeatherNow(info["list"][j])
            strToReturn += strchik[0]
            list.append(strchik[1])
            temp += "......." + str(round(info["list"][j]["main"]["temp"])) + "°С......./"
            j += 1
        getOnePicture(list)
        attachment = getWholePicture(upload)
        temp += strToReturn
        return (temp, attachment)
    elif time == "на 5 дней":
        i = 0
        strToReturn = ""
        day = ""
        night = ""
        attachment = []
        stop = False
        numberOfDays = 0
        weather = "Погода в Москве с " + info["list"][0]["dt_txt"].split()[0].split("-")[2] + "." + \
                  info["list"][0]["dt_txt"].split()[0].split("-")[1] + " по "
        while i < len(info["list"]):
            today = info["list"][i]["dt_txt"].split()[0].split("-")[2]
            time = info["list"][i]["dt_txt"].split()[1].split(":")[0]
            if int(time) > 15:
                day += "/............../"
            else:
                while time != "12" and time != "15":
                    i += 1
                    time = info["list"][i]["dt_txt"].split()[1].split(":")[0]
                day += "/......." + str(round(info["list"][i]["main"]["temp"])) + "......./"
            attachment.append(info["list"][i]["weather"][0]["icon"])
            numberOfDays += 1
            while time != "21":
                i += 1
                time = info["list"][i]["dt_txt"].split()[1].split(":")[0]
            night += "/......." + str(round(info["list"][i]["main"]["temp"])) + "......./"
            if numberOfDays == 4:
                if info["list"][i]["dt_txt"].split()[0].split("-")[2][0] != "0":
                    weather += str(int(info["list"][i]["dt_txt"].split()[0].split("-")[2]) - 1) + "." + \
                               info["list"][i]["dt_txt"].split()[0].split("-")[1]
                else:
                    weather += "0" + str(int(info["list"][i]["dt_txt"].split()[0].split("-")[2]) - 1) + "." + \
                               info["list"][i]["dt_txt"].split()[0].split("-")[1]
                break
            i += 1
        getOnePicture(attachment)
        attachment = getWholePicture(upload)
        day += "ДЕНЬ\n"
        night += "НОЧЬ\n"
        day += night
        return (weather, day, attachment)
