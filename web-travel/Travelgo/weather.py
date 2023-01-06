import requests
import json
import pandas as pd
def quanbu(key,city,extensions = "base",output = "json"):
    """根据用户输入的adcode，查询目标区域当前/未来的天气情况。具体查看：https://lbs.amap.com/api/webservice/guide/api/weatherinfo"""
    url = "https://restapi.amap.com/v3/weather/weatherInfo?parameters"
    params = {
        "key":key,
        "city":city
    }
    response = requests.get(url,params=params)
    results = response.json()
    # 返回值
    return results

def weather1(key,city,extensions = "base",output = "json"):
    """根据用户输入的adcode，查询目标区域当前/未来的天气情况。具体查看：https://lbs.amap.com/api/webservice/guide/api/weatherinfo"""
    url = "https://restapi.amap.com/v3/weather/weatherInfo?parameters"
    params = {
        "key":key,
        "city":city
    }
    response = requests.get(url,params=params)
    results = response.json()['lives'][0]['weather']
    # 返回值
    return results

def temperature(key,city,extensions = "base",output = "json"):
    """根据用户输入的adcode，查询目标区域当前/未来的温度情况。具体查看：https://lbs.amap.com/api/webservice/guide/api/weatherinfo"""
    url = "https://restapi.amap.com/v3/weather/weatherInfo?parameters"
    params = {
        "key":key,
        "city":city
    }
    response = requests.get(url,params=params)
    results = response.json()['lives'][0]['temperature']
    # 返回值
    return results

def winddirection(key,city,extensions = "base",output = "json"):
    """根据用户输入的adcode，查询目标区域当前/未来的风向情况。具体查看：https://lbs.amap.com/api/webservice/guide/api/weatherinfo"""
    url = "https://restapi.amap.com/v3/weather/weatherInfo?parameters"
    params = {
        "key":key,
        "city":city
    }
    response = requests.get(url,params=params)
    results = response.json()['lives'][0]['winddirection']
    # 返回值
    return results

def windpower(key,city,extensions = "base",output = "json"):
    """根据用户输入的adcode，查询目标区域当前/未来的风力情况。具体查看：https://lbs.amap.com/api/webservice/guide/api/weatherinfo"""
    url = "https://restapi.amap.com/v3/weather/weatherInfo?parameters"
    params = {
        "key":key,
        "city":city
    }
    response = requests.get(url,params=params)
    results = response.json()['lives'][0]['windpower']
    # 返回值
    return results

def humidity(key,city,extensions = "base",output = "json"):
    """根据用户输入的adcode，查询目标区域当前/未来的湿度情况。具体查看：https://lbs.amap.com/api/webservice/guide/api/weatherinfo"""
    url = "https://restapi.amap.com/v3/weather/weatherInfo?parameters"
    params = {
        "key":key,
        "city":city
    }
    response = requests.get(url,params=params)
    results = response.json()['lives'][0]['humidity']
    # 返回值
    return results
