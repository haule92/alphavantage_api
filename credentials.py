import configparser
from pathlib import Path


class Credentials:
    """
    Credentials class to read the credentials for different of accounts, emails, apis or databases
    This information is usually stored locally and gitignored in the repo under the name 'config.ini'
    """
    # the parents of the ROOT DIR depend on the class Credentials is defined.
    ROOT_DIR = Path(__file__).parents[0]
    # the same for the .joinpath(), depending on where the 'config.ini' is placed.
    CONFIG_FILENAME = ROOT_DIR.joinpath('config.ini')

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read(self.CONFIG_FILENAME)

    def credentials_api_something3(self):
        definition = 'ALPHAVANTAGE_PAU'
        credential_dict = {
            'email': self.config[definition]['email'],
            'api_key': self.config[definition]['api_key'],
        }
        setattr(self, definition, credential_dict)
