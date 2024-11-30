from django.urls import path
from ..views import views

urlpatterns = [
    path('question1', views.question1),
    path('question2/<int:value>', views.question2),
    path('question3', views.question3),
    path('question4a', views.question4a),
    path('question4b', views.question4b),
    path('question4c', views.question4c)
]