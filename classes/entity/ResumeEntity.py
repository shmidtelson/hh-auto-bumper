from __future__ import annotations


class ResumeEntity:
    STATUS_PUBLISHED = 'published'
    ACCESS_TYPE_BLACKLIST = 'blacklist'

    __id = None
    __updated = None
    __status = None
    __access_type = None

    @staticmethod
    def createFromResponse(response) -> ResumeEntity:
        entity = ResumeEntity()
        entity.setId(response.get('id'))
        entity.setUpdated(response.get('updated'))
        entity.setStatus(response.get('status').get('id'))
        entity.setStatus(response.get('access').get('type').get('id'))

        return entity

    def getId(self):
        return self.__id

    def setId(self, id) -> None:
        self.__id = id

    def getUpdated(self) -> str:
        return self.__updated

    def setUpdated(self, updated) -> None:
        self.__updated = updated

    def getStatus(self) -> str:
        return self.__status

    def setStatus(self, updated) -> None:
        self.__status = updated

    def getAccessType(self) -> str:
        return self.__access_type

    def setAccessType(self, updated) -> None:
        self.__access_type = updated
