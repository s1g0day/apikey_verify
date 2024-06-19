#/usr/bin/python3
# https://docs.securitytrails.com/reference/usage


import time
import requests
from tabulate import tabulate

def securitytrails_apikey_verify(files):
    print('\n' + '*'*30 + "key验证" + '*'*30 + '\n')
    table = [["API_KEY"]]
    
    # 构建 API 请求的 URL
    API_URL = 'https://api.securitytrails.com/v1/account/usage'
    for key in open(files):
        API_key=key.strip()
        headers = {
            "accept": "application/json",
            "APIKEY": API_key
        }
        res = requests.get(API_URL, headers=headers)
        if res.status_code == 200:
            results = res.json()
            results_data = API_key + ',' + str(results["current_monthly_usage"]) + ',' + str(results["allowed_monthly_usage"]) + ',' + ''
            print(results_data.split(","))
            table.append(results_data.split(","))
        elif res.status_code == 429:
            results = res.json()
            results_data = API_key + ',' + "0" + ',' + "0" + ',' + "本月已用完"
            print(results_data.split(","))
            table.append(results_data.split(","))
        else:
            print(API_key + ', Error!')
        time.sleep(5)
    
    print('\n' + '*'*30 + "注释信息" + '*'*30 + '\n')
    Notes_json = {
        "current_monthly_usage": "每月已使用",
        "allowed_monthly_usage": "每月剩余",
        "message": "消息",
    }
    # 将键写入到table中
    for key, value in Notes_json.items():
        table[0].append(key)
        print(f"{key}: {value}")
    print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    print(tabulate(table, headers='firstrow'))

