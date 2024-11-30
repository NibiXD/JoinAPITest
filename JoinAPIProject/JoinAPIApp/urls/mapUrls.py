from django.urls import path
from ..views import templateViews

urlpatterns = [
    path('', templateViews.getMapTemplate),
    path('getAllLocations/', templateViews.getAllLocations),
    path('createLocation/', templateViews.createLocation),
    path('updateLocation/<int:id>', templateViews.updateLocation),
    path('deleteLocation/<int:id>', templateViews.deleteLocation)
]