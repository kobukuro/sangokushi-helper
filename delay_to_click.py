import pyautogui
from datetime import datetime, timedelta

# 現在時間 - 等多少時間後click - 軍隊行軍時間 - 到達攻城時間

# 攻城時間 時 分 秒
des_hour = 22  # TODO need to modify
des_min = 0  # TODO need to modify
des_sec = 0  # TODO need to modify

# 軍隊行軍時間(單位:秒)
army_need_secs = 24  # TODO need to modify

start = datetime.now()
print(f'program start time : {start}')
total_secs = (timedelta(hours=24) - (
        start - start.replace(hour=des_hour, minute=des_min, second=des_sec))).total_seconds() % (
                     24 * 3600)
total_secs = int(total_secs)
print(f'need to wait seconds : {total_secs}')

need_to_wait_secs = total_secs - army_need_secs

now = datetime.now()
elapsed = (now - start).seconds
# print((now - start).seconds)

while elapsed < need_to_wait_secs:
    now = datetime.now()
    elapsed = (now - start).seconds
print(f'click time : {datetime.now()}')
pyautogui.click()  # click
