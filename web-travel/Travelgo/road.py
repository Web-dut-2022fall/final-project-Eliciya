import requests
# 下面注释是为了进入路径不变灰
# noinspection PyUnresolvedReferences
import json
import pandas as pd

# 服务于高德三个路径规划，先将用户的地址换成代码
def geocode(key, address, city=None, batch=None, ) -> str:
    """获取高德API的地理编码
温馨提示：key是指高德api的密钥，请先去注册；
          address是指结构化地址，具体请查看：https://lbs.amap.com/api/webservice/guide/api/georegeo
    """
    url = "https://restapi.amap.com/v3/geocode/geo?parameters"
    params = {
        "key": key,
        "address": address,
        "city": city,
        "batch": batch

    }
    response = requests.get(url, params=params)
    results = response.json()['geocodes'][0]['location']
    return results

def walking(key, origin, destination) -> str:
    """获取高德API的步行路径规划
温馨提示：key是指高德api的密钥，请先去注册；
          origin是指起始地点，destination是目的地，
          具体请查看：https://lbs.amap.com/api/webservice/guide/api/direction
    """
    url = 'https://restapi.amap.com/v3/direction/walking?parameters'
    params = {
        "key": key,
        "origin": origin,
        "destination": destination,

    }
    response = requests.get(url, params=params)
    results = pd.json_normalize(response.json()['route']['paths'][0]['steps'])['instruction'].tolist()
    return results

def car(key,origin,destination,originid = None,destinationid=None,origintype = None,destinationtype = None,strategy = 10,waypoints = None,avoidpolygons = None,avoidroad = None,province = None,number = None,cartype = 0,ferry = 0,adaggregation = 'true',nosteps = 0,sig = None,output = 'json',callback = None,extensions = 'base')->str:
    """获取高德API的驾车路径规划
温馨提示：key是指高德api的密钥，请先去注册；
          origin是指起始地点，destination是目的地
          具体请查看：https://lbs.amap.com/api/webservice/guide/api/direction
    """
    url = 'https://restapi.amap.com/v3/direction/driving?parameters'
    params = {'key':key,
          'origin':origin,
          'destination':destination,
          }
    response = requests.get(url,params = params)
    results = pd.json_normalize(response.json()['route']['paths'][0]['steps'])['instruction'].tolist()
    return results

def bike(key,origin,destination)->str:
    """获取高德API的骑行路径规划
温馨提示：key是指高德api的密钥，请先去注册；
          origin是指起始地点，destination是目的地
          具体请查看：https://lbs.amap.com/api/webservice/guide/api/direction
    """
    url = 'https://restapi.amap.com/v4/direction/bicycling?parameters'
    params = {'key':key,
          'origin':origin,
          'destination':destination,
          }
    response = requests.get(url,params = params)
    results = pd.json_normalize(response.json()['data']['paths'][0]['steps'])['instruction'].tolist()
    return results