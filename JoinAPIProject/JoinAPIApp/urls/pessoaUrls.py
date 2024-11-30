from django.urls import path
from ..views import views

urlpatterns = [
    path('', views.getAllPessoas),
    path('getById/<str:id>/', views.getPessoaById),
    path('insert/', views.addPessoa),
    path('update/<str:id>/', views.updatePessoa),
    path('delete/<str:id>/', views.deletePessoa)
]