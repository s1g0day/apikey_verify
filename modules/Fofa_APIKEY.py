#/usr/bin/python3
# https://fofa.info/api/introd

import time
import requests
from tabulate import tabulate

def fofa_apikey_verify(files):
    print('\n' + '*'*30 + "key验证" + '*'*30 + '\n')
    table = [["email/key"]]
    
    # 构建 API 请求的 URL
    urllist = ["https://fofa.info","https://g.fofa.info"]
    def get_url_result(email, key, urllistint):
        get_url = urllist[urllistint] + "/api/v1/info/my?email={your_email}&key={your_key}"
        url = get_url.format(your_email=email, your_key=key)
        res = requests.get(url)
        results = res.json()
        return results

    def successkey(email, key, urllistint, results):
        results_data = email + ':' + key + ',' + urllist[urllistint] + ',' + str(results['isvip']) + ',' + str(results['vip_level']) + ',' + str(results['fcoin']) + ',' + str(results['fofa_point']) + ',' + str(results['remain_free_point']) + ',' + str(results['remain_api_query']) + ',' + str(results['remain_api_data'])
        print(results_data.split(","))
        table.append(results_data.split(","))

    for key in open(files):
        email, key = key.strip().split(":")
        urllistint = 0
        results = get_url_result(email, key, urllistint)
        
        if results["error"] == False:
            successkey(email, key, urllistint, results)
        elif results["error"] == True:
            urllistint = 1
            results = get_url_result(email, key, urllistint)
            if results["error"] == False:
                successkey(email, key, urllistint, results)
            else:
                print(email + ', Error!')
        time.sleep(2)

    print('\n' + '*'*30 + "注释信息" + '*'*30 + '\n')
    Notes_json = {
        "api_url": "api地址",
        "isvip": "是否是vip",
        "vip_level": "用户级别",
        "fcoin": "F币",
        "fofa_point": "F点",
        "remain_free_point": "剩余免费F点",
        "remain_api_query": "API月度剩余查询次数",
        "remain_api_data": "API月度剩余返回数量"
    }
        # 将键写入到table中
    for key, value in Notes_json.items():
        table[0].append(key)
        print(f"{key}: {value}")
    print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    print(tabulate(table, headers='firstrow'))


