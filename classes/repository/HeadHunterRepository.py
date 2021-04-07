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

    def getBlackListCompaniesByResumeId(self, resumeId):
        try:
            response = requests.get(self.config.getResumeBlackListEndpoint(resumeId),
                                    headers=self.config.getAuthHeader())
        except Exception as e:
            logger.error(e)
            return []

        responseDict = json.loads(response.text)

        if 'items' not in responseDict:
            logger.error(responseDict)
            return []

        return responseDict['items']

    def setBlackListCompaniesByResumeId(self, resumeId, data: dict) -> bool:
        try:
            requests.post(self.config.getResumeBlackListEndpoint(resumeId), json=data,
                          headers=self.config.getAuthHeader())
        except Exception as e:
            logger.error(e)
            return False

        return True

    def get_views_history_by_resume_id(self, resume_id: str):
        try:
            response = requests.get(self.config.get_resume_views_history(resume_id),
                                    headers=self.config.getAuthHeader()
                                    )

        except Exception as e:
            logger.error(e)
            return []

        return response.json()

    def get_employer_by_id(self, employer_id: str):
        try:
            response = requests.get(self.config.get_employer_by_id(employer_id),
                                    headers=self.config.getAuthHeader()
                                    )

        except Exception as e:
            logger.error(e)
            return []

        return response.json()
