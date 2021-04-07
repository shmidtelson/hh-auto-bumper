import os
import pickle
from os.path import dirname

from classes.client.RedisClient import RedisClient
from classes.entity.AccessTokenEntity import AccessTokenEntity


class Config:
    TOKEN_NAME = 'token'
    redis_client: RedisClient

    def __init__(self):
        self.redis_client = RedisClient()

    def getApiOauthUrl(self) -> str:
        return 'https://hh.ru/'

    def getOauthTokenEndpoint(self) -> str:
        return self.getApiOauthUrl() + 'oauth/token'

    def getApiUrl(self) -> str:
        return 'https://api.hh.ru/'

    def getMyResumesEndpoint(self) -> str:
        return self.getApiUrl() + 'resumes/mine'

    def getResumeBlackListEndpoint(self, resumeId: str) -> str:
        return self.getApiUrl() + f'resumes/{resumeId}/blacklist'

    def getAppId(self) -> str:
        return os.getenv('APP_ID')

    def getAppSecret(self) -> str:
        return os.getenv('APP_SECRET')

    def getAppPath(self) -> str:
        return dirname(dirname(__file__))

    def getAccessToken(self) -> AccessTokenEntity:
        return pickle.loads(self.redis_client.db.get(self.TOKEN_NAME))

    def setAccessToken(self, entity: AccessTokenEntity) -> None:
        self.redis_client.db.set(self.TOKEN_NAME, pickle.dumps(entity))

    def getAppEmail(self) -> str:
        return os.getenv('APP_EMAIL')

    def getAuthHeader(self):
        return {
            "Authorization": f"Bearer {self.getAccessToken().getAccessToken()}",
            "User Agent": f"Checker/1.0 ({self.getAppEmail()})"
        }

    def get_resume_views_history(self, resume_id: str) -> str:
        return self.getApiUrl() + f'resumes/{resume_id}/views'

    def get_employer_by_id(self, employer_id: str) -> str:
        return self.getApiUrl() + f'employers/{employer_id}'
