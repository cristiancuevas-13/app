from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.saludo),
    path('pagina1/', views.pagina1, name="principal"),
    path('pagina2/', views.pagina2, name="secundario"),
]