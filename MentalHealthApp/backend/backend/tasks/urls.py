from django.urls import path
from .views import compare_clean, suggest_clean

urlpatterns = [
    path('compare-clean/', compare_clean.as_view(), name='compare-clean'),
    path("suggest-clean/", suggest_clean, name="suggest_clean"),
]
