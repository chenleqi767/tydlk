import requests
import json

# 创建一个持久化会话
session = requests.Session()

# 设置 cookie
cookies = {'uid': '4148359661949870080'}
session.cookies.update(cookies)

# 发送请求
productid_response = session.post('http://score.tydlk.com/scorequery/goldentouch/api/Project/ListForQueryScore')

productid_json = productid_response.json()

print(productid_json)