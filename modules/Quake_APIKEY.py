#/usr/bin/python3
# https://quake.360.cn/quake/#/help?id=5e6845ade1322779dd299e14&title=Quake%E7%AE%80%E4%BB%8B

import time
import requests
from tabulate import tabulate

def quake_apikey_verify(files):
    print('\n' + '*'*30 + "key验证" + '*'*30 + '\n')
    table = [["API_KEY"]]
    
    # 构建 API 请求的 URL
    API_URL = 'https://quake.360.cn/api/v3/user/info'

    for key in open(files):
        API_key=key.strip()
        header = {
            'X-QuakeToken': API_key
        }
        res = requests.get(API_URL,headers=header)
        if res.status_code == 200:
            results = res.json()
            lenrole = len(results["data"]["role"])
            # print(results)
            results_data = API_key + ',' + str(results["data"]["user"]["fullname"]) + ',' + str(results["data"]["user"]["email"]) + ',' + str(results["data"]["month_remaining_credit"]) + ',' + str(results["data"]["constant_credit"]) + ',' + str(results["data"]["free_query_api_count"]) + ',' + str(results["data"]["role"][lenrole-1]["fullname"])
            print(results_data.split(","))
            table.append(results_data.split(","))
        else:
            print(API_key + ', Error!')
        time.sleep(2)

    print('\n' + '*'*30 + "注释信息" + '*'*30 + '\n')
    Notes_json = {
        "user_fullname": "用户名",
        "email": "邮箱",
        "month_remaining_credit": "月度剩余积分",
        "constant_credit": "长效积分",
        "free_query_api_count": "api月度剩余免费查询次数",
        "role_fullname": "用户级别"
    }
    # 将键写入到table中
    for key, value in Notes_json.items():
        table[0].append(key)
        print(f"{key}: {value}")
    print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    print(tabulate(table, headers='firstrow'))

