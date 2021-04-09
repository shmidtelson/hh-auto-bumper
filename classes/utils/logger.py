import logging
from classes.config import Config

logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

## Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
config = Config()
