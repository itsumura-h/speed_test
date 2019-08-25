from django.urls import path, include
from app.controllers.sample_controller import SampleController


app_urls = [
    path('fib/<str:num>/', SampleController.fib)
]

