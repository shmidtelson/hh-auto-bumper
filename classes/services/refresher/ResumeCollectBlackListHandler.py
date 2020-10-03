from classes.entity.ResumeEntity import ResumeEntity
from classes.services.ResumeBlackListService import ResumeBlackListService
from classes.services.ResumeBlackListStorageService import ResumeBlackListStorageService
from classes.services.refresher.AbstractHandler import AbstractHandler


class ResumeCollectBlackListHandler(AbstractHandler):
    resumeBlackListService = None
    resumeBlackListStorageService = None

    def __init__(self):
        self.resumeBlackListService = ResumeBlackListService()
        self.resumeBlackListStorageService = ResumeBlackListStorageService()

    def handle(self, resume: ResumeEntity) -> str:
        if resume.getAccessType() == ResumeEntity.ACCESS_TYPE_BLACKLIST:
            data = self.resumeBlackListService.getBlackListIdsByResumeId(resume.getId())
            currentBlackList = self.resumeBlackListStorageService.get()
            currentBlackList = currentBlackList.union(data)

            self.resumeBlackListStorageService.set(currentBlackList)

        # Blacklist
        return super().handle(resume)
