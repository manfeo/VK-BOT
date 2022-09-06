from vk_api.keyboard import VkKeyboard, VkKeyboardColor
def get_teacher_keyboard():
    keyboardTeach = VkKeyboard(one_time=False)
    keyboardTeach.add_button('на эту неделю', color=VkKeyboardColor.PRIMARY)
    keyboardTeach.add_button('на следующую неделю', color=VkKeyboardColor.PRIMARY)
    return keyboardTeach