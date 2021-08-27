from datetime import datetime

from classes.entity.resume_entity import ResumeEntity
from classes.repository.hh_repository import HeadHunterRepository
from templates.cv import DESCRIPTION


class ResumeUpdateDescriptionHandler:
    def __init__(self):
        self.hh_repository = HeadHunterRepository()

    def handle(self, resume: ResumeEntity) -> None:
        content = f"""{DESCRIPTION}
        
Информация от бота, который управляет этим резюме:
{self.get_date_latest_bot_work_message(resume.get_updated())}
{self.get_similar_vacancies_message(resume.get_similar_vacancies_count())}
{self.get_total_views_message(resume.get_total_views())}
{self.get_blocked_companies_message(resume)}
        """
        self.hh_repository.set_resume_description_by_id(resume.get_id(), content)

    @staticmethod
    def get_similar_vacancies_message(count_vacancies: int) -> str:
        return f'Подходящих вакансий: {count_vacancies}'

    @staticmethod
    def get_date_latest_bot_work_message(updated_date: datetime) -> str:
        return f'Дата последней работы бота: {updated_date.strftime("%d %B %Y %H:%M:%S")}'

    def get_blocked_companies_message(self, resume: ResumeEntity) -> str:
        black_list_companies_text = ''
        if resume.get_access_type() == resume.ACCESS_TYPE_BLACKLIST:
            count = self.hh_repository.get_black_list_companies_count_by_resume_id(resume.get_id())
            black_list_companies_text = f'Количество заблокированных компаний: {count}'

        return black_list_companies_text

    @staticmethod
    def get_total_views_message(total_views: int) -> str:
        return f'Всего просмотров этого резюме: {total_views}'
