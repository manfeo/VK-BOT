from vk_api.keyboard import VkKeyboard, VkKeyboardColor
def get_weather_keyboard():
    keyboardForWeather = VkKeyboard(one_time=False)
    keyboardForWeather.add_button("сейчас", color=VkKeyboardColor.PRIMARY)
    keyboardForWeather.add_button("сегодня", color=VkKeyboardColor.POSITIVE)
    keyboardForWeather.add_button("завтра", color=VkKeyboardColor.POSITIVE)
    keyboardForWeather.add_line()
    keyboardForWeather.add_button("на 5 дней", color=VkKeyboardColor.POSITIVE)
    return keyboardForWeather