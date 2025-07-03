from django.shortcuts import render
from datacenter.models import Passcard
from datacenter.models import Visit

def active_passcards_view(request):
    all_passcards = Passcard.objects.filter(is_active=True)
    context = {
        'active_passcards': all_passcards,
    }
    return render(request, 'active_passcards.html', context)

def is_visit_long(visit, minutes=60):
    duration = get_duration(visit)
    return duration.total_seconds() > minutes * 60
