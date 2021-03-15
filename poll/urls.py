from django.urls import path, include
from . import views


app_name = 'poll'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>/', views.question_detail, name="question_detail"),
    path('<int:question_id>/answers/', views.results, name="results"),
    path('<int:question_id>/vote/', views.vote, name="vote"),
]

