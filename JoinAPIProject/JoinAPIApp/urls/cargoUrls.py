from django.urls import path
from ..views import cargoViews

urlpatterns = [
    path('', cargoViews.getAllCargos),
    path('getById/<str:id>/', cargoViews.getCargoById),
    path('insert/', cargoViews.addCargo),
    path('update/<str:id>/', cargoViews.updateCargo),
    path('delete/<str:id>/', cargoViews.deleteCargo)
]