import json
import urllib.request

api_url = 'http://openapi.tuling123.com/openapi/api/v2'

for i in range(100):
    text_input = input('我：')

    req = {
        'perception':{
            'inputText':{
                'text': text_input
            },
            'selfInfo':{
                'location':{
                    'city': '北京',
                    'province': '北京',
                    'street': '海淀区某路'
                }
            }
        },
        'userInfo': {
            'apiKey': 'd700d6e902de45dc90b8f16f4aaf8f74',
            'userId': 'OnlyUseAlphabet'
        }
    }

    # 将字典格式的req编码为utf8，因为调用图灵API的各个环节的编码方式均为UTF-8
    req = json.dumps(req).encode('utf8')  #将req（dict）编码成JSON格式的str，再编码成utf8

    http_post = urllib.request.Request(api_url, data=req, headers={'content-type': 'application/json'})
    response = urllib.request.urlopen(http_post)
    response_str = response.read().decode('utf8')  #response.read()出来的类型是bytes，按utf8解码成str
    response_dic = json.loads(response_str)
    results_text = response_dic['results'][0]['values']['text']
    print('Turing：'+ results_text)
