import pyautogui
import time
import json
from old_info import kols

# 摁chrome浏览器
link_num = 137
link_num_end = len(kols)
link_num_str = ""
action_list = [
    {
        "name":"摁chrome浏览器",
        "x":618,
        "y":800 - 25,
        "action":"move_and_click",
        "sleep": 1
    },
    {
        "name":"摁pgy tab",
        "x":120,
        "y":800 - 750,
        "action":"move_and_click",
        "sleep": 1
    },
    {
        "name":"摁地址栏",
        "x":400,
        "y":800 - 715,
        "action":"move_and_click",
        "sleep": 1
    },
    {
        "name":"输入网址",
        "x":400,
        "y":800 - 715,
        "action":"input_link",
        "sleep": 15
    },
    {
        "name":"点击userId",
        "x":673,
        "y":800 - 635,
        "action":"move_and_click",
        "sleep": 1
    },
    {
        "name":"输入userId",
        "x":673,
        "y":800 - 635,
        "action":"input_link_userid",
        "sleep": 2
    },
    
    {
        "name":"点击network内容",
        "x":707,
        "y":800 - 483,
        # "x":721,
        # "y":800 - 441,
        "action":"move_and_click",
        "sleep": 1
    },
    {
        "name":"点击response",
        "x":1112,
        "y":800 - 471,
        "action":"move_and_click",
        "sleep": 1
    },
    {
        "name":"复制response",
        "x":1083,
        "y":800 - 453,
        "action":"move_and_click_and_copy",
        "sleep": 1
    },
    {
        "name":"摁qsh page pgy tab",
        "x":592,
        "y":800 - 751,
        "action":"move_and_click",
        "sleep": 1
    },
    {
        "name":"摁输入框",
        "x":187,
        "y":800 - 606,
        "action":"move_and_click_and_paste",
        "sleep": 2
    },
    {
        "name":"摁输入框 提交",
        "x":230,
        "y":800 - 522,
        "action":"move_and_click",
        "sleep": 1
    },
    {
        "name":"更新link num",
        "x":673,
        "y":800 - 635,
        "action":"update_link_num",
        "sleep": 0
    },
]
do_one = True
def do_one():
    global do_one
    global link_num
    global link_num_str
    global link_num_end
    for action in action_list:
        action_now = action.get("action",None)
        if action_now in ["move_and_click"]:
            pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
            pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
        elif action_now in ["input_link"]:
            link_num_str = kols[link_num]["userId"]
            pyautogui.typewrite("https://pgy.xiaohongshu.com/solar/advertiser/kol/%s"%link_num_str)
            pyautogui.press('enter')
        elif action_now in ["input_link_userid"]:
            pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
            pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
            pyautogui.hotkey("command", "a")
            link_num_str = kols[link_num]["userId"]
            pyautogui.typewrite(link_num_str)
            pyautogui.press('enter')
        elif action_now in ["move_and_click_and_copy"]:
            pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
            pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
            pyautogui.hotkey("command", "a")
            pyautogui.hotkey("command", "c")
        elif action_now in ["move_and_click_and_paste"]:
            pyautogui.moveTo(x=action.get("x",None), y=action.get("y",None),duration=0, tween=pyautogui.linear)
            time.sleep(2)
            pyautogui.click(x=action.get("x",None), y=action.get("y",None),clicks=1, button='left')
            pyautogui.hotkey("command", "v")
        elif action_now in ["update_link_num"]:
            link_num = link_num + 1
        time.sleep(action.get("sleep",0))
    if link_num > link_num_end:
        do_one = False
while do_one:
    do_one()


