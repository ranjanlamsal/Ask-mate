from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from qna_app import views
from .views import QuestionListView
app_name = 'qna'


urlpatterns = [
    # path('add',views.question, name='add'),
    path('read/', views.question,name='read'),
    path('create/', views.add_question, name='create'),
    path('list/', views.list_question, name= 'list'),
    path('update/<int:id>/', views.update_question, name='update'),
    path('delete/<int:id>/', views.delete_question, name='delete'),
    path('vote_qn/<int:id>/', views.vote_question,name='vote'),
    path('listview/', QuestionListView.as_view(), name='list')
]
