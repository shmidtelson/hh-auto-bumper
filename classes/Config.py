import os
import pickle
import datetime
from os.path import dirname

from classes.entity.AccessTokenEntity import AccessTokenEntity


class Config:
    ACCESS_TOKEN_PATH = '/var/access_keys.pickle'

    def getApiOauthUrl(self) -> str:
        return 'https://hh.ru/'

    def getOauthTokenEndpoint(self) -> str:
        return self.getApiOauthUrl() + 'oauth/token'

    def getApiUrl(self) -> str:
        return 'https://api.hh.ru/'

    def getMyResumesEndpoint(self) -> str:
        return self.getApiUrl() + 'resumes/mine'

    def getAppId(self) -> str:
        return os.getenv('APP_ID')

    def getAppSecret(self) -> str:
        return os.getenv('APP_SECRET')

    def getAppPath(self) -> str:
        return dirname(dirname(__file__))

    def getAccessToken(self) -> AccessTokenEntity:
        with open(self.getAppPath() + self.ACCESS_TOKEN_PATH, 'rb') as file:
            entity = pickle.load(file)

        return entity

    def setAccessToken(self, entity: AccessTokenEntity) -> None:
        with open(self.getAppPath() + self.ACCESS_TOKEN_PATH, 'wb') as file:
            pickle.dump(entity, file)

    def getAppEmail(self) -> str:
        return os.getenv('APP_EMAIL')

    def getAuthHeader(self):
        return {
            "Authorization": f"Bearer {self.getAccessToken().getAccessToken()}",
            "User Agent": f"Checker/1.0 ({self.getAppEmail()})"
        }
