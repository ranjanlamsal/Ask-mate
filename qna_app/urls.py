from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from qna_app import views


urlpatterns = [
    path('view/',views.question),
]
