from __future__ import annotations

from datetime import datetime


class ResumeEntity:
    STATUS_PUBLISHED = 'published'
    ACCESS_TYPE_BLACKLIST = 'blacklist'
    ACCESS_TYPE_NO_ONE = 'no_one'

    __id = None
    __status = None
    __access_type = None
    __similar_vacancies_count = 0
    __updated = None
    __total_views = 0

    @staticmethod
    def createFromResponse(response) -> ResumeEntity:
        entity = ResumeEntity()
        entity.set_id(response.get('id'))
        entity.set_status(response.get('status').get('id'))
        entity.set_access_type(response.get('access').get('type').get('id'))
        entity.set_similar_vacancies_count(response.get('similar_vacancies').get('counters').get('total'))
        entity.set_updated_from_string(response.get('updated'))
        entity.set_total_views(response.get('total_views'))

        return entity

    def get_id(self):
        return self.__id

    def set_id(self, id) -> None:
        self.__id = id

    def get_status(self) -> str:
        return self.__status

    def set_status(self, status) -> None:
        self.__status = status

    def get_access_type(self) -> str:
        return self.__access_type

    def set_access_type(self, access_type) -> None:
        self.__access_type = access_type

    def set_similar_vacancies_count(self, count: int):
        self.__similar_vacancies_count = count

    def get_similar_vacancies_count(self):
        return self.__similar_vacancies_count

    def set_updated_from_string(self, date: str):
        self.__updated = datetime.strptime(date, '%Y-%m-%dT%H:%M:%S%z')

    def get_updated(self) -> datetime:
        return self.__updated

    def set_total_views(self, count: int):
        self.__total_views = count

    def get_total_views(self) -> int:
        return self.__total_views
