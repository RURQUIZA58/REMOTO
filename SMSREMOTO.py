import datetime
import requests
import schedule
import time
import json

response = requests.get('http://checkip.dyndns.org/')

def sms(numero,texto):
    global dt
    dt = datetime.datetime.today()

    # URL's para llamadas al API.
    api_auth_url = 'https://api-sms.softas.mx/api/auth/login/'
    send_sms_url = 'https://api-sms.softas.mx/api/sms/send'
    get_bal_url = 'https://api-sms.softas.mx/api/account/status'
    get_tr_code = 'https://api-sms.softas.mx/api/sms/get/'

    # Payload con información de autenticación.
    auth_payload = {
        'email': 'rulp@hotmail.com',
        'password': 'rulp.API.123'
    }

    # llamada API para autenticación.
    auth_api_call = requests.post(url=api_auth_url, data=auth_payload)

    # Validación si la llamada es correcta.
    if auth_api_call.status_code == 200:
        # Obtención del Token de autenticación.
        auth_token = auth_api_call.json()['token']

        # Generación de encabezados para agregar la autenticación a la petición.
        auth_headers = {
            'Authorization': 'Token {0}'.format(auth_token),
            'Content-Type': 'application/json'
            }
        get_bal_call = requests.get(url=get_bal_url, headers=auth_headers)
        #print(get_bal_call.json())
        # Generación de Payload con información de envío de SMS.
        sms_payload = {
            'numbers': [
                {'number': numero, 'message': texto}
            ]
        }

        # Llamada API para el envío de SMS.
        try:
            send_sms_call = requests.post(url=send_sms_url, data=json.dumps(sms_payload), headers=auth_headers,verify=True)
        except:
            print ('ERROR : ')


dt = datetime.datetime.today()

#schedule.every().day.at("12:02").do(sms,4424812489,"prueba "+str(dt)+response.text)
schedule.every(.5).minutes.do(sms,4424812489,"prueba "+str(dt))


while True:
    dt = datetime.datetime.today()
    now=datetime.datetime.now()
    schedule.run_pending()
    time.sleep(1)

