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
        if resume.get_access_type() == ResumeEntity.ACCESS_TYPE_BLACKLIST:
            data = self.resumeBlackListService.getBlackListIdsByResumeId(resume.get_id())
            current_black_list = self.resumeBlackListStorageService.get()
            current_black_list = current_black_list.union(data)

            self.resumeBlackListStorageService.set(current_black_list)
