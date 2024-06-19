#/usr/bin/python3
# https://api-docs.fullhunt.io/#introduction

import time
import requests
from tabulate import tabulate

def fullhunt_apikey_verify(files):
    print('\n' + '*'*30 + "key验证" + '*'*30 + '\n')
    table = [["API_KEY"]]
    
    # 构建 API 请求的 URL
    API_URL = f"https://fullhunt.io/api/v1/auth/status"
    for key in open(files):
        API_key=key.strip()
        headers_format = {
            "X-API-KEY": f"{API_key}",
            "Accept": "application/json"  # 指定响应数据格式为 JSON
        }
        res = requests.get(API_URL, headers=headers_format)
        if res.status_code == 200:
            results = res.json()
            results_data = API_key + ',' + str(results['user']['email']) + ',' + str(results['user']['plan']) + ',' + str(results['user_credits']['credits_usage']) + ',' + str(results['user_credits']['max_results_per_request']) + ',' + str(results['user_credits']['remaining_credits']) + ',' + str(results['user_credits']['total_credits_per_month'])
            print(results_data.split(","))
            table.append(results_data.split(","))
        else:
            print(API_key + ', Error!')
        time.sleep(2)

    print('\n' + '*'*30 + "注释信息" + '*'*30 + '\n')
    Notes_json = {
        "email": "邮箱",
        "plan": "计划",
        "credits_usage": "积分使用量",
        "max_results_per_request": "每个请求的最大结果数",
        "remaining_credits": "剩余积分",
        "total_credits_per_month": "每月总积分"
    }
    # 将键写入到table中
    for key, value in Notes_json.items():
        table[0].append(key)
        print(f"{key}: {value}")
    print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    print(tabulate(table, headers='firstrow'))
