import time
from classes.AccessToken import AccessToken
from classes.Config import Config
from classes.AuthApp import AuthApp
from classes.ResumeService import ResumeService
from classes.repository.HeadHunterRepository import HeadHunterRepository


class Refresher:
    config = None
    authApp = None
    repository = None
    resumeService = None

    def __init__(self):
        self.config = Config()
        self.authApp = AuthApp()
        self.accessToken = AccessToken()
        self.repository = HeadHunterRepository()
        self.resumeService = ResumeService()

    def handle(self):
        tokenEntity = self.config.getAccessToken()

        if self.accessToken.isTokenExpired():
            self.accessToken.handleRefreshToken(tokenEntity.getRefreshToken())
            tokenEntity = self.config.getAccessToken()

        resumes = self.repository.getResumes()

        for resume in resumes:
            if resume.get('status').get('id') == 'published':
                resumeId = resume.get('id')
                date = resume.get('updated')

                if self.resumeService.isReadyToBump(date):
                    self.resumeService.bump(resumeId)
                    time.sleep(1)
