import time

from dotenv import load_dotenv, find_dotenv
from classes.refresher import Refresher
from classes.utils.logger import logger

load_dotenv(find_dotenv())

if __name__ == "__main__":
    logger.info('Server was started')

    while True:
        client = Refresher()
        client.execute()
        logger.info('Wait next iteration')
        time.sleep(15)
        # time.sleep(60*5)
