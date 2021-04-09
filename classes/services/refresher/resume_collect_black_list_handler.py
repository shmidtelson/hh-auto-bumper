from classes.entity.resume_entity import ResumeEntity
from classes.services.resume_black_list_service import ResumeBlackListService
from classes.services.resume_black_list_storage_service import ResumeBlackListStorageService


class ResumeCollectBlackListHandler:
    resumeBlackListService = None
    resumeBlackListStorageService = None

    def __init__(self):
        self.resumeBlackListService = ResumeBlackListService()
        self.resumeBlackListStorageService = ResumeBlackListStorageService()

    def handle(self, resume: ResumeEntity) -> None:
        if resume.getAccessType() == ResumeEntity.ACCESS_TYPE_BLACKLIST:
            data = self.resumeBlackListService.getBlackListIdsByResumeId(resume.getId())
            currentBlackList = self.resumeBlackListStorageService.get()
            currentBlackList = currentBlackList.union(data)

            self.resumeBlackListStorageService.set(currentBlackList)
