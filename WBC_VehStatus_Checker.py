from datetime import datetime
import json
from time import sleep
import requests
import notification
from pyautogui import typewrite
from Models.model_config import Config

base_api = 'https://website-elastic-api.webuycars.co.za/api/get-car/'


file = open('config.json')
config = Config.from_dict(json.load(file))

def input_veh_code():
    print('Enter 9-digit Vehicle Code: ')
    typewrite(config.default_stock_code)
    return input()

def input_refresh_delay():
    print('Enter Refresh delay (sec): ')
    typewrite(str(config.default_refresh_delay))
    return input()

veh_code = input_veh_code()
refresh_delay = int(input_refresh_delay())

wbc_link = "https://www.webuycars.co.za/buy-a-car/{}".format(veh_code)
email_message = 'To: {}\nSubject: {}\n{}\n\n{}'.format(config.email_settings.to_email, config.email_settings.email_subject, config.email_settings.email_message,wbc_link)

while(True):
    response = requests.get(base_api+veh_code)
    if (response.status_code == 200):
        veh_status = response.json()['data']['Status']
        if(veh_status == 'For Sale'):
            print('Vehicle is available. An  email has been sent.', datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            notification.sendEmail(config.email_settings.port, config.email_settings.smtp_server, config.email_settings.from_email, config.email_settings.password, config.email_settings.to_email, email_message)
            sleep(refresh_delay)
        else:
            print('Vehicle Status: {}'.format(veh_status), datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
            sleep(refresh_delay)
    else:
        print('Invalid Stock Code!')
        veh_code = input_veh_code()