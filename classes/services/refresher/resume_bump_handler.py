import time

from classes.entity.resume_entity import ResumeEntity
from classes.services.resume_bump_service import ResumeBumpService


class ResumeBumpHandler:
    resumeBumpService = None

    def __init__(self):
        self.resumeBumpService = ResumeBumpService()

    def handle(self, resume: ResumeEntity) -> None:
        if resume.getStatus() != ResumeEntity.STATUS_PUBLISHED:
            return None

        if resume.getAccessType() == ResumeEntity.ACCESS_TYPE_NO_ONE:
            return None

        if not self.resumeBumpService.isReadyToBump(resume.getUpdated()):
            return None

        self.resumeBumpService.bump(resume.getId())
        time.sleep(1)
