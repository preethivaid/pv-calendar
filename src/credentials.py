from __future__ import print_function
import os

import oauth2client
import tempfile

from oauth2client import client
from oauth2client import tools
SCOPES = 'https://www.googleapis.com/auth/calendar'
this_dir = os.path.dirname(os.path.realpath(__file__))
CLIENT_SECRET_FILE = os.path.join(this_dir, 'client_secret.json')
APPLICATION_NAME = 'pv-calendar'


class GetCredentials:

    def get_credentials(self, auth_key):
        """Gets valid user credentials from storage.

        If nothing has been stored, or if the stored credentials are invalid,
        the OAuth2 flow is completed to obtain the new credentials.

        Returns:
            Credentials, the obtained credential.
        """
        temp_file_name = tempfile.NamedTemporaryFile().name
        store = None
        if auth_key:
            with open(temp_file_name, 'a+') as api_temp_file:
                api_temp_file.write(auth_key)
                api_temp_file.seek(0)
                store = oauth2client.file.Storage(temp_file_name)
                api_temp_file.close()
            credentials = store.get()
        else:
            flow = client.flow_from_clientsecrets(CLIENT_SECRET_FILE, SCOPES)
            flow.user_agent = APPLICATION_NAME
            credentials = tools.run_flow(flow, store)
        return credentials
