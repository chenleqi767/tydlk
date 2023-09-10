import requests
import json


# 创建一个持久化会话
session = requests.Session()

# 设置 cookie
cookies = {'uid': '4148359661949870080'}
session.cookies.update(cookies)

# 设置UA

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}




#
get_score_post_data = {
    "projectId": 576,
    "candidateNumber": "554610221503",
    "historyRangeId": 16,
    "type": 0,
    "className": "",
    "needInfoFalg": 1
}


score_response = session.post(url="http://score.tydlk.com/scorequery/goldentouch/api/QueryScoreOnlie/ScoreQuery_ClassInfo",data=get_score_post_data,headers=headers)

print(score_response.text)