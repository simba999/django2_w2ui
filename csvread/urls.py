from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from .views import index, CsvReadFile

"""
    timely_backend/users URL Configuration
"""
app_name = "csvread"

urlpatterns = [
    url(r'^csv_index/$', index),
    url(r'^api/csv/$', CsvReadFile.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
