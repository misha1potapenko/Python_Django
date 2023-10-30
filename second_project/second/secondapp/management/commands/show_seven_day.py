from datetime import datetime, date, time, timedelta
from django import template
from django.core.management import BaseCommand
from django.db.models import Count, Q
from django.utils import timezone

from secondapp.models import Order, User

register = template.Library()

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # получаем текущую дату и время в формате datetime
        now = timezone.now()
        # вычисляем дату начала дня (00:00) 7 дней назад
        start_date = now - timedelta(days=7)
        # вычисляем дату начала текущего дня (00:00)
        today_start = timezone.make_aware(datetime.combine(date.today(), time.min))
        # получаем все статьи и количество их просмотров за последние 7 дней
        articles = Order.objects.annotate(
            total_view_count=Count('date_ordered', filter=Q(date_ordered__viewed_on__gte=start_date)),
            today_view_count=Count('date_ordered', filter=Q(date_ordered__viewed_on__gte=today_start))
        ).prefetch_related('date_ordered')
        # сортируем статьи по количеству просмотров в порядке убывания, сначала по просмотрам за сегодня, затем за все время
        popular_articles = articles.order_by('-total_view_count', '-today_view_count')[:10]
        self.stdout.write(popular_articles)