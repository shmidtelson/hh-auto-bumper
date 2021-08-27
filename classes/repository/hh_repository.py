import time

import requests
import json
from classes.config import Config
from classes.utils.logger import logger


class HeadHunterRepository:
    config = None

    def __init__(self):
        self.config = Config()

    def get_resumes(self):
        try:
            response = requests.get(self.config.getMyResumesEndpoint(), headers=self.config.getAuthHeader())
        except Exception as e:
            logger.error(e, exc_info=True)
            return []

        response_dict = json.loads(response.text)

        if 'items' not in response_dict:
            logger.error(response_dict, exc_info=True)
            return []

        logger.info('Got resumes')

        return response_dict['items']

    def get_black_list_companies_by_resume_id(self, resumeId):
        try:
            response = requests.get(self.config.getResumeBlackListEndpoint(resumeId),
                                    headers=self.config.getAuthHeader())
        except Exception as e:
            logger.error(e, exc_info=True)
            return []

        response_dict = json.loads(response.text)

        if 'items' not in response_dict:
            logger.error(response_dict)
            return []

        logger.info(f'Got black_list companies for resumeId: {resumeId}')

        return response_dict['items']

    def set_black_list_companies_by_resume_id(self, resumeId, data: dict) -> bool:
        try:
            requests.post(self.config.getResumeBlackListEndpoint(resumeId), json=data,
                          headers=self.config.getAuthHeader())
            logger.info(f'Updated black_list for: {resumeId}')
        except Exception as e:
            logger.error(e)
            return False

        return True

    """
    TODO: Return only unique list
    """
    def get_views_history_by_resume_id(self, resume_id: str):
        while True:
            try:
                response = requests.get(
                    self.config.get_resume_views_history(resume_id),
                    headers=self.config.getAuthHeader()
                )

                if response.ok:
                    logger.info(f'Got views_history for resume_id: {resume_id}')
                    return response.json()

            except Exception as e:
                logger.error(e)

            time.sleep(10)

    def get_employer_by_id(self, employer_id: str):
        while True:
            try:
                logger.info(f'Try to get info about employer_id {employer_id}')
                url = self.config.get_employer_by_id(employer_id)
                response = requests.get(
                    self.config.get_employer_by_id(employer_id),
                    headers=self.config.getAuthHeader()
                )

                if response.status_code == 200 and response.ok:
                    logger.info(f'Got employer_id {employer_id}')
                    return response.json()

                logger.error(f'{employer_id} not found. This is weird! {response.status_code} ({url})')
                return {}
            except Exception as e:
                logger.error(e, exc_info=True)

            time.sleep(10)
