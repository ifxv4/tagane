# -*- coding: utf-8 -*-
from selenium import webdriver
import hashlib
import schedule
import time
from time import sleep
import requests


# ハッシュ計算
def hash_it(path):
    with open(path, 'rb') as f:
        hasher = hashlib.md5()
        hasher.update(f.read())
        return hasher.hexdigest()

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = ''
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)

# 定期実行関数
def task():
    anotherhash = '8ec81e8aa5b16b6be9e079eb615d095f'
    # ディレクトリ
    directory = "./image_comparison"
    
    # chromedriverのpath
    driver = webdriver.Chrome(executable_path='C:\\chromedriver.exe')
    
    # スジボリ堂にアクセス
    driver.get('https://sujibori-do.ocnk.net/product/2453?')

    # ウインドウ最大化
    driver.maximize_window()

    # 一応3秒待機
    time.sleep(3)

    # スクショする
    driver.save_screenshot('image_comparison/actual_img.png')
    
    # スクリーンショット
    actual_img = "{}/{}".format(directory, "actual_img.png")
    # 期待値
    expected_img = "{}/{}".format(directory, "expected_img.png")
     
    # 元画像と比較する
    actual_img_hash = hash_it(actual_img)
    expected_img_hash = hash_it(expected_img)

    # 一致
    if actual_img_hash == expected_img_hash:
        print("Images match. {} and {}".format(
            actual_img_hash, expected_img_hash))
    # 一致
    elif actual_img_hash == anotherhash:
        print("Images match.")   
    # 一致しない場合Lineに通知を送る
    else:
        print("Images do not match. {} and {}".format(
            actual_img_hash, expected_img_hash))
        send_line_notify('発売中かも！リンクから確認[https://sujibori-do.ocnk.net/product/2453?]')

    #比較して同じであれば閉じる
    driver.quit()

#02 スケジュール登録
schedule.every(30).minutes.do(task)

#03 イベント実行
while True:
    schedule.run_pending()
    sleep(1)
