import time

from classes.entity.resume_entity import ResumeEntity
from classes.services.resume_bump_service import ResumeBumpService


class ResumeBumpHandler:
    resumeBumpService = None

    def __init__(self):
        self.resumeBumpService = ResumeBumpService()

    def handle(self, resume: ResumeEntity) -> None:
        if resume.get_status() != ResumeEntity.STATUS_PUBLISHED:
            return None

        if resume.get_access_type() == ResumeEntity.ACCESS_TYPE_NO_ONE:
            return None

        if not self.resumeBumpService.isReadyToBump(resume.get_updated()):
            return None

        self.resumeBumpService.bump(resume.get_id())
        time.sleep(1)
