from django.urls import path

from . import views

urlpatterns = [
    path('/<slug:label>/', views.chat_room)

]
