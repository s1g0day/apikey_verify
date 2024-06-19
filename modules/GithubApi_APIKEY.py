#/usr/bin/python3
# https://docs.github.com/en/rest/quickstart
# 90天有效期，需手动更新

import time
import datetime
import requests
from tabulate import tabulate

def convert_unix_timestamp(timestamp):
    dt = datetime.datetime.fromtimestamp(timestamp)
    formatted_date = dt.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date

def github_apikey_verify(files):
    print('\n' + '*'*30 + "key验证" + '*'*30 + '\n')
    table = [["API_key"]]

    # 构建 API 请求的 URL
    API_URL = f"https://api.github.com/rate_limit"
    for key in open(files):
        API_key=key.strip()
        headers_format = {
            "Authorization": f"Bearer {API_key}",
            "Accept": "application/json"  # 指定响应数据格式为 JSON
        }
        res = requests.get(API_URL, headers=headers_format)
        if res.status_code == 200:
            user_data = res.json()
            results_data = API_key + ',' + str(user_data['rate']['limit']) + ',' + str(user_data['rate']['used']) + ',' + str(user_data['rate']['remaining']) + ',' + str(convert_unix_timestamp(user_data['rate']['reset']))
            print(results_data.split(","))
            table.append(results_data.split(","))
        else:
            print(API_key + ', Error!')
        time.sleep(2)

    print('\n' + '*'*30 + "注释信息" + '*'*30 + '\n')
    Notes_json = {
        "limit": "总额度",
        "used": "使用总次数",
        "remaining": "余额",
        "reset_date": "重置时间"
    }
    # 将键写入到table中
    for key, value in Notes_json.items():
        table[0].append(key)
        print(f"{key}: {value}")
    print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    print(tabulate(table, headers='firstrow'))
