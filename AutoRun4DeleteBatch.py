# import pyautogui
# import time

# # 增加足夠的時間讓你移動滑鼠到目標位置
# print("請在 5 秒內將滑鼠移動到目標位置...")
# time.sleep(5)  # 等待 5 秒

# # 輸出當前滑鼠的座標位置
# current_position = pyautogui.position()
# print(f"當前滑鼠位置: {current_position}")

import pyautogui
import time

def remove_video_from_watch_later(repeat_times):
    for i in range(repeat_times):

        time.sleep(2)

        # 第一步：點擊三點選單（根據你的螢幕分辨率調整 x, y）
        pyautogui.click(x=1844, y=639)  # 替換成三點選單的位置
        time.sleep(2)  # 等待 1 秒
        
        # 第二步：移動滑鼠到 "從稍後觀看中移除"
        pyautogui.moveTo(x=1736, y=742)  # 替換成 "移除" 的選項位置
        time.sleep(1)
        
        # 第三步：點擊移除按鈕
        pyautogui.click()
        time.sleep(1)  # 等待操作完成

        # 如果列表刷新後位置變化，你可以考慮加上滾動
        # pyautogui.scroll(-500)  # 向下滾動（可根據需求調整）

# 設定要刪除的次數，假設是 10 部影片
remove_video_from_watch_later(500)
