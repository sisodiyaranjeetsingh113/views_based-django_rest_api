from rest_framework.response import Response
from django.shortcuts import render
from django.http.response import JsonResponse
from .models import Tile
from .serializers import TileSerializer
from rest_framework.decorators import api_view
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
@api_view(['GET'])
def taskList(request):
    task=Tile.objects.all()
    if task is None:
        JsonResponse("No records")
    else:
      serializer=TileSerializer(task,many=True)
    return JsonResponse({'result':serializer.data},safe=False)
@api_view(['GET'])
def taskDetail(request,pk):
    task=Tile.objects.get(id=pk)
    serializer=TaskSerializer(task,many=True)
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def taskCreate(request):
    serializer=TileSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return JsonResponse(serializer.data,safe=False)
@api_view(['POST'])
def taskUpdate(request,pk):
    task=Tile.objects.get(id=pk)
    serializer=TileSerializer(instance=task,data=request.data)
    return JsonResponse(serializer.data,safe=False)
@api_view(['DELETE'])
def taskDelete(request,pk):
    task=Tile.objects.get(id=pk)
    serializer=TileSerializer(task,many=True)
    return JsonResponse("Deleted")
