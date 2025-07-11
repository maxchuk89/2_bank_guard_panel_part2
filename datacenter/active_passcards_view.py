from django.shortcuts import render
from datacenter.models import Passcard

def active_passcards_view(request):
    active_passcards = Passcard.objects.filter(is_active=True)
    return render(request, 'active_passcards.html', {
        'active_passcards': active_passcards,
    })
