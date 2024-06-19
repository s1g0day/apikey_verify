#/usr/bin/python3
# https://hunter.qianxin.com/home/helpCenter?r=5-1-1

import time
import base64
import requests
from tabulate import tabulate

def hunter_qianxin_apikey_verify(files):
    print('\n' + '*'*30 + "key验证" + '*'*30 + '\n')
    table = [["API_key"]]

    # 构建 API 请求的 URL
    search = 'domain.suffix="testtestesttesttesttesttest.com"'
    search = base64.urlsafe_b64encode(search.encode("utf-8"))
    searchs = str(search.decode('utf-8'))

    API_URL = "https://hunter.qianxin.com/openApi/search?api-key={key}&search={searchs_data}&page=1&page_size=10&is_web=1&start_time=2021-01-01&end_time=2021-03-01"
    
    for key in open(files):
        API_key=key.strip()
        url = API_URL.format(key=API_key, searchs_data = searchs)
        res = requests.get(url)
        if res.status_code == 200:
            results = res.json()
            if results['code'] == 200:
                results_data = API_key + ',' + str(results['data']['consume_quota']) + ',' + str(results['data']['rest_quota']) + ',' + results['message']
                print(results_data.split(","))
                table.append(results_data.split(","))
            elif results['code'] == 40204:
                results_data = API_key + ',' + '0' + ',' + '0' + ',' + results['message']
                print(results_data.split(","))
                table.append(results_data.split(","))
            elif results['code'] == 401:
                print(API_key + ', Error!')
        else:
            print(API_key + ', Error!')
        time.sleep(2)

    print('\n' + '*'*30 + "注释信息" + '*'*30 + '\n')
    Notes_json = {
        "account_type": "账户类型",
        "consume_quota": "消耗积分",
        "rest_quota": "今日剩余积分",
        "message": "备注"
    }
    # 将键写入到table中
    for key, value in Notes_json.items():
        table[0].append(key)
        print(f"{key}: {value}")
    print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    print(tabulate(table, headers='firstrow'))

