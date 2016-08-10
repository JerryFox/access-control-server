from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'accesscodes'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'6eebabbeba3f162859636d349a3e74fd9cbeff5c/dump_codes.json', views.dump_codes, name='dump-codes'),
    url(r"get_code", views.get_code, name="get-code"),
    url(r"finished", TemplateView.as_view(template_name='accesscodes/finished.html'), name="finished"),
]

