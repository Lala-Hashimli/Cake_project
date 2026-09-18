from celery import shared_task
from .utils import send_mail

from .models import Cake


@shared_task # celery taski
def send_mail_task(id):
    cake = Cake.objects.get(id=id)
    
    send_mail(
        subject="Add status",
        message="Status changed",
    )

    
    

    