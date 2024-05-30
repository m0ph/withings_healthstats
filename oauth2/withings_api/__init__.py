# from https://github.com/withings-sas/api-oauth2-python/blob/master/src/withings_api_example/__init__.py
import os.path

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import SafeConfigParser as ConfigParser

config = ConfigParser()
DEFAULT_CONFIG_FILES = []

LOCAL_CONFIG_PATH = os.path.join(
    os.path.dirname(os.path.dirname(os.path.dirname(
        os.path.realpath(__file__)
    ))),
    "user.conf"
)

config.read(DEFAULT_CONFIG_FILES + [LOCAL_CONFIG_PATH])