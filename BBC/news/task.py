from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
from django.http import HttpResponse
from django.views import View

from .models import *
import datetime
import time


@shared_task
def post_created(pk):

    post = Post.objects.get(id=pk)
    categories = post.categories_post.all()

    emails = User.objects.filter(
            subscriptions__category__in=categories
        ).values_list('email', flat=True)

    emails = set(emails)

    subject = f'Новая статья в категории {', '.join([f'{i}' for i in categories])}'

    html_content = (
            f'Название: {post.name_post}<br>'
            f'<a href="http://127.0.0.1{post.get_absolute_url()}">'
            f'Ссылка на пост</a>'
        )
    for email in emails:
        print('email ', email)
        msg = EmailMultiAlternatives(subject, html_content, None, [email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()

@shared_task
def send_mail_weekly():
    one_week_later = datetime.datetime.now() - datetime.timedelta(weeks=1)
    post = Post.objects.filter(dateCreation__gt=one_week_later)
    category = set(post.values_list('PostCategory', flat=True))
    subscribers = set(Subscription.objects.filter(category__in=category).values_list('user__email', flat=True))

    html_content = render_to_string(
        'daily_post.html',
        {
            'link': f'http://127.0.0.1:8000',
            'posts': Post
        }
    )

    msg = EmailMultiAlternatives(
        subject="Новости недели",
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers
    )

    msg.attach_alternative(html_content, "text/html")
    msg.send()