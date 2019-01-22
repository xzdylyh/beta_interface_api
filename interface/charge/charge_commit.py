#_*_coding:utf-8_*_
import requests,json
from base.base_config import BaseConfig

from library.scripts import getYamlfield
from library.scripts import retry
from globalVar import gl

class ChargeClass(object):
    url = "/charge/commit"
    payload = '------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"req\"\r\n\r\n{\"biz_id\":1337,\"is_diy\":false}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"appid\"\r\n\r\ndp3lF7bop2e5PTFXwLHTszgv\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ts\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"sig\"\r\n\r\n1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"v\"\r\n\r\n2.0\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--'
    headers = {
        'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
        'cache-control': "no-cache",
        'postman-token': "90d9ba84-836d-9744-f9f0-fb4fd9701d38"
    }

    def __init__(self):
        self.baseUrl = BaseConfig().base_url
        self.url = self.baseUrl + self.url



    #储值提交
    @property
    # @retry(reNum=getYamlfield(gl.configFile)['RETRY']['ReNum'])
    def chargeCommit(self):
        res = requests.request("POST",self.url,data=self.payload,headers=self.headers)
        if res.status_code ==200:
            return res.json()
        else:
            return {"errcode": 9001, "errmsg": str(res)}

if __name__=="__main__":

    print json.dumps(ChargeClass().chargeCommit).decode('unicode-escape')