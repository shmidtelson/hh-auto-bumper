from typing import List

from classes.entity.resume_entity import ResumeEntity
from classes.repository.hh_repository import HeadHunterRepository


class ResumeService:
    repository = None

    def __init__(self):
        self.repository = HeadHunterRepository()

    def getResumes(self) -> List[ResumeEntity]:
        result = []
        resumes = self.repository.get_resumes()
        for resume in resumes:
            result.append(ResumeEntity.createFromResponse(resume))

        return result
