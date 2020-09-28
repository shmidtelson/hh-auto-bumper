from datetime import datetime
import requests
from classes.Config import Config
from classes.utils.DateHelper import DateHelper
from classes.utils.logger import logger
class ResumeService:

    RANGE_BUMP = 14400
    config = None

    def __init__(self):
        self.config = Config()

    def isReadyToBump(self, date: str) -> bool:
        unixDate = int(datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z').timestamp())
        return (DateHelper.getCurrentUnixDate() - unixDate) > self.RANGE_BUMP

    def bump(self, resumeId: str) -> None:
        try:
            requests.post(f"{self.config.getApiUrl()}resumes/{resumeId}/publish", headers=self.config.getAuthHeader())
        except Exception as e:
            logger.error(e)
