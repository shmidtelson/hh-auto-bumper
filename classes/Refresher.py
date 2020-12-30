import time
from classes.Config import Config
from classes.AccessToken import AccessToken
from classes.services.ResumeService import ResumeService
from classes.services.refresher.ResumeBumpHandler import ResumeBumpHandler
from classes.services.refresher.ResumeCollectBlackListHandler import ResumeCollectBlackListHandler
from classes.services.refresher.ResumeUpdateBlackListHandler import ResumeUpdateBlackListHandler
from classes.utils.logger import logger


class Refresher:
    config = None
    accessToken = None
    resumeService = None

    def __init__(self):
        self.config = Config()
        self.accessToken = AccessToken()
        self.resumeService = ResumeService()

    def execute(self):
        while True:
            try:
                expired = self.accessToken.isTokenExpired()
                break
            except:
                print('Access token not found')
            time.sleep(10)

        if expired:
            logger.info('Access token expired. Try to get new')
            self.accessToken.handleRefreshToken(self.config.getAccessToken().getRefreshToken())

        resumes = self.resumeService.getResumes()

        # Resumes Bump and collect Data
        for resume in resumes:
            resumeBumpHandler = ResumeBumpHandler()
            resumeCollectBlackListHandler = ResumeCollectBlackListHandler()
            # Setup our Chain
            resumeBumpHandler.set_next(resumeCollectBlackListHandler)
            # Run Chain
            resumeBumpHandler.handle(resume)

        # Update resumes
        for resume in resumes:
            resumeUpdateBlackListHandler = ResumeUpdateBlackListHandler()
            # Setup our Chain
            resumeUpdateBlackListHandler.handle(resume)
