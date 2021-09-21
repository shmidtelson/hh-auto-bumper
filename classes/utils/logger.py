import logging
import logging_loki
import sys


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
if config.get_loki_host() and config.get_loki_pass() and config.get_loki_user():
    handler = logging_loki.LokiHandler(
        url=config.get_loki_host(),
        tags={"application": "hh.bumper"},
        auth=(config.get_loki_user(), config.get_loki_pass()),
        version="1",
    )

    logger.addHandler(handler)
