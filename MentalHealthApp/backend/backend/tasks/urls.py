from django.urls import path
from .views import CompareClean

urlpatterns = [
    path('compare-clean/', compare_clean.as_view(), name='compare-clean'),
]
