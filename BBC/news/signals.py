from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from .models import PostCategory
from .task import post_created

@receiver(m2m_changed, sender=PostCategory)
def post_created_signals(instance, **kwargs):
    if not kwargs['action'] == 'post_add':
        post_created.delay(instance.id)

    # emails = User.objects.filter(
    #     subscriptions__category__in=instance.category.all()
    # ).values_list('email', flat=True)
    #
    # subject = f'Новая статья в категории {instance.category.all()}'
    #
    # text_content = (
    #     f'Статья: {instance.title}\n'
    #     f'Ссылка на статью: http://127.0.0.1:8000{instance.get_absolute_url()}'
    # )
    # html_content = (
    #     f'Статья: {instance.title}<br>'
    #     f'<a href="http://127.0.0.1:8000{instance.get_absolute_url()}">'
    #     f'Ссылка на статью</a>'
    # )
    # for email in emails:
    #     msg = EmailMultiAlternatives(subject, text_content, None, [email])
    #     msg.attach_alternative(html_content, "text/html")
    #     msg.send()