import time
import pyautogui

# 此程式還有待改進
# region direction
TOP = 1
DOWN = 2
LEFT = 3
RIGHT = 4
LEFT_TOP = 5


# endregion

def position_by_direction(direction):
    if direction == LEFT_TOP:
        return 700, 350


# this will print width and height of screen
time.sleep(2)
# print(pyautogui.size())  # width=1920, height=1080

images = [r'images\eigth_wood.png',
          r'images\eigth_iron.png',
          r'images\eigth_stone.png',
          r'images\eigth_food.png',
          r'images\eigth_gold.png']
is_target_found = False
while True:
    pyautogui.moveTo(960, 540)
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(position_by_direction(LEFT_TOP)[0], position_by_direction(LEFT_TOP)[1])  # 左上
    for image in images:
        target_location = pyautogui.locateOnScreen(image,
                                                   confidence=0.7)
        if target_location is not None:
            pyautogui.moveTo(target_location.left, target_location.top)
            pyautogui.click()
            if not pyautogui.locateOnScreen(r'images\mail_icon.png',
                                            confidence=0.7):
                is_target_found = True
            break
    if is_target_found:
        break
    time.sleep(2)
