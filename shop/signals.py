from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import OrderItem, Order

@receiver(post_save, sender=OrderItem)
def triggerDis(sender, instance, created, **kwargs):
    #print("TRIGGERED")
    o = Order.objects.get(id=instance.order_id)
    if instance.quantity > 3:
        o.total -= (0.2*o.total)
        o.save()
        print("TOTAL: " , o.total)
        print("TOTAL: " , o)