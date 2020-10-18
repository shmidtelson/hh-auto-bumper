import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib import parse
import requests

from dotenv import load_dotenv, find_dotenv

from classes.Config import Config
from classes.entity.AccessTokenEntity import AccessTokenEntity

load_dotenv(find_dotenv())

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        code = dict(parse.parse_qsl(parse.urlsplit(self.path).query)).get('code', None)

        if code:
            response = requests.post('https://hh.ru/oauth/token', {
                'grant_type': 'authorization_code',
                'client_id': os.getenv('APP_ID'),
                'client_secret': os.getenv('APP_SECRET'),
                'code': code,
                'redirect_uri': 'http://localhost:8080'
            })

            result = json.loads(response.text)

            if 'access_token' in result:
                c = Config()
                c.setAccessToken(AccessTokenEntity(result))

            exit()

        self.send_response(200)
        self.end_headers()

        return


if __name__ == '__main__':
    server = HTTPServer(('localhost', 8080), GetHandler)
    print('Starting server at http://localhost:8080')
    server.serve_forever()
