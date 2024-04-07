import sys
import datetime
import os.path
import json

from docassemble.base.util import get_config
from docassemble.base.error import DAException
from google.auth.transport.requests import Request
from google.oauth2 import service_account
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

__all__ = ['add_calendar', 'get_appointments', 'take_appointment']

SCOPES = ["https://www.googleapis.com/auth/calendar.readonly", "https://www.googleapis.com/auth/calendar"]

credential_json = get_config('google calendar service account', None)
if credential_json is None:
    credential_info = None
else:
    credential_info = json.loads(credential_json, strict=False)


def google_cloud_credentials():
    if credential_info is None:
        raise DAException("google calendar service account not defined in configuration")
    return service_account.Credentials.from_service_account_info(credential_info)


def add_calendar(calendar_id):
    service = build("calendar", "v3", credentials=google_cloud_credentials())
    service.calendarList().insert(body={'id': calendar_id}).execute()


def take_appointment(cal_id, event_id, name):
    try:
        service = build("calendar", "v3", credentials=google_cloud_credentials())
        event = service.events().get(calendarId=cal_id, eventId=event_id).execute()
        event['summary'] = name
        service.events().update(calendarId=cal_id, eventId=event_id, body=event).execute()
    except HttpError as error:
        raise DAException(f"An error occurred: {error}")


def get_appointments():
    appointments = []
    try:
        service = build("calendar", "v3", credentials=google_cloud_credentials())
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
        now = datetime.datetime.utcnow().isoformat() + "Z"
        for calendar in calendars:
            events_result = (
                    service.events()
                    .list(
                            calendarId=calendar['id'],
                            timeMin=now,
                            maxResults=50,
                            singleEvents=True,
                            orderBy="startTime",
                    )
                    .execute()
            )
            events = events_result.get("items", [])

            if not events:
                continue

            for event in events:
                start = event["start"].get("dateTime", event["start"].get("date"))
                end = event["end"].get("dateTime", event["end"].get("date"))
                if 'available' in event["summary"].lower():
                    appointments.append({'id': appt_count, 'event_id': event['id'], 'cal_id': calendar['id'], 'organization': calendar['name'], 'start': start, 'end': end})
                    appt_count += 1
    except HttpError as error:
        raise DAException(f"An error occurred: {error}")
    return appointments
