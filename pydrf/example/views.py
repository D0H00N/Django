from rest_framework import viewsets,permissions,generics, status,mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404 # get_object_or_404 불로오기


from .models import Book                              # 모델 불러오기
from .serializers import BookSerializer               # 시리얼라이저 불러오기

#뷰: 클라이언트 요청 처리, 필요한 데이터 반환 기능,API 엔드포인트로 사용자 맞춤 데이터 제공
#데코레이터 : 함수에 대한 성격(스타일)을 표시해주는 표기법,함수를 감싼다.
#HelloAPI 함수가 GET 요청을 받을 수 있는 API이다! -> @api_view 표기
#FBV
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world")
#CBV
class HelloAPI(APIView):
    def get(self, request, format=None):
        return Response("hello world")
    
#FBV 
@api_view(['GET', 'POST'])
def booksAPI(request):
    if request.method == 'GET': # GET 요청(도서전체정보)
        books = Book.objects.all() #Book 모델로부터 전체데이터 가져오기
        serializer = BookSerializer(books, many=True) #시리얼라이저에 전체 데이터를 한번에 집어넣기(직렬화,many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST': #POST 요청
        serializer = BookSerializer(data=request.data) #POST 요청으로 들어온 데이터를 시리얼라이저에 집어넣기
        if serializer.is_valid(): #유효한 데이터라면?
            serialize.save() #역직렬화를 통해, 모델시리얼라이저의 기본 create()함수가 동작
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])             
def bookAPI(request, bid): # book/bid/
    book = get_object_or_404(Book, bid=bid) #bid=id인 데이터를 Book에서 가져오고, 없으면 404 에러
    serializer = BookSerializer(book) #데이터 집어넣기 직렬화 
    return Response(serializer.data, status=status.HTTP_200_OK)

#CBV
class BooksAPI(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BookAPI(APIView):
    def get(self, request, bid):
        book = get_object_or_404(Book, bid=bid)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)

#mixins
class BooksAPIMixins(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):  # 목록조회
        return self.list(request, *args, **kwargs) 
    
    def post(self, request, *args, **kwargs):  # 도서정보추가
        return self.create(request, *args, **kwargs)
    
class BookAPIMixins(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'

    def get(self, request, *args, **kwargs):  # 조회 retrieve
        return self.retrieve(request, *args, **kwargs) 
    def put(self, request, *args, **kwargs):  # 수정 update
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):  # 삭제 destroy
        return self.destroy(request, *args, **kwargs)
    
class BooksAPIGenerics(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookAPIGenerics(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'bid'

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
