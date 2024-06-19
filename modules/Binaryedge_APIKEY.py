#/usr/bin/python3
# https://docs.binaryedge.io/api-v2/

import time
import requests
from tabulate import tabulate

def binaryedge_apikey_verify(files):
    print('\n' + '*'*30 + "key验证" + '*'*30 + '\n')
    table = [["API_KEY"]]
    
    # 构建 API 请求的 URL
    API_URL = 'https://api.binaryedge.io/v2/user/subscription'
    for key in open(files):
        API_key=key.strip()
        headers = {
            'x-key': API_key,
        }
        res = requests.get(API_URL, headers=headers)
        if res.status_code == 200:
            results = res.json()
            results_data = API_key + ',' + str(results["subscription"]["name"]) + ',' + str(results["end_date"]) + ',' + str(results["requests_left"]) + ',' + str(results["requests_plan"]) 
            print(results_data.split(","))
            table.append(results_data.split(","))
        else:
            print(API_key + ', Error!')
        time.sleep(2)
    
    print('\n' + '*'*30 + "注释信息" + '*'*30 + '\n')
    Notes_json = {
        "subscription": "订阅权限",
        "end_date": "有效时间(每月自动更新)",
        "requests_left": "每月剩余的请求",
        "requests_plan": "每月请求额度"
    }
    # 将键写入到table中
    for key, value in Notes_json.items():
        table[0].append(key)
        print(f"{key}: {value}")
    print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    print(tabulate(table, headers='firstrow'))

