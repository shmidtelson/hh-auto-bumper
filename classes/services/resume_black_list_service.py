from typing import Set

from classes.repository.hh_repository import HeadHunterRepository


class ResumeBlackListService:
    def __init__(self):
        self.repository = HeadHunterRepository()

    def getBlackListIdsByResumeId(self, resumeId):
        response = self.repository.get_black_list_companies_by_resume_id(resumeId)
        return set(map(lambda x: x.get('id'), response))

    def setBlackListCompaniesByResumeId(self, resumeId, blackListSet: Set[str]) -> None:
        data = {
            'items': list(map(lambda x: {'id': x}, blackListSet))
        }
        self.repository.set_black_list_companies_by_resume_id(resumeId, data)
