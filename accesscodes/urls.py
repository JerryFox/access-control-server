from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'6eebabbeba3f162859636d349a3e74fd9cbeff5c/dump_codes.json', views.dump_codes, name='dump-codes'),
]

