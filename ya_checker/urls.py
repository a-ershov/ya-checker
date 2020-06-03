from django.urls import path

from .views import CheckerView

app_name = 'checker'

urlpatterns = [
    path('', CheckerView.as_view(), name='detail'),
]
