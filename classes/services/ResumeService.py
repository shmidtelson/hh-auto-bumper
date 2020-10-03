from classes.entity.ResumeEntity import ResumeEntity
from classes.repository.HeadHunterRepository import HeadHunterRepository

class ResumeService:
    repository = None

    def __init__(self):
        self.repository = HeadHunterRepository()

    def getResumes(self) -> list:
        result = []
        resumes = self.repository.getResumes()
        for resume in resumes:
            result.append(ResumeEntity.createFromResponse(resume))

        return result