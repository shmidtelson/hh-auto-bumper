import logging
import logging.handlers as handlers
from classes.Config import Config

logger = logging.getLogger('app')
logger.setLevel(logging.INFO)

## Here we define our formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
config = Config()

logHandler = handlers.TimedRotatingFileHandler(config.getAppPath() + '/var/log/app.log', when='M', interval=1,
                                               backupCount=2)
logHandler.setLevel(logging.INFO)
## Here we set our logHandler's formatter
logHandler.setFormatter(formatter)

logger.addHandler(logHandler)
