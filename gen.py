import requests as rq
from datetime import datetime
import os
import discord


def getacc(input):
    BASE_URL = "https://sxskey.pythonanywhere.com"
    payload = {'input': input}
    respose = rq.get(BASE_URL, params=payload)

    json_values = respose.json()

    rq_input = json_values['input']
    timestamp = json_values['timestamp']



    print(f'input is: {rq_input}')
    print(f'date is: {datetime.fromtimestamp(timestamp)}')
    if(input == 'nord'):
        nordvpnacc = json_values['nordvpnacc']
        print(f'the account is: {nordvpnacc}')
        return nordvpnacc
    elif(input == 'crunchy'):
        crunchyacc = json_values['crunchyacc']
        print(f'the account is: {crunchyacc}')
        return crunchyacc




getacc("crunchy")

#os.system('python assets.py')
