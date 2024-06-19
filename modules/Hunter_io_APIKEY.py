#/usr/bin/python3
# https://hunter.io/api-documentation/v2

import time
import requests
from tabulate import tabulate

def hunter_io_apikey_verify(files):
    print('\n' + '*'*30 + "key验证" + '*'*30 + '\n')
    table = [["API_key"]]

    # 构建 API 请求的 URL
    API_URL = "https://api.hunter.io/v2/account?api_key={key}"
    for key in open(files):
        API_key=key.strip()
        url = API_URL.format(key=API_key)
        res = requests.get(url)
        if res.status_code == 200:
            results = res.json()
            results_data = API_key + ',' + str(results['data']['plan_name']) + ',' + str(results['data']['plan_level'])+ ',' + str(results['data']['reset_date']) + ',' + str(results['data']['calls']['used']) + ',' + str(results['data']['calls']['available']) + ',' + str(results['data']['requests']['searches']["used"]) + ',' + str(results['data']['requests']['searches']['available']) + ',' + str(results['data']['requests']['verifications']["used"]) + ',' + str(results['data']['requests']['verifications']['available'])
            print(results_data.split(","))
            table.append(results_data.split(","))
        else:
            print(API_key + ', Error!')
        time.sleep(2)

    print('\n' + '*'*30 + "注释信息" + '*'*30 + '\n')
    Notes_json = {
        "plan_name": "会员计划",
        "plan_level": "会员级别",
        "reset_date": "重置时间",
        "calls_used": "使用总次数",
        "calls_available": "总额度",
        "searches_used": "搜索使用次数",
        "searches_available": "搜索总额度",
        "verifications_used": "验证使用次数",
        "verifications_available": "验证总额度"
    }
    # 将键写入到table中
    for key, value in Notes_json.items():
        table[0].append(key)
        print(f"{key}: {value}")
    print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    print(tabulate(table, headers='firstrow'))

