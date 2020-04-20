'''from django.contrib.auth.models import AbstarctUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from crm.ServiceLevelAgreement.models import SLA

@receiver(post_save,sender=SLA)
def generate_ticket (sender,instance,created,**kwargs):
    if created:
        SLA.objects.create(SLA=instance)

@receiver(post_save,sender=SLA)
def save_ticket(sender,instance,**kwargs):
    instance.SLA.save()


