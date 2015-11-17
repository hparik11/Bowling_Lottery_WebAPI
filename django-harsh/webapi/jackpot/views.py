# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.utils import timezone
from jackpot.models import Bowler
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from jackpot.serializers import BowlerSerializer





@api_view(['GET', 'POST'])
def bowler_list(request, format=None):
    """
    List all Bowlers, or create a new snippet.
    """
    if request.method == 'GET':
        bowlers = Bowler.objects.all()
        serializer = BowlerSerializer(bowlers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BowlerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def bowler_detail(request, pk, format=None):
    """
    Retrieve, update or delete a bowler instance.
    """
    try:
        bowler = Bowler.objects.get(id=pk)
    except Bowler.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = BowlerSerializer(bowler)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = BowlerSerializer(bowler, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        bowler.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


