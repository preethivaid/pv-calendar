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
        event_created = self.service.events().quickAdd(
            calendarId='primary',
            text=event_text).execute()

        if 'summary' in event_created:
            if 'date' in event_created['start']:
                date_type = 'date'
            else:
                date_type = 'dateTime'
            start_time = dateparser.parse(event_created['start'][date_type]).strftime("%-I:%M %p")
            end_time = dateparser.parse(event_created['end'][date_type]).strftime("%-I:%M %p")
            start_date = dateparser.parse(event_created['start'][date_type]).strftime("%A %B %d, %Y")

        response_text = "Created event '{}' from {} - {} on {}".format(event_created['summary'],
                                                                       start_time,
                                                                       end_time,
                                                                       start_date)
        return response_text

    def get_summary(self, request_text):
        """
        Builds a summary text of the events for a given day
        """
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

            calendar_summary_text = "------------------------"
            calendar_summary_text += '\n' + "Summary for:" \
                                            " {}".format(dateparser.parse(time_range_min).strftime("%A %B %d, %Y"))
            for index, event in enumerate(events['items']):
                if 'summary' in event:
                    if 'date' in event['start']:
                        date_type = 'date'
                    else:
                        date_type = 'dateTime'
                    start_time = dateparser.parse(event['start'][date_type]).strftime("%-I:%M %p")
                    end_time = dateparser.parse(event['end'][date_type]).strftime("%-I:%M %p")

                    calendar_summary_text += '\n\n' + "{}. {}, from  " \
                                                      "{} - {}".format(index, event['summary'], start_time, end_time)
            calendar_summary_text += '\n' + "------------------------"
            page_token = events.get('nextPageToken')
            if not page_token:
                break
        return calendar_summary_text
