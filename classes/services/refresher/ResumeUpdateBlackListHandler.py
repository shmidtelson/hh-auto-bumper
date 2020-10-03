from classes.entity.ResumeEntity import ResumeEntity
from classes.services.ResumeBlackListService import ResumeBlackListService
from classes.services.refresher.AbstractHandler import AbstractHandler
from classes.services.ResumeBlackListStorageService import ResumeBlackListStorageService


class ResumeUpdateBlackListHandler(AbstractHandler):
    resumeBlackListService = None

    def __init__(self):
        self.resumeBlackListService = ResumeBlackListService()
        self.resumeBlackListStorageService = ResumeBlackListStorageService()

    def handle(self, resume: ResumeEntity) -> str:
        if resume.getAccessType() == ResumeEntity.ACCESS_TYPE_BLACKLIST:
            blackListSet = self.resumeBlackListStorageService.get()
            self.resumeBlackListService.setBlackListCompaniesByResumeId(resume.getId(), blackListSet)

        # Blacklist
        return super().handle(resume)