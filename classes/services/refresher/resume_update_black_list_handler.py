from classes.entity.resume_entity import ResumeEntity
from classes.services.resume_black_list_service import ResumeBlackListService
from classes.services.resume_black_list_storage_service import ResumeBlackListStorageService


class ResumeUpdateBlackListHandler:
    resumeBlackListService = None

    def __init__(self):
        self.resumeBlackListService = ResumeBlackListService()
        self.resumeBlackListStorageService = ResumeBlackListStorageService()

    def handle(self, resume: ResumeEntity) -> None:
        if resume.get_access_type() == ResumeEntity.ACCESS_TYPE_BLACKLIST:
            black_list_set = self.resumeBlackListStorageService.get()
            data = self.resumeBlackListService.getBlackListIdsByResumeId(resume.get_id())

            # Add if exists new elements
            if black_list_set.symmetric_difference(data):
                self.resumeBlackListService.setBlackListCompaniesByResumeId(resume.get_id(), black_list_set)
