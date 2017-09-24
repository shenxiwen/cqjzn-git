from django.conf.urls import url

from . import views
from django.conf.urls import url
from index.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]