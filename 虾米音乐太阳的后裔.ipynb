import requests
import json,re

url = 'https://music.xiami.com/resource/collect/v2/detail/334573806/366661006/1519811760?auth_key=1589091771853-0-0-d24741bcae3ac53838ae0a85f7a9d094&_s=74fdac2f7934521184ea4216b5295bf9'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:73.0) Gecko/20100101 Firefox/73.0'}
response = requests.get( url=url, headers=headers ).json()
songs = response['resultObj']['songs']

for song in songs:
    filename = song['songName']+'.wav'
    re.sub('[\/:*?"<>|]', '', filename)
    fileurl = song['listenFiles'][0]['listenFile']
    filedata = requests.get(url=fileurl, headers=headers).content
    filepath = 'C:/Users/shenanna/Desktop/太阳的后裔OST/'+filename
    with open (filepath, 'wb') as fp:
        fp.write ( filedata )
        print(filename+'下载成功！')
