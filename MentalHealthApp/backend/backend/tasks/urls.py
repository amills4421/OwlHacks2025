from django.urls import path
from .views import CompareClean

urlpatterns = [
    path('compare-clean/', CompareClean.as_view(), name='compare-clean'),
]
