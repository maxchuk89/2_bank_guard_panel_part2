from django.utils.timezone import localtime
from datetime import timedelta

def get_duration(visit):
    end_time = visit.leaved_at or localtime()
    return end_time - visit.entered_at

def format_duration(duration: timedelta) -> str:
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours:02d}:{minutes:02d}"

def is_visit_long(visit, minutes=60):
    return get_duration(visit).total_seconds() > minutes * 60