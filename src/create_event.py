from __future__ import print_function

from pathlib import Path

import httplib2
from apiclient import discovery
from dotenv import load_dotenv

from src.credentials import GetCredentials as Cred

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class CreateEvent:

    @staticmethod
    def create_event(event_text):
        """
        Creates a Google Calendar event based on human readable text input.
        """
        credentials = Cred.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)

        service.events().quickAdd(
            calendarId='primary',
            text=event_text).execute()
