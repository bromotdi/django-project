from django.urls import path
from . import views

# привязка функции-вида к определенному маршруту
app_name = "home"

urlpatterns = [
    path('', views.index, name='index'),
]