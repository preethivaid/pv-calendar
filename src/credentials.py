from __future__ import print_function
import os

import oauth2client
from oauth2client import client, tools

import io
import tempfile
from dotenv import load_dotenv
from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class GetCredentials:

    @staticmethod
    def get_credentials():
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        temp_file_name = tempfile.NamedTemporaryFile().name
        with open(temp_file_name, 'a+') as api_temp_file:
            api_temp_file.write(os.getenv('GOOGLE_CAL_AUTH'))
            api_temp_file.seek(0)
            store = oauth2client.file.Storage(temp_file_name)
            api_temp_file.close()
        credentials = store.get()
        return credentials
