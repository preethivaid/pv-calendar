from __future__ import print_function
import os

import oauth2client
from oauth2client import client
from oauth2client import tools

from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


class GetCredentials:

    @staticmethod
    def get_credentials():
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join(home_dir, '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir,
                                       'pv-calendar.json')

        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:

            tmp_secret_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'google_api_secret.json')
            with open(tmp_secret_file, 'w+') as api_file:
                api_file.write(os.getenv('GOOGLE_API_SECRET'))
            flow = client.flow_from_clientsecrets(tmp_secret_file, SCOPES)
            os.remove(tmp_secret_file)
            flow.user_agent = APPLICATION_NAME
        return credentials
