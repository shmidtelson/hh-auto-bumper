import time
from classes.config import Config
from classes.access_token import AccessToken
from classes.services.refresher.resume_update_description_handler import ResumeUpdateDescriptionHandler
from classes.services.resume_service import ResumeService
from classes.services.refresher.resume_bump_handler import ResumeBumpHandler
from classes.services.refresher.resume_collect_black_list_handler import ResumeCollectBlackListHandler
from classes.services.refresher.resume_update_black_list_handler import ResumeUpdateBlackListHandler
from classes.services.refresher.resume_check_views_handler import ResumeCheckViewsHandler
from classes.utils.logger import logger


class Refresher:
    config = None
    accessToken = None
    resumeService = None
    resume_bump_handler = ResumeBumpHandler()
    resume_check_views_handler = ResumeCheckViewsHandler()
    resume_collect_black_list_handler = ResumeCollectBlackListHandler()
    resume_update_black_list_handler = ResumeUpdateBlackListHandler()
    resume_update_description_handler = ResumeUpdateDescriptionHandler()

    def __init__(self):
        self.config = Config()
        self.accessToken = AccessToken()
        self.resumeService = ResumeService()

    def execute(self):
        while True:
            try:
                expired = self.accessToken.isTokenExpired()
                break
            except Exception as e:
                logger.info('Access key is not found')
            time.sleep(10)

        if expired:
            logger.info('Access token expired. Try to get new')
            self.accessToken.handleRefreshToken(self.config.getAccessToken().getRefreshToken())

        resumes = self.resumeService.getPublishedResumes()

        # Resumes read
        for resume in resumes:
            # Who watched our resume
            self.resume_check_views_handler.handle(resume.get_id())

            # Bump if it is possibly
            self.resume_bump_handler.handle(resume)

            # Collect black list
            self.resume_collect_black_list_handler.handle(resume)

        # Resumes write
        for resume in resumes:
            self.resume_update_black_list_handler.handle(resume)

        # Update resume description
        for resume in resumes:
            self.resume_update_description_handler.handle(resume)
