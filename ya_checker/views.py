from django.conf import settings
from django.http import JsonResponse
from django.views.generic import View

from .utils import clear_database_info, get_package_list


class CheckerView(View):

    def get(self, request, *args, **kwargs):
        result = {
            'BASE_DIR': settings.BASE_DIR,
            'DEBUG': settings.DEBUG,
            'INSTALLED_APPS': settings.INSTALLED_APPS,
            'DATABASES': clear_database_info(settings.DATABASES),
            'PACKAGE_LIST': get_package_list()
        }
        return JsonResponse(result)
