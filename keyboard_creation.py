from vk_api.keyboard import VkKeyboard, VkKeyboardColor
def createKeyboard(dictionary):
    keyboardOfTeachers = VkKeyboard(one_time=True)
    for j in dictionary:
        keyboardOfTeachers.add_button(j, color=VkKeyboardColor.PRIMARY)
        break
    counter = 0
    for i in dictionary:
        if counter != 0:
            keyboardOfTeachers.add_line()
            keyboardOfTeachers.add_button(i, color=VkKeyboardColor.PRIMARY)
        else:
            counter += 1
            continue
    return keyboardOfTeachers