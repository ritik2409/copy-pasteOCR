from django.urls import path, include
from .views import (
    InvoiceView, 
)

urlpatterns = [
    path('file/', InvoiceView.as_view()),
]