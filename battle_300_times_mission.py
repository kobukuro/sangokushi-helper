import pyautogui
import time
from datetime import datetime
import easyocr

# region scroll
# time.sleep(1)
# pyautogui.moveTo(1009, 551)
# pyautogui.mouseDown(button='left')
# pyautogui.moveTo(1005, 193)
# pyautogui.mouseUp(button='left')
# time.sleep(1)
# pyautogui.moveTo(1009, 551)
# pyautogui.click()
# endregion

# 記得午夜12點後執行, 因為會發獎勵, 會擋住畫面
# 這個是為了解交戰300次任務的程式
# 看滑鼠動態座標
# pyautogui.displayMousePosition()
# 共三個隊伍, 一開始把武將全部清空, 然後都要設定為騎兵, 剛開始要先點主城座標
# 記得輸入法為英數
# 敵人座標
ENEMY_X, ENEMY_Y = 1194, 601
# 主城座標
CASTLE_X, CASTLE_Y = 958, 495
# 填兵力數字的座標
SOLDIERS_NUMBER_X, SOLDIERS_NUMBER_Y = 786, 676
# 50分鐘為3000(等武將回滿體力15需要45分鐘, 保險起見用50分鐘)
WAIT_SECONDS = 3000  # 15分鐘:900(重傷恢復所需時間)
IS_CLICK_DAILY = False  # 是否為午夜前開始執行，是的話，必須把每日獎勵點掉


