from django.shortcuts import render
from datacenter.models import Passcard
from datacenter.models import Visit
from django.utils.timezone import localtime
from datetime import timedelta


def get_duration(visit):
    end_time = visit.leaved_at or localtime()
    # Конвертируем время входа и выхода в локальное
    entered = visit.entered_at
    return end_time - entered


def format_duration(duration: timedelta) -> str:
    total_seconds = int(duration.total_seconds())
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    return f"{hours:02d}:{minutes:02d}"


def storage_information_view(request):
    open_visits = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []
    for visit in open_visits:
        entered_local = localtime(visit.entered_at)
        duration = get_duration(visit)
        non_closed_visits.append({
            'who_entered': visit.passcard.owner_name,
            'entered_at': entered_local.strftime('%d-%m-%Y %H:%M'),
            'duration': format_duration(duration),
        })
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
