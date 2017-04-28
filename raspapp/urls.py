from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from raspapp import views

urlpatterns = [

    url(r'test/', views.Test)
]

urlpatterns = format_suffix_patterns(urlpatterns)
