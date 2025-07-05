from django.shortcuts import render
from datacenter.models import Visit
from django.utils.timezone import localtime
from datacenter.visit_utils import get_duration, format_duration

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
    return render(request, 'storage_information.html', {
        'non_closed_visits': non_closed_visits,
    })
