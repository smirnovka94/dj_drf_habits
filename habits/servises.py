import os
from dotenv import load_dotenv
import requests

load_dotenv(dotenv_path='.env')

token = os.getenv('TG_TOKEN')
user_id = os.getenv('TG_NAME_ID')

def send_tg(user_id, message):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    data = {
        'chat_id': user_id,
        'text': message
    }
    response = requests.post(url, data=data)
    print(response.json())

send_tg(user_id, 'test')