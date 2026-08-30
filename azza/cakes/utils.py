from django.conf import settings
from django.core.mail import EmailMultiAlternatives

def send_mail(subject, message):
    email = EmailMultiAlternatives(
        subject=subject,
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=["lalahashimli06@gmail.com", 
            "heyderli.seide2509@gmail.com",
            "zumrudjfl@gmail.com"],
    )

    html_message = f"""
    <h2>Cake created!</h2>

    <p>{message}</p>

    <a href="https://youtu.be/iK3MMmGu53U?si=tvjQQ2E3hl-Pckt_">
        Watch the tutorial on YouTube
    </a>
    """

    email.attach_alternative(html_message, "text/html")
    email.send(fail_silently=False)
