import pytz

from django.utils import timezone

class TimeZoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get('django_timezone') # Пытаемся забрать часовой пояс из сессии,
# Если есть, то выставляем его, если нет то выставляем часовой пояс по умолчанию (часовой пояс сервера)

        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)
