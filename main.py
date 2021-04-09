import time

from dotenv import load_dotenv, find_dotenv
from classes.refresher import Refresher
from classes.utils.logger import logger

load_dotenv(find_dotenv())

if __name__ == "__main__":
    while True:
        logger.info('Server was started')
        client = Refresher()
        client.execute()
        time.sleep(60*5)
