import json
import os
import requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
from dotenv import load_dotenv, find_dotenv
from rauth import OAuth2Service
from classes.Config import Config
from classes.entity.AccessTokenEntity import AccessTokenEntity

load_dotenv(find_dotenv())

redirect_uri = os.getenv('APP_REDIRECT_URI')

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

class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        code = dict(parse.parse_qsl(parse.urlsplit(self.path).query)).get('code', None)

        if code:
            response = requests.post('https://hh.ru/oauth/token', {
                'grant_type': 'authorization_code',
                'client_id': os.getenv('APP_ID'),
                'client_secret': os.getenv('APP_SECRET'),
                'code': code,
                'redirect_uri': redirect_uri
            })

            result = json.loads(response.text)

            if 'access_token' in result:
                c = Config()
                c.setAccessToken(AccessTokenEntity(result))
                print(c.getAccessToken().getAccessToken())
            exit()

        self.send_response(200)
        self.end_headers()

        return


if __name__ == '__main__':
    server = HTTPServer(('', 8085), GetHandler)
    print('Starting server at http://localhost:8085')
    server.serve_forever()
