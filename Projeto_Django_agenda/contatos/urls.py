from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:contato_id>', views.show_contato_id, name='show_contato_id'),
    path('busca/', views.busca, name='busca')
]
