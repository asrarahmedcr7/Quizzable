from django.urls import path
from . import views
urlpatterns = [
    path('', views.index.as_view(), name="index"),
    path('/<int>:pk/quiz', views.quiz.as_view(), name="quiz"),
    path('/<int>:pk/result', views.result.as_view(), name="result"),
]