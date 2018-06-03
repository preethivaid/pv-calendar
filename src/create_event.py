from __future__ import print_function

from pathlib import Path

import httplib2
from apiclient import discovery
from dotenv import load_dotenv

from src.credentials import GetCredentials as Cred

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# If modifying these scopes, delete your previously saved credentials
# at ~/.credentials/calendar-python-quickstart.json
SCOPES = 'https://www.googleapis.com/auth/calendar'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'


class CreateEvent:

    def event_prompt(self):
        summary_input = input("Event summary: ")
        self.create_event(summary_input)

    @staticmethod
    def create_event(summary):
        """Shows basic usage of the Google Calendar API.

        Creates a Google Calendar API service object and outputs a list of the next
        10 events on the user's calendar.
        """
        credentials = Cred.get_credentials()
        http = credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)

        event = {
            'summary': summary,
            'location': '800 Howard St., San Francisco, CA 94103',
            'description': 'Preethi Test Event.',
            'start': {
                'dateTime': '2018-06-04T09:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
            },
            'end': {
                'dateTime': '2018-06-04T17:00:00-07:00',
                'timeZone': 'America/Los_Angeles',
            },
            'recurrence': [
                'RRULE:FREQ=DAILY;COUNT=1'
            ],
            'attendees': [
                {'email': 'tyler@example.com'},
            ],
            'reminders': {
                'useDefault': False,
                'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                ],
            },
        }

        event = service.events().insert(calendarId='primary', body=event).execute()
        print('Event created: %s' % (event.get('htmlLink')))


if __name__ == '__main__':
    CreateEvent().event_prompt()
