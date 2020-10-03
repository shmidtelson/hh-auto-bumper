import requests
import json
from typing import Union
from classes.utils.logger import logger
from classes.Config import Config


class AuthApp:
    config = None

    def __init__(self):
        self.config = Config()

    def handle(self) -> Union[bool, str]:
        try:
            response = requests.post(self.config.getOauthTokenEndpoint(),
                                     {
                                         'grant_type': 'client_credentials',
                                         'client_id': self.config.getAppId(),
                                         'client_secret': self.config.getAppSecret(),
                                     }
                                     )
        except Exception as e:
            logger.error(e)
            return False

        responseDict = json.loads(response.text)

        if 'error' in responseDict:
            logger.error(responseDict.get('error'))
            return False

        if 'access_token' in responseDict:
            self.config.setAccessToken(responseDict.get('access_token'))

        return True
