import logging
import sys

from classes.config import Config

logger = logging.getLogger('app')
logger.setLevel(logging.INFO)


handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
config = Config()
