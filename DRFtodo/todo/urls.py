from django.urls import path

from .views import TodosAPIView, TodoAPIView, DoneTodosAPIView, DoneTodoAPIView

urlpatterns = [
    path('todo/', TodosAPIView.as_view()),
#상세 조회 뷰 url 연결
    path('todo/<int:pk>/', TodoAPIView.as_view()),
#완료 뷰 URL 연결
    path('done/', DoneTodosAPIView.as_view()),
    path('done/<int:pk>/', DoneTodoAPIView.as_view()),
]  
