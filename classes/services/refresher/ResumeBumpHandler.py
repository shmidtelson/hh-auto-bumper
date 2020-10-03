import time
from classes.entity.ResumeEntity import ResumeEntity
from classes.services.ResumeBumpService import ResumeBumpService
from classes.services.refresher.AbstractHandler import AbstractHandler


class ResumeBumpHandler(AbstractHandler):
    resumeBumpService = None

    def __init__(self):
        self.resumeBumpService = ResumeBumpService()

    def handle(self, resume: ResumeEntity) -> str:
        if resume.getStatus() == ResumeEntity.STATUS_PUBLISHED:
            if self.resumeBumpService.isReadyToBump(resume.getUpdated()):
                self.resumeBumpService.bump(resume.getId())
                time.sleep(1)

        return super().handle(resume)
