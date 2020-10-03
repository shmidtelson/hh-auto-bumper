from typing import Set

from classes.repository.HeadHunterRepository import HeadHunterRepository


class ResumeBlackListService:
    def __init__(self):
        self.repository = HeadHunterRepository()

    def getBlackListIdsByResumeId(self, resumeId):
        response = self.repository.getBlackListCompaniesByResumeId(resumeId)
        return set(map(lambda x: x.get('id'), response))

    def setBlackListCompaniesByResumeId(self, resumeId, blackListSet: Set[str]) -> None:
        data = {
            'items': list(map(lambda x: {'id': x}, blackListSet))
        }
        self.repository.setBlackListCompaniesByResumeId(resumeId, data)
