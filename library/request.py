# _*_coding:utf-8_*_
import requests
from interface_project.base.base_config import BaseConfig
import json
from interface_project.library.scripts import retry
from requests.exceptions import ConnectionError,\
    ConnectTimeout,HTTPError,Timeout

class HttpWebRequest(object):

    payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"req\"\r\n\r\n{\"cno\":\"1151996117825155\",\"activity_id\":3032065}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"appid\"\r\n\r\ndp1svA1gkNt8cQMkoIv7HmD1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ts\"\r\n\r\n123\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sig\"\r\n\r\n111\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"v\"\r\n\r\n2.0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "b551c555-a137-32f0-9cda-da434e3fc74c"
    }

    def __init__(self,url='/xxx/xxxx'):
        self.baseUrl  = BaseConfig().base_url
        self.url = self.baseUrl + str(url).strip()


    # post请求
    @retry(reNum=3)
    def post(self):
        res = requests.request("POST",self.url,data=self.payload,headers=self.headers)
        if res.status_code ==200:
            return res.json()
        else:
            return {"errcode": 9001, "errmsg": str(res)}


if __name__ == "__main__":
    print json.dumps(HttpWebRequest().post())\
        .decode('unicode-escape')


