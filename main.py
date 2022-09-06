import vk_api
from vk_api import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import json
import re
import requests
from bs4 import BeautifulSoup
import xlrd
import PIL.Image as Image
import numpy as np
import matplotlib.pyplot as plt
from vk_token import tok_name
from schedule_keyboard import get_schedule_keyboard
from empty_keyboard import get_empty_keyboard
from get_schedule_for_group_tomorrow_today import getScheduleForDay
from get_schedule_for_group_for_week import getScheduleForWeek
from current_week import get_current_week
from constants import allMonths,days
from get_schedule_for_day_for_group import getScheduleDay
from find_teacher import findTeacher
from keyboard_creation import createKeyboard
from teacher_keyboard import get_teacher_keyboard
from teacher_schedule import getScheduleForTeacher
from get_weather import getWeather
from weather_keyboard import get_weather_keyboard
from get_picture import getPictures, getOnePicture, getWholePicture
from corona import getKorona
def main():
    vk_session = vk_api.VkApi(token=tok_name)
    vk = vk_session.get_api()
    longpoll = VkLongPoll(vk_session)
    pattern = re.compile("[А-Я]{4}(\-[0-9][0-9]){2}")
    group = ""
    upload = VkUpload(vk_session)
    second_group = ""
    teacher = ""
    flag = False
    second_flag = False
    flag_teacher = False
    courses = []
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                if second_flag and event.text != "на сегодня" and event.text != "на завтра" and event.text != "на эту неделю" and event.text != "на следующую неделю" and event.text != "какая неделя?" and event.text != "какая группа?":
                    texts = event.text.split()
                    for i in texts:
                        if re.fullmatch(pattern, i) and len(texts) != 1:
                            flag = True
                    if not flag:
                        group = second_group
                        second_flag = False
                if event.text.split()[0] != "найти" and not re.fullmatch("[А-Я][а-я]+\s+[А-Я]\.[А-Я]\.",
                                                                         event.text) and event.text != "на сегодня" and event.text != "на завтра" and event.text != "на эту неделю" and event.text != "на следующую неделю":
                    flag_teacher = False
                if re.fullmatch(pattern, event.text):
                    group = event.text
                    vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                     message="Я запомнил, что ты из группы {}".format(group))
                else:
                    text = event.text.lower()
                    if text == 'привет' or text == "начать":
                        keyboard = get_empty_keyboard()
                        """
                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                         message="Привет, " + vk.users.get(user_id=event.user_id)[0][
                                             'first_name'] + "\n☘Введи номер группы, чтобы я её запомнил\n☘Напиши \"Бот\" чтобы вывести "
                                                             "расписание на выбранную группу\n☘Напиши \"Бот <день недели>\" чтобы найти "
                                                             "расписание группы на определённый день\n☘Напиши \"Бот <номер группы>\" чтобы "
                                                             "найти расписание для определённой группы\n☘Напиши \"Бот <день недели> <номер "
                                                             "группы>\" чтобы найти расписание выбранной группы на определённый день недели\n☘"
                                                             "Напиши \"Погода\" чтобы узнать о погоде\n☘Напиши \"Найти <фамилия преподавателя> "
                                                             "чтобы найти расписание преподавателя\n☘Напиши \"Корона\" чтобы узнать о состоянии "
                                                             "короны на текущий момент в Москве\n☘Напиши \"Корона <Область>\" чтобы узнать о состоянии "
                                                             "короны на текущий момент в <Область>", keyboard=keyboard)
                        """
                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                         message="Привет, Олег" + "\n☘Введи номер группы, чтобы я её запомнил\n☘Напиши \"Бот\" чтобы вывести "
                                                             "расписание на выбранную группу\n☘Напиши \"Бот <день недели>\" чтобы найти "
                                                             "расписание группы на определённый день\n☘Напиши \"Бот <номер группы>\" чтобы "
                                                             "найти расписание для определённой группы\n☘Напиши \"Бот <день недели> <номер "
                                                             "группы>\" чтобы найти расписание выбранной группы на определённый день недели\n☘"
                                                             "Напиши \"Погода\" чтобы узнать о погоде\n☘Напиши \"Найти <фамилия преподавателя> "
                                                             "чтобы найти расписание преподавателя\n☘Напиши \"Корона\" чтобы узнать о состоянии "
                                                             "короны на текущий момент в Москве\n☘Напиши \"Корона <Область>\" чтобы узнать о состоянии "
                                                             "короны на текущий момент в <Область>", keyboard=keyboard)
                        text = ""
                    elif text == 'бот':
                        keyboard = get_schedule_keyboard()
                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                         message="Показать расписание ...", keyboard=keyboard.get_keyboard())
                    elif text == "на сегодня" or text == "на завтра":
                        if group == "":
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                             message="Сначала напиши из какой ты группы!")
                        else:
                            messageToSend = getScheduleForDay(group, text)
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                             message=messageToSend)
                    elif text == "на эту неделю" or text == "на следующую неделю":
                        if flag_teacher == False:
                            if group == "":
                                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                                 message="Сначала напиши из какой ты группы!")
                            else:
                                messageToSend = getScheduleForWeek(text, group)
                                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                                 message=messageToSend)
                        else:
                            raspisanie = getScheduleForTeacher(teacher, courses, text)
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=raspisanie)
                    elif text == "какая неделя?":
                        messageToSend = "Сейчас идёт " + str(get_current_week()) + " неделя"
                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=messageToSend)
                    elif text == "какая группа?":
                        if group == "":
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                             message="Сначала напишите из какой ты группы!")
                        else:
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                             message="Показываю расписание группы " + group)
                    elif text == "пока":
                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message="Пока!✋",
                                         keyboard=get_empty_keyboard())
                    elif text.split()[0] == "бот" and text.split()[1] in days and len(text.split()) == 2:
                        if group != "":
                            messageToSend = getScheduleDay(text.split()[1], group)
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=messageToSend)
                        else:
                            messageToSend = "Сначала напиши из какой ты группы!"
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=messageToSend)
                    elif text.split()[0] == "бот" and re.fullmatch(pattern, text.split()[1].upper()):
                        second_flag = True
                        temp = group
                        group = text.split()[1].upper()
                        second_group = temp
                        keyboard = get_schedule_keyboard()
                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                         message="Показать расписание группы " + group + "...",
                                         keyboard=keyboard.get_keyboard())
                    elif text.split()[0] == "бот" and text.split()[1] in days and re.fullmatch(pattern,
                                                                                               text.split()[2].upper()):
                        messageToSend = getScheduleDay(text.split()[1], text.split()[2].upper())
                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=messageToSend)
                    elif text == "погода":
                        keyboardForWeather = get_weather_keyboard()
                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                         message="Показать погоду в Москве", keyboard=keyboardForWeather.get_keyboard())
                    elif text == "сейчас":
                        all = getWeather(upload, text)
                        attachments = getPictures(upload, all[1])
                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message="Погода в Москве",
                                         attachment=','.join(attachments))
                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=all[0])
                    elif text == "сегодня" or text == "завтра" or text == "на 5 дней":
                        allAttachments = getWeather(upload, text)
                        if len(allAttachments) == 2:
                            if text == "сегодня":
                                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                                 message="Погода в Москве сегодня",
                                                 attachment=",".join(allAttachments[1]))
                            elif text == "завтра":
                                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                                 message="Погода в Москве на завтра",
                                                 attachment=",".join(allAttachments[1]))
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                             message=allAttachments[0])
                        elif len(allAttachments) == 3:
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                             message=allAttachments[0], attachment=",".join(allAttachments[2]))
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                             message=allAttachments[1])
                    elif len(text.split()) >= 2 and (
                            text.split()[0] == "найти" or re.fullmatch("[А-Я][а-я]+\s+[А-Я]\.[А-Я]\.",
                                                                       text.split()[0].title() + " " + text.split()[
                                                                           1].upper())):
                        if "найти" in text:
                            flag_teacher = True
                            dictionary = findTeacher(text.split()[1].title())
                            if len(dictionary) > 1:
                                keyboardForTeachers = createKeyboard(dictionary)
                                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                                 message="Найденные учителя...",
                                                 keyboard=keyboardForTeachers.get_keyboard())
                            elif len(dictionary) == 1:
                                teacher = list(dictionary)[0]
                                keyboardForTeachers = get_teacher_keyboard()
                                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                                 message="Показать расписание преподавателя " + teacher + "...",
                                                 keyboard=keyboardForTeachers.get_keyboard())
                            else:
                                keyboard = get_empty_keyboard()
                                vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                                 message="Преподаватель не найден", keyboard=keyboard)
                        else:
                            chosed = text.split()[0].title() + " " + text.split()[1].upper()
                            keyboardForTeachers = get_teacher_keyboard()
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                             message="Показать расписание преподавателя " + teacher + "...",
                                             keyboard=keyboardForTeachers.get_keyboard())
                    elif "корона" in text:
                        attach = getKorona(text, upload)
                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=attach,
                                         keyboard=get_empty_keyboard())
                        """
                        if len(attach) > 2:
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=attach,
                                             keyboard=get_empty_keyboard())
                        elif attach == "Такого региона не найдено":
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=attach)
                        else:
                            vk.messages.send(user_id=event.user_id, random_id=get_random_id(), message=attach[0],
                                             attachment=",".join(attach[1]), keyboard=get_empty_keyboard())
                            """
                    else:
                        vk.messages.send(user_id=event.user_id, random_id=get_random_id(),
                                         message="Я не понимаю, что ты написал...")


if __name__ == "__main__":
    main()