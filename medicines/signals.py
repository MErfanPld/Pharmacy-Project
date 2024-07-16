from django.contrib.auth.signals import user_logged_out
from django.dispatch import receiver

@receiver(user_logged_out)
def clear_alerts_added(sender, request, user, **kwargs):
    if 'alerts_added' in request.session:
        del request.session['alerts_added']
