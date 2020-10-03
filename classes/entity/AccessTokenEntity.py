from classes.utils.DateHelper import DateHelper


class AccessTokenEntity:
    __access_token: str = ''
    __refresh_token: str = ''
    __expires_in: int = 0
    __expires_at: int = 0

    def __init__(self, resp_dict):
        self.setAccessToken(resp_dict.get('access_token'))
        self.setRefreshToken(resp_dict.get('refresh_token'))
        self.setExpiresIn(resp_dict.get('expires_in'))
        self.setExpiresAt(DateHelper.getCurrentUnixDate() + resp_dict.get('expires_in'))

    def getAccessToken(self) -> str:
        return self.__access_token

    def setAccessToken(self, access_token: str) -> None:
        self.__access_token = access_token

    def getRefreshToken(self) -> str:
        return self.__refresh_token

    def setRefreshToken(self, refresh_token: str) -> None:
        self.__refresh_token = refresh_token

    def getExpiresIn(self) -> int:
        return self.__expires_in

    def setExpiresIn(self, expires_in: int) -> None:
        self.__expires_in = expires_in

    def getExpiresAt(self) -> int:
        return self.__expires_at

    def setExpiresAt(self, expires_at: int) -> None:
        self.__expires_at = expires_at
