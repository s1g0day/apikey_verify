#/usr/bin/python3
import time
import shodan
from tabulate import tabulate

def shodan_apikey_verify(files):
    print('\n' + '*'*30 + "key验证" + '*'*30 + '\n')
    table = [["API_KEY"]]

    # 构建 API 请求的 URL
    
    for key in open(files):
        api = shodan.Shodan(key.strip())
        try:
            results = api.info()    # GET https://api.shodan.io/api-info?key=xxx
            results_data = key.strip() + "," + str(results["scan_credits"]) + "," + str(results["query_credits"]) + "," + str(results["usage_limits"]["monitored_ips"]) + "," + str(results["monitored_ips"])
            print(results_data.split(","))
            table.append(results_data.split(","))
        except shodan.APIError as e:
            print(key.strip() + ',Error: {}'.format(e))
        time.sleep(5)

    print('\n' + '*'*30 + "注释信息" + '*'*30 + '\n')
    Notes_json = {
        "scan_credits": "剩余扫描积分",
        "query_credits": "剩余查询积分",
        "usage_limits_ips": "可监控IP数",
        "monitored_ips": "已监控IP数"
    }
    # 将键写入到table中
    for key, value in Notes_json.items():
        table[0].append(key)
        print(f"{key}: {value}")
    print('\n' + '*'*30 + "程序结果" + '*'*30 + '\n')
    print(tabulate(table, headers='firstrow'))