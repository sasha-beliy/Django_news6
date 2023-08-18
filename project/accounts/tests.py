from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from news.models import News, Category
from news.signals import *
from celery import shared_task

@shared_task
def send_notifications(preview, pk, title, subscribers):...

@shared_task
def weekly_notification():
    today = datetime.now()
    last_week = today - timedelta(days=7)
    posts = Post.objects.filter(dateCreation__gte=last_week)
    categories = set(posts.values_list("category__name", flat=True))
    html_content = render_to_string(
        "weekly_post.html",
        {
            "link": settings.SITE_URL,
            "posts": posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject="Посты за неделю",
        body="",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()



