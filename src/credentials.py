from __future__ import print_function
import os

import oauth2client
from oauth2client import client

import io
import tempfile
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
        credential_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'pv-calendar-credentials.json')

        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:

            with tempfile.NamedTemporaryFile() as api_temp_file:
                api_temp_file.write(io.StringIO(os.getenv('GOOGLE_API_SECRET')))
                flow = client.flow_from_clientsecrets(api_temp_file, SCOPES)
                api_temp_file.close()
            flow.user_agent = APPLICATION_NAME
        return credentials
