import requests as r
import time

last_mail = None

url = 'https://www.1secmail.com/api/v1/'
get_mail = '?action=genRandomMailbox&count=1'

res = r.request("GET", url+get_mail).json()

print(res[0])

mail = res[0].split('@')


get_messages = '?action=getMessages&login=' + f'{mail[0]}&domain={mail[1]}'
read_message = '?action=readMessage&login=' + f'{mail[0]}&domain={mail[1]}'

while (True):
    time.sleep(5)
    res = r.request("GET", url + get_messages).json()

    if len(res) > 0 and last_mail != res[0]:
        last_mail = res[0]
        get_data = f'&id={last_mail["id"]}'
        res = r.request("GET", url + read_message + get_data).json()

        data = res['from']
        print('From: ' + data)
        data = res['subject']
        print('Subject: ' + data)
        data = res['body']
        print('Mensaje:')
        for linea in data.split('<div'):
            for lin in linea.split('</div>'):
                lin = lin.replace('dir="ltr">','')
                lin = lin.replace('<br>','\n')
                lin = lin.replace('<','')
                lin = lin.replace('>','')
                print(lin)
