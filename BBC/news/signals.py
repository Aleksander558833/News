from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from .models import Post

@receiver(m2m_changed, sender=Post)
def post_created(instance, **kwargs):
    if not kwargs ['action'] == 'post_add':
        return

    emails = User.objects.filter(
        subscriptions__Category__in=instance.PostCategory.all()
    ).values_list('email', flat=True)

    subject = f'Новая статья в категории {instance.PostCategory.all()}'

    text_content = (
        f'Статья: {instance.name_post}\n'
        f'Текст: {instance.text_post}\n\n'
        f'Ссылка на статью: http://127.0.0.1:8000{instance.get_absolute_url()}'
    )
    html_content = (
        f'Статья: {instance.name_post}<br>'
        f'Текст: {instance.text_post}<br><br>'
        f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
        f'Ссылка на статью</a>'
    )
    for email in emails:
        msg = EmailMultiAlternatives(subject, text_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()