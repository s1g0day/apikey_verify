#/usr/bin/python3
# https://search.censys.io/api

import time
import requests
from tabulate import tabulate

def censys_apikey_verify(files):
    print('\n' + '*'*30 + "key验证" + '*'*30 + '\n')
    table = [["UID/SECRET"]]
    
    # 构建 API 请求的 URL
    API_URL = "https://search.censys.io/api/v1/account"

    for key in open(files):
        if ":" in key:
            UID, SECRET = key.strip().split(":")
        else:
            UID, SECRET = key.strip().split("|")
            
        res = requests.get(API_URL, auth= (UID, SECRET))
        if res.status_code == 200:
            results = res.json()
            results_data = UID + ':' + SECRET + ',' + str(results['email']) + ',' + str(results['quota']['used']) + ',' + str(results['quota']['allowance']) + ',' + str(results['quota']['resets_at'])
            print(results_data.split(","))
            table.append(results_data.split(","))
        else:
            print(UID + ', Error!')
        time.sleep(2)
    
    print('\n' + '*'*30 + "注释信息" + '*'*30 + '\n')
    Notes_json = {
        "email": "邮箱",
        "used": "使用次数",
        "allowance": "剩余额度",
        "resets_at": "重置时间"
    }
    # 将键写入到table中
    for key, value in Notes_json.items():
        table[0].append(key)
        print(f"{key}: {value}")
    print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    print(tabulate(table, headers='firstrow'))

