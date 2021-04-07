from typing import List

from classes.repository.HeadHunterRepository import HeadHunterRepository
from classes.services.ResumeBlackListService import ResumeBlackListService


class ResumeCheckViewsHandler:
    AGENCY_TYPE = 'agency'
    repo = HeadHunterRepository()
    resume_black_list_service = ResumeBlackListService()

    def handle(self, resume_id: str):
        result = []
        employers = self.repo.get_views_history_by_resume_id(resume_id)
        for employer in employers.get('items'):
            employer_id = employer.get('employer').get('id')
            employer_data = self.repo.get_employer_by_id(employer_id)
            if employer_data.get('type') == ResumeCheckViewsHandler.AGENCY_TYPE:
                result.append(employer_id)

        self.__set_black_list(resume_id, result)

    def __set_black_list(self, resume_id: str, ids: List):
        data = self.resume_black_list_service.getBlackListIdsByResumeId(resume_id)
        print(ids)
        if ids:
            for i in ids:
                if i not in data:
                    data.add(i)
                    print('added ')
                    print(i)
            self.resume_black_list_service.setBlackListCompaniesByResumeId(resume_id, data)

