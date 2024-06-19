# 简介

起于subfinder，用于验证相应厂商APIKEY值可用性，娱乐项目

# 使用

- `key.txt`：依照subfinder的key值格式

运行，懒散操作使用了模糊匹配，只要确认输入的类型唯一即可

```
python3 main.py -t shodan	or	python3 main.py -t sho
完整类型可以查看 load_module.py 的 APIlist
python3 main.py -t shodan_apikey_verify
```

# 进度

已完成的代码均为 `modules/*_APIKEY.py`

```
Binaryedge
Censys
Fofa
Fullhunt
GithubApi
Hunter_io
Hunter_qianxin
Quake
SecurityTrails
Shodan
ViruStotal
ZoomEyeHK_Api
```



# Lssuse

该项目只适合分享、学习、交流，不得用于商业及非法用途。觉得项目不错的小伙伴，可以在右上角Star一下，后期项目会不断优化，在使用过程中什么建议与BUG ，欢迎大家提交Lssuse
