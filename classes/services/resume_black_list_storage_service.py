import pickle
from typing import Set

from classes.config import Config


class ResumeBlackListStorageService:
    BLACK_LIST_PATH = '/var/black_list.pickle'

    config = None

    def __init__(self):
        self.config = Config()

    def set(self, listIds: Set):
        with open(self.config.getAppPath() + self.BLACK_LIST_PATH, 'wb') as file:
            pickle.dump(listIds, file)

    def get(self) -> Set:
        try:
            with open(self.config.getAppPath() + self.BLACK_LIST_PATH, 'rb') as file:
                listIds = pickle.load(file)
        except:
            with open(self.config.getAppPath() + self.BLACK_LIST_PATH, 'wb') as file:
                pickle.dump(set(), file)
            return self.get()

        return listIds
