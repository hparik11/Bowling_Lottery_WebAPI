# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response
from jackpot.models import Bowler
from django.http import HttpResponseRedirect
from django.utils import timezone
#from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from jackpot.models import Bowler
from jackpot.serializers import BowlerSerializer
from rest_framework import status
from rest_framework.decorators import api_view

from rest_framework.response import Response

"""
class JSONResponse(HttpResponse):
    

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def articles(request):
    #language = 'en-us'
    #session_language = 'en-us'

    #if 'lang' in request.COOKIES:
    #    language = request.COOKIES['lang']
    return render_to_response('articles.html',{'jackpot':Bowler.objects.all()})# Create your views here.
"""





@api_view(['GET', 'POST'])
def bowler_list(request):
    """
    List all snippets, or create a new snippet.
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
def bowler_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
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

