from rest_framework import serializers
from .models import Todo

#Todo 전체 조회 시리얼라이저( '__all__' )
class TodoSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'complete', 'important')
                    #제목,완료 여부,중요 여부
# 상세 조회용
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description','created', 'complete', 'important')
                    
# 생성용
class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'important')
                    