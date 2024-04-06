#! /usr/bin/env python3
import sys
import datetime
import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# This requires credentials in a gcal.json file. Jonathan Pyle can share this file with you.

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly", "https://www.googleapis.com/auth/calendar"]


def main():
    creds = service_account.Credentials.from_service_account_file('gcal.json')

    try:
        service = build("calendar", "v3", credentials=creds)
        # This is how you add a calendar; you need its ID first.
        # calendar_list_entry = {
        #     'id': 'bd307a187fd372df1f3456059ed7ecb3678d82b2e65b389900b91a510b17f58d@group.calendar.google.com'
        # }
        # created_calendar_list_entry = service.calendarList().insert(body=calendar_list_entry).execute()
        # get a list of calendars
        calendars = []
        page_token = None
        while True:
            calendar_list = service.calendarList().list(pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                calendars.append({'id': calendar_list_entry['id'], 'name': calendar_list_entry['summary']})
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break
        appt_count = 1
        appointments = []
        now = datetime.datetime.utcnow().isoformat() + "Z"    # 'Z' indicates UTC time
        for calendar in calendars:
            events_result = (
                    service.events()
                    .list(
                            calendarId=calendar['id'],
                            # timeMin=now,
                            maxResults=10,
                            singleEvents=True,
                            orderBy="startTime",
                    )
                    .execute()
            )
            events = events_result.get("items", [])

            if not events:
                print("No upcoming events found.")
                continue

            # Prints the start and name of the next 10 events
            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                end = event["end"].get("dateTime", event["end"].get("date"))
                if 'available' in event["summary"].lower():
                    appointments.append({'id': appt_count, 'organization': calendar['name'], 'start': start, 'end': end})
                    appt_count += 1
        print(json.dumps(appointments))
    except HttpError as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
