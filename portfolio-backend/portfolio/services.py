"""Services utilitaires."""
import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)


def send_contact_notification(contact_message):
    """
    Envoie un email à l'administrateur du portfolio lorsqu'un message de contact est reçu.
    """
    from .models import Profile

    profile = Profile.objects.filter(is_active=True).first()
    recipient = profile.email if profile else getattr(
        settings, 'CONTACT_RECIPIENT_EMAIL', 'gracemahouk@gmail.com'
    )

    subject = f"[Portfolio] {contact_message.subject}"
    message = f"""
Nouveau message depuis le formulaire de contact :

De : {contact_message.name} <{contact_message.email}>
Sujet : {contact_message.subject}

Message :
{contact_message.message}

---
Enregistré le : {contact_message.created_at}
"""
    try:
        send_mail(
            subject=subject,
            message=message.strip(),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[recipient],
            fail_silently=False,
        )
        logger.info(f"Email envoyé à {recipient} pour le message: {contact_message.subject}")
    except Exception as e:
        logger.exception(f"Erreur envoi email à {recipient}: {e}")
