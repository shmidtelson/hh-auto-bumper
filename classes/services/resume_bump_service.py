from datetime import datetime
import requests
from classes.config import Config
from classes.utils.date_helper import DateHelper
from classes.utils.logger import logger


class ResumeBumpService:
    RANGE_BUMP = 14400
    config = None

    def __init__(self):
        self.config = Config()

    def isReadyToBump(self, date: datetime) -> bool:
        unix_date = int(date.timestamp())
        return (DateHelper.getCurrentUnixDate() - unix_date) > self.RANGE_BUMP

    def bump(self, resume_id: str) -> None:
        try:
            requests.post(f"{self.config.getApiUrl()}resumes/{resume_id}/publish", headers=self.config.getAuthHeader())
            logger.info(f'Bumped resume: {resume_id}')
        except Exception as e:
            logger.error(e)
