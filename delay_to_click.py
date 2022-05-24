import pyautogui
from datetime import datetime, timedelta

# 現在時間 - 等多少時間後click - 軍隊行軍時間 - 到達攻城時間

# 實驗結果:以下設定要設定在實際攻城時間-1秒, 戰報的時間會剛好
# 例如攻城時間為晚上九點, 以下變數要設定des_hour=20, des_min=59, des_sec=59

# 攻城時間 時 分 秒
des_hour = 22  # TODO need to modify
des_min = 28  # TODO need to modify
des_sec = 59  # TODO need to modify

# 軍隊行軍時間(單位:秒)
army_need_secs = 30  # TODO need to modify

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
