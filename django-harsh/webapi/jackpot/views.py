# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.utils import timezone
from jackpot.models import Bowler
from jackpot.models import League
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from jackpot.serializers import *





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


@api_view(['GET', 'POST'])
def league_list(request, format=None):
    """
    List all Leagues, or create a new snippet.
    """
    if request.method == 'GET':
        leagues = League.objects.all()
        serializer = LeagueSerializer(leagues, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LeagueSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'PUT', 'DELETE'])
def league_detail(request, pk, format=None):
    """
    Retrieve, update or delete a league instance.
    """
    try:
       league = League.objects.get(id=pk)
    except League.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LeagueSerializer(league)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = LeagueSerializer(league, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        league.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def join_league(request, pk, format=None):
    """
    List all Leagues, or create a new snippet.
    """
    try:
       league = League.objects.get(id=pk)
    except League.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = LeagueSerializer(league)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = LeagueSerializer(league, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

