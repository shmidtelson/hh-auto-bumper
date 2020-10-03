from datetime import datetime


class DateHelper:

    @staticmethod
    def getCurrentUnixDate() -> int:
        return int(datetime.now().timestamp())
