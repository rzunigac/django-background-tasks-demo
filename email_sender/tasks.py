from django.core.mail import send_mail
from background_task import background


@background(schedule=10)
def send_email_task():
    send_mail(
        'Subject here',
        'Here is the message.',
        'from@example.com',
        ['to@example.com'],
        fail_silently=False
    )
