import requests
import json
import pandas as pd
appkey = 'ff246351bfb9f00f'
def yunshi(astroid = 1):
    """根据用户输入的星座类型，返回今日运势。具体查看：jisuapi.com/api/astro/"""
    url = "https://api.jisuapi.com/astro/fortune"
    params = {
        "astroid": astroid,
        "appkey": appkey
    }
    response = requests.get(url, params=params)
    results = response.json()['result']['year']['summary']
    return results