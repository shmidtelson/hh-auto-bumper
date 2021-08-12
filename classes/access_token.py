import json
import requests
from classes.config import Config
from classes.entity.AccessTokenEntity import AccessTokenEntity
from classes.utils.date_helper import DateHelper
from classes.utils.logger import logger


class AccessToken:
    config = None

    def __init__(self):
        self.config = Config()

    def handleRefreshToken(self, refresh_token: str) -> None:
        try:
            response = requests.post(self.config.getOauthTokenEndpoint(), {
                'grant_type': 'refresh_token',
                'refresh_token': refresh_token,
            })
            result = json.loads(response.text)

            if 'access_token' in result:
                logger.debug('Refresh access_token')
                self.config.setAccessToken(AccessTokenEntity(result))
        except Exception as e:
            logger.error(e)

    def isTokenExpired(self) -> bool:
        return DateHelper.getCurrentUnixDate() > self.config.getAccessToken().getExpiresAt()
