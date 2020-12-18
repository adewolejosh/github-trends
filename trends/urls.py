
from django.urls import path

from .views import *

urlpatterns = [
    path('', GithubTrendsView.as_view(), name="github-trends")
]
