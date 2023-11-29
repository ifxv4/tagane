# -*- coding: utf-8 -*-
from selenium import webdriver
import hashlib
import schedule
import time
from time import sleep
import requests

def send_line_notify(notification_message):
    """
    LINEに通知する
    """
    line_notify_token = ''
    line_notify_api = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {line_notify_token}'}
    data = {'message': f'message: {notification_message}'}
    requests.post(line_notify_api, headers = headers, data = data)
# ハッシュ計算
send_line_notify('test')