from classes.entity.resume_entity import ResumeEntity
from classes.services.resume_black_list_service import ResumeBlackListService
from classes.services.resume_black_list_storage_service import ResumeBlackListStorageService


class ResumeUpdateBlackListHandler:
    resumeBlackListService = None

    def __init__(self):
        self.resumeBlackListService = ResumeBlackListService()
        self.resumeBlackListStorageService = ResumeBlackListStorageService()

    def handle(self, resume: ResumeEntity) -> None:
        if resume.getAccessType() == ResumeEntity.ACCESS_TYPE_BLACKLIST:
            blackListSet = self.resumeBlackListStorageService.get()
            data = self.resumeBlackListService.getBlackListIdsByResumeId(resume.getId())

            # Add if exists new elements
            if blackListSet.symmetric_difference(data):
                self.resumeBlackListService.setBlackListCompaniesByResumeId(resume.getId(), blackListSet)
