import configparser
import os

# Go up 2 levels from utils/ to reach root, then into config/
config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'configuration', 'config.ini'))

configuration = configparser.RawConfigParser()
configuration.read(config_path)


class ReadConfig:
    @staticmethod
    def get_application_url():
        return configuration.get('common info', 'baseUrl')

    @staticmethod
    def get_user_mobile():
        return configuration.get('common info', 'mobile_number')

    @staticmethod
    def get_user_password():
        return configuration.get('common info', 'password')