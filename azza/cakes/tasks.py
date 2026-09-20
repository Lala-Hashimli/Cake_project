from celery import shared_task
from .utils import send_mail
from datetime import timedelta
from django.utils import timezone
from django.conf import settings

from .models import Cake


@shared_task # celery taski
def send_mail_task(id):
    cake = Cake.objects.get(id=id)
    
    send_mail(
        subject="Add status",
        message="Status changed",
    )


@shared_task
def check_expire():
    now = timezone.now()

    past_time = now - timedelta(
        seconds=settings.CAKE_TTL
    )

    cakes = Cake.objects.filter(
        created_at__lte=past_time,
        status="active",
    )

    print("NOW:", now)
    print("PAST TIME:", past_time)
    print("FOUND CAKES:", cakes.count())

    updated = cakes.update(status="expired")

    print("EXPIRED:", updated)
    
    

    