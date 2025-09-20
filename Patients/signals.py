from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Patient
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from django.forms.models import model_to_dict


@receiver(post_save, sender=Patient)
def send_patient_update(sender, instance, created, **kwargs):
    channel_layer = get_channel_layer()
    data = model_to_dict(instance)
    data["id"] = str(instance.id)

    async_to_sync(channel_layer.group_send)(
        "patients",
        {
            "type": "patient_update",  # must match Consumer method
            "patient": data,
        },
    )