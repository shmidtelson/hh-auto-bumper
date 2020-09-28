from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
from rauth import OAuth2Service
import os
import requests

redirect_uri = 'http://localhost:8080'

hh = OAuth2Service(
    client_id=os.getenv('APP_ID'),
    client_secret=os.getenv('APP_SECRET'),
    name='Checker',
    authorize_url='https://hh.ru/oauth/authorize',
    access_token_url='https://hh.ru/oauth/token',
    base_url='https://hh.ru/')


params = {'state': 'read_stream',
          'response_type': 'code',
          'redirect_uri': redirect_uri
          }

url = hh.get_authorize_url(**params)
print(url)
response = requests.get(url)

print(response.text)

session = hh.get_auth_session(data={
    'grant_type': 'authorization_code',
    'redirect_uri': redirect_uri
})

print(session.get('me').json())