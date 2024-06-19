#/usr/bin/python3
# https://www.virustotal.com/gui/user/gsd/apikey
# https://developers.virustotal.com/reference/user

import time
import requests
from tabulate import tabulate

def virustotal_apikey_verify(files):
    print('\n' + '*'*30 + "程序运行" + '*'*30 + '\n')
    table = [["API_key", "monthly_used", "monthly_allowed", "daily_used", "daily_allowed", "hourly_used", "hourly_allowed"]]

    API_URL = 'https://www.virustotal.com/api/v3/users/{id}'

    for key in open(files):
        API_key=key.strip()
        url = API_URL.format(id=API_key)
        header = {
            'x-apikey': API_key
        }
        res = requests.get(url,headers=header)
        if res.status_code == 200:
            results = res.json()
            results_data = API_key + ',' + str(results["data"]["attributes"]["quotas"]["api_requests_monthly"]["used"]) + ',' + str(results["data"]["attributes"]["quotas"]["api_requests_monthly"]["allowed"]) + ',' + str(results["data"]["attributes"]["quotas"]["api_requests_daily"]["used"]) + ',' + str(results["data"]["attributes"]["quotas"]["api_requests_daily"]["allowed"]) + ',' + str(results["data"]["attributes"]["quotas"]["api_requests_hourly"]["used"]) + ',' + str(results["data"]["attributes"]["quotas"]["api_requests_hourly"]["allowed"]) 
            print(results_data.split(","))
            table.append(results_data.split(","))
        else:
            print(API_key + ', Error!')
        time.sleep(2)

    print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    test = '''
    api_requests_monthly_used: 每月已使用的api请求,
    api_requests_monthly_allowed: 每月的api请求额度, 
    api_requests_daily_used: 每天已使用的api请求, 
    api_requests_daily_allowed: 每天的api请求额度
    api_requests_hourly_used: 每小时已使用的api请求, 
    api_requests_hourly_allowed: 每小时的api请求额度
    '''
    print(test + '\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    print(tabulate(table, headers='firstrow'))

