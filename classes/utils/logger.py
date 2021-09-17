import logging
import sys
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.handler import LogstashFormatter

from classes.config import Config
config = Config()

logger = logging.getLogger('hh.bumper')
logger.setLevel(logging.INFO)

# STDOUT
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# LOGSTASH
if config.get_logstash_host() and config.get_logstash_host():
    logstash_handler = AsynchronousLogstashHandler(
        host=config.get_logstash_host(),
        port=config.get_logstash_port(),
        ssl_enable=False,
        ssl_verify=False,
        database_path=''
    )
    logstash_handler.setLevel(logging.ERROR)
    formatter = LogstashFormatter()
    logstash_handler.setFormatter(formatter)
    logger.addHandler(logstash_handler)


