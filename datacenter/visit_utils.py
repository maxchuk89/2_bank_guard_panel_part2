from django.utils.timezone import localtime
from datetime import timedelta

SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


def get_duration(visit):
    end_time = visit.leaved_at or localtime()
    return end_time - visit.entered_at


def format_duration(duration: timedelta) -> str:
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // SECONDS_IN_HOUR
    minutes = (total_seconds % SECONDS_IN_HOUR) // SECONDS_IN_MINUTE
    return f"{hours:02d}:{minutes:02d}"


def is_visit_long(visit, minutes=60):
    return get_duration(visit).total_seconds() > minutes * SECONDS_IN_MINUTE