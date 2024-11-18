from django.urls import path, include
from .views import HelloAPI, bookAPI, booksAPI, BookAPI, BooksAPI, BooksAPIMixins, BookAPIMixins, BookViewSet
from rest_framework import routers

urlpatterns = [
    #path("hello/", HelloAPI),
    path('hello/', HelloAPI.as_view()), #클래스 / path 등록할 떄 .as_view() 사용
    path("fbv/books/", booksAPI),
    path("fbv/book/<int:bid>/", bookAPI),
    path("cbv/books/", BooksAPI.as_view()),
    path("cbv/book/<int:bid>/", BookAPI.as_view()),
    path("mixin/books/", BooksAPIMixins.as_view()),
    path("mixin/book/<int:bid>/", BookAPIMixins.as_view()),
]

router = routers.SimpleRouter()
router.register('books', BookViewSet)

urlpatterns = router.urls