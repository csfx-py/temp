import requests
import time
from requests.structures import CaseInsensitiveDict


name = '250ids.txt'
data = {}
with open(name) as f:
    lines = f.readlines()
    for line in lines:
        if not line == '':
            email, rmid = line.strip().split(',')
            data[email] = {'rmid': rmid, 'points': 0}
data1 = []
with open('outputid.txt') as f:
    lines = f.readlines()
    for line in lines:
        if not line == '':
            id = line.strip()
            data1.append(id)
temp = data1.copy()

headers = {
    'authority': 'event-api.realme.com',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'cookie': '',
    'language': 'en',
    'origin': 'https://event.realme.com',
    'referer': 'https://event.realme.com/',
    'sec-ch-ua-mobile': '?1',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
    'x-user-id': ''
}    

i = 1

for file_id in data1:
    for email, info in data.items():
        print(email + ' ' + str(i))
        headers['cookie'] ='RMID=' + info['rmid'] + ';' 

    ########################

        data2 = '{"object_type":2,"file_id":"' + file_id + '","type":3}' 
        res = requests.post('https://api.realme.com/in/auth/login', headers = headers).json()
        #print(res)
        user_id = '00'+ str(res['data']['userId'])
        print(user_id)
        headers['x-user-id'] = user_id
        res1 = requests.put('https://event-api.realme.com/in/sign/v1/mini/activityFileLikes/addActivityFileLike', headers=headers, data = data2)
        print(res1.json())
    i = i +1
    temp.remove(file_id)
    with open('outputid.txt', 'w+') as f:
        for file_id in temp:
            f.write(file_id +'\n')






#response = requests.put('https://event-api.realme.com/in/sign/v1/mini/activityFileLikes/addActivityFileLike', headers=headers, data=data)