def program_without_ocr():
    # print(type(datetime.now()))
    # print((datetime.now() + timedelta(minutes=30)).hour)
    time.sleep(2)
    if IS_CLICK_DAILY:
        time_now = datetime.now()
        while True:
            time.sleep(1)
            if time_now.hour == 0 and time_now.minute == 10:  # 午夜零點10分
                break
            time_now = datetime.now()
        join_army_position = pyautogui.locateCenterOnScreen('images\\daily_award_confirm.png')
        pyautogui.moveTo(join_army_position.x, join_army_position.y)
        pyautogui.click()

    time.sleep(1)

    # 先自己進入城池頁面
    pyautogui.moveTo(CASTLE_X, CASTLE_Y)
    pyautogui.click()
    time.sleep(1)
    edit_army_positions = list(pyautogui.locateAllOnScreen('images\\edit_army.png'))
    len_edit_army_positions = len(edit_army_positions)
    while len_edit_army_positions > 0:
        pyautogui.moveTo(edit_army_positions[0].left, edit_army_positions[0].top)
        pyautogui.click()
        time.sleep(1)
        plus_buttons = list(pyautogui.locateAllOnScreen('images\\plus_btn.png'))
        len_plus_buttons = len(plus_buttons)
        if len_plus_buttons > 0:
            pyautogui.moveTo(plus_buttons[0].left, plus_buttons[0].top)
            pyautogui.click()
        time.sleep(1)
        join_army_position = pyautogui.locateCenterOnScreen('images\\join_army_btn.png')
        pyautogui.moveTo(join_army_position.x, join_army_position.y)
        pyautogui.click()
        time.sleep(1)
        pyautogui.moveTo(SOLDIERS_NUMBER_X, SOLDIERS_NUMBER_Y)
        pyautogui.click()
        time.sleep(1)
        pyautogui.press('backspace')
        time.sleep(1)
        pyautogui.typewrite('1')
        time.sleep(1)
        join_army_position = pyautogui.locateCenterOnScreen('images\\confirm_to_allocate_soldiers.png')
        pyautogui.moveTo(join_army_position.x, join_army_position.y)
        pyautogui.click()
        time.sleep(1)
        back_btn = pyautogui.locateCenterOnScreen('images\\inner_back_btn.png')
        pyautogui.moveTo(back_btn.x, back_btn.y)
        pyautogui.click()
        time.sleep(1)
        edit_army_positions = list(pyautogui.locateAllOnScreen('images\\edit_army.png'))
        len_edit_army_positions = len(edit_army_positions)
    # region 都已上陣的情況
    # endregion
    time.sleep(1)
    back_btn = pyautogui.locateCenterOnScreen('images\\outer_back_btn.png')
    pyautogui.moveTo(back_btn.x, back_btn.y)
    pyautogui.click()
    time.sleep(1)
    # click enemy
    pyautogui.moveTo(ENEMY_X, ENEMY_Y)
    pyautogui.click()
    time.sleep(1)
    back_btn = pyautogui.locateCenterOnScreen('images\\move_army_btn.png')
    pyautogui.moveTo(back_btn.x, back_btn.y)
    pyautogui.click()
    time.sleep(1)
    wait_icons = list(pyautogui.locateAllOnScreen('images\\wait_icon.png'))
    len_wait_icons = len(wait_icons)
    while len_wait_icons > 0:
        pyautogui.moveTo(wait_icons[0].left, wait_icons[0].top)
        pyautogui.click()
        time.sleep(1)
        back_btn = pyautogui.locateCenterOnScreen('images\\move_army_final_btn.png')
        pyautogui.moveTo(back_btn.x, back_btn.y)
        pyautogui.click()
        # click enemy
        pyautogui.moveTo(ENEMY_X, ENEMY_Y)
        pyautogui.click()
        time.sleep(1)
        back_btn = pyautogui.locateCenterOnScreen('images\\move_army_btn.png')
        pyautogui.moveTo(back_btn.x, back_btn.y)
        pyautogui.click()
        time.sleep(1)
        wait_icons = list(pyautogui.locateAllOnScreen('images\\wait_icon.png'))
        len_wait_icons = len(wait_icons)
    move_army_back_btn = pyautogui.locateCenterOnScreen('images\\move_army_back_btn.png')
    pyautogui.moveTo(move_army_back_btn.x, move_army_back_btn.y)
    pyautogui.click()
    now = datetime.now()
    print(now.strftime("%H:%M:%S"))
    while True:
        time.sleep(WAIT_SECONDS)
        now = datetime.now()
        print(now.strftime("%H:%M:%S"))

        pyautogui.moveTo(CASTLE_X, CASTLE_Y)
        pyautogui.click()
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        wait_icons = list(pyautogui.locateAllOnScreen('images\\horse_rider.png'))
        for i in range(len(wait_icons)):
            wait_icons = list(pyautogui.locateAllOnScreen('images\\horse_rider.png'))
            pyautogui.moveTo(wait_icons[i].left, wait_icons[i].top)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(SOLDIERS_NUMBER_X, SOLDIERS_NUMBER_Y)
            pyautogui.click()
            time.sleep(1)
            pyautogui.press('backspace')
            time.sleep(1)
            pyautogui.typewrite('1')
            time.sleep(1)
            join_army_position = pyautogui.locateCenterOnScreen('images\\confirm_to_allocate_soldiers.png')
            pyautogui.moveTo(join_army_position.x, join_army_position.y)
            pyautogui.click()
            time.sleep(1)
            back_btn = pyautogui.locateCenterOnScreen('images\\inner_back_btn.png')
            pyautogui.moveTo(back_btn.x, back_btn.y)
            pyautogui.click()
            time.sleep(1)
        back_btn = pyautogui.locateCenterOnScreen('images\\outer_back_btn.png')
        pyautogui.moveTo(back_btn.x, back_btn.y)
        pyautogui.click()
        time.sleep(1)
        # click enemy
        pyautogui.moveTo(ENEMY_X, ENEMY_Y)
        pyautogui.click()
        time.sleep(1)
        back_btn = pyautogui.locateCenterOnScreen('images\\move_army_btn.png')
        pyautogui.moveTo(back_btn.x, back_btn.y)
        pyautogui.click()
        time.sleep(1)
        wait_icons = list(pyautogui.locateAllOnScreen('images\\wait_icon.png'))
        len_wait_icons = len(wait_icons)
        while len_wait_icons > 0:
            pyautogui.moveTo(wait_icons[0].left, wait_icons[0].top)
            pyautogui.click()
            time.sleep(1)
            back_btn = pyautogui.locateCenterOnScreen('images\\move_army_final_btn.png')
            pyautogui.moveTo(back_btn.x, back_btn.y)
            pyautogui.click()
            # click enemy
            pyautogui.moveTo(ENEMY_X, ENEMY_Y)
            pyautogui.click()
            time.sleep(1)
            back_btn = pyautogui.locateCenterOnScreen('images\\move_army_btn.png')
            pyautogui.moveTo(back_btn.x, back_btn.y)
            pyautogui.click()
            time.sleep(1)
            wait_icons = list(pyautogui.locateAllOnScreen('images\\wait_icon.png'))
            len_wait_icons = len(wait_icons)
        move_army_back_btn = pyautogui.locateCenterOnScreen('images\\move_army_back_btn.png')
        pyautogui.moveTo(move_army_back_btn.x, move_army_back_btn.y)
        pyautogui.click()


def program_with_ocr():
    # import torch
    #
    # print(torch.cuda.is_available())
    # # 先點部隊隊伍
    # time.sleep(1)
    # # region 進入主城頁面
    # pyautogui.click(CASTLE_X, CASTLE_Y)
    # time.sleep(1)
    # pyautogui.click(CASTLE_X, CASTLE_Y)
    # # endregion
    now = time.time()
    reader = easyocr.Reader(['ch_tra'], gpu=True)
    # image = pyautogui.screenshot(region=(429, 742, 475-429, 763-742))
    # image.save('1.jpg')
    result = reader.readtext(r'images\\example-1.jpg')
    # result = reader.readtext('1.jpg')
    print(result)
    later = time.time()
    difference = int(later - now)
    print(difference)


if __name__ == '__main__':
    program_without_ocr()
