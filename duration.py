from datacenter.models import Visit
from django.utils.timezone import localtime

open_visits = Visit.objects.filter(leaved_at__isnull=True)

for visit in open_visits:
    entered_local = localtime(visit.entered_at)
    now_local = localtime()
    duration = now_local - entered_local

    print("Зашёл в хранилище, время по Москве:")
    print(entered_local)
    print()
    print("Находится в хранилище:")
    print(duration)
    print("-" * 30)
