from __future__ import print_function

from pathlib import Path

import httplib2
from apiclient import discovery
from dotenv import load_dotenv

import datetime
import dateparser
import pytz

from src.credentials import GetCredentials as Cred

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class CalendarHandler:

    def __init__(self):
        credentials = Cred.get_credentials()
        http = credentials.authorize(httplib2.Http())
        self.service = discovery.build('calendar', 'v3', http=http)

    def create_event(self, event_text):
        """
        Creates a Google Calendar event based on human readable text input.
        """
        self.service.events().quickAdd(
            calendarId='primary',
            text=event_text).execute()

    def get_summary(self, request_text):
        # Parse the date text
        requested_date_text = request_text.split(' ', 1)[1]
        requested_date = dateparser.parse(requested_date_text)
        # Set the clock back to midnight
        requested_date.replace(hour=0, minute=0, second=0, microsecond=0)
        # Get the date summary
        page_token = None
        while True:
            time_range_min = pytz.UTC.localize(requested_date).isoformat()
            time_range_max = pytz.UTC.localize(requested_date + datetime.timedelta(days=1)).isoformat()
            events = self.service.events().list(calendarId='primary',
                                                timeMax=time_range_max,
                                                timeMin=time_range_min,
                                                pageToken=page_token).execute()
            print("--------------------------------------")
            print("Summary for: {}".format(time_range_min))
            for index, event in enumerate(events['items']):
                if 'summary' in event:
                    start_time_field = event['start']
                    end_time_field = event['end']
                    if 'date' in start_time_field:
                        start_time = dateparser.parse(start_time_field['date'])
                        end_time = dateparser.parse(end_time_field['date'])
                    else:
                        start_time = dateparser.parse(start_time_field['dateTime'])
                        end_time = dateparser.parse(end_time_field['dateTime'])

                    print("{}. {}, Start: {}, End: {}".format(index, event['summary'], start_time, end_time))
            print("--------------------------------------")
            page_token = events.get('nextPageToken')
            if not page_token:
                break
