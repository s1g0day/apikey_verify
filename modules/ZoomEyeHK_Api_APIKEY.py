#/usr/bin/python3
# https://www.zoomeye.hk/doc

import time
import requests
from tabulate import tabulate

def zoomeyehk_api_apikey_verify(files):
    print('\n' + '*'*30 + "key验证" + '*'*30 + '\n')
    table = [["API_KEY"]]

    # 构建 API 请求的 URL
    API_URL = "https://api.zoomeye.hk/resources-info"
    for key in open(files):
        API_key=key.strip()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36',
            'API-KEY': API_key,
        }
        res = requests.get(API_URL, headers=headers)
        if res.status_code == 200:
            results = res.json()
            print(results)
            results_data = API_key + ',' + str(results["plan"]) + ',' + str(results["user_info"]["name"]) + ',' + str(results["resources"]["search"]) + ',' + str(results["resources"]["stats"]) + ',' + str(results["resources"]["interval"]) + ',' + str(results["user_info"]["expired_at"]) + ',' + str(results["quota_info"]["remain_free_quota"]) + ',' + str(results["quota_info"]["remain_pay_quota"]) + ',' + str(results["quota_info"]["remain_total_quota"])
            print(results_data.split(","))
            table.append(results_data.split(","))
        else:
            print(API_key + ', Error!')
        time.sleep(5)

    print('\n' + '*'*30 + "注释信息" + '*'*30 + '\n')
    Notes_json = {
        "name": "用户名称",
        "plan": "用户类型",
        "search": "搜索",
        "stats": "统计",
        "interval": "间隔",
        "expired_at": "过期时间",
        "remain_free_quota": "剩余免费配额",
        "remain_pay_quota": "剩余付费配额",
        "remain_total_quota": "剩余总配额",
    }
    # 将键写入到table中
    for key, value in Notes_json.items():
        table[0].append(key)
        print(f"{key}: {value}")
    print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    print(tabulate(table, headers='firstrow'))