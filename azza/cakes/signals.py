from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Cake
from .tasks import send_mail_task

@receiver(post_save, sender=Cake)
def advertisement_status_changed(sender, instance, **kwargs):

    if not instance.id:
        return

    old_instance = Cake.objects.get(id=instance.id)

    if old_instance.status != instance.status:
        print("Status changed")
        send_mail_task.delay(instance.id)



    """
    id=1
    title = Moka
    status = sold
    
    """


