import requests
import time
from requests.structures import CaseInsensitiveDict

def photoChecker():
    name = 'ids.txt'
    data = {}
    with open(name) as f:
        lines = f.readlines()
        for line in lines:
            if not line == '':
                email, rmid = line.strip().split(',')
                data[email] = {'rmid': rmid, 'points': 0}
    open('outputid.txt', 'w+').close()


    headers = {
        'authority': 'event-api.realme.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'language': 'en',
        'cookie': '',
        'origin': 'https://event.realme.com',
        'referer': 'https://event.realme.com/',
        'sec-ch-ua-mobile': '?1',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Mobile Safari/537.36',
        'x-user-id': '',
    }

    headers5 = {
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
    for email, info in data.items():
        print(email)
        headers['cookie'] ='RMID=' + info['rmid'] + ';' 
        headers5['cookie'] = 'RMID=' + info['rmid'] + ';'
        ########
        #daily sign in

        res = requests.post('https://api.realme.com/in/auth/login', headers = headers5).json()
        #print(res)
        user_id = '00'+ str(res['data']['userId'])
        print(user_id)
        headers5['x-user-id'] = user_id
        res1 = requests.get('https://event-api.realme.com/in/sign/v1/mini/user-sign-in/sign-in', headers=headers5)
        print(res1.json())




        # sending user id
        res = requests.post('https://api.realme.com/in/auth/login', headers = headers).json()
        #print(res)
        uuid = str(res['data']['userId'])
        user_id = '00'+ str(res['data']['userId'])
        print(user_id)
        headers['x-user-id'] = user_id

        ##########
        ##gettin object id
        res1 = requests.get('https://event-api.realme.com/in/sign/v1/mini/user-sign-in/sign-in-info', headers = headers)
        object_id = res1.json()['sign_in_result']['uuid']


        data = '{"object_id":"' + str(object_id) + '"'   ',"object_type":2,"url":"https://s1.realme.net/event/sign/simple/1665065372461_249264.jpeg","uuid":"' + str(uuid) + '"}'
        print(data)
        print(type(data))
        res2 = requests.get('https://event-api.realme.com/in/sign/v1/mini/user-sign-in/sign-in', headers = headers)
        res = requests.put('https://event-api.realme.com/in/sign/v1/mini/activityFiles/addActivityFile', headers=headers, data=data)

        print(res.json())



        ###get id
        res3 = requests.get('https://event-api.realme.com/in/sign/v1/mini/activityFiles/queryList?objectType=2&pageIndex=1&pageSize=100', headers=headers )
        id = res3.json()['data'][0]['id']
        print(id)
        with open('outputid.txt', 'a+') as f:
            f.write(str(id) + '\n')