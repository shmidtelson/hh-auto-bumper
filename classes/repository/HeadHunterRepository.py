import requests
import json
from classes.Config import Config
from classes.utils.logger import logger

class HeadHunterRepository:
    config = None

    def __init__(self):
        self.config = Config()

    def getResumes(self):
        try:
            response = requests.get(self.config.getMyResumesEndpoint(), headers=self.config.getAuthHeader())
        except Exception as e:
            logger.error(e)
            return []

        responseDict = json.loads(response.text)

        if 'items' not in responseDict:
            logger.error(responseDict)
            return []

        return responseDict['items']