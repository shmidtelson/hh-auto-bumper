import time
import locale

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from classes.refresher import Refresher
from classes.utils.logger import logger


locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

if __name__ == "__main__":
    logger.info('Server was started')

    while True:
        client = Refresher()
        client.execute()
        logger.info('Wait next iteration')
        time.sleep(60*5)
