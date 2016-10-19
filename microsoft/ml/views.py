from django.shortcuts import render,render_to_response,HttpResponseRedirect,get_object_or_404
from django.template import RequestContext, loader,Template
from django.template.defaultfilters import slugify
from django.http import HttpResponse
import os,re,collections,random,imp,nltk
from .models import Sentiments
from decimal import Decimal
from ml.serializers import mlSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from nltk import tokenize
from nltk.sentiment import *
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#@csrf_exempt
def process_detail(request,data):
    str = data.split('_')
    str = ' '.join(str)
    #str = request.POST['data']
    sid = SentimentIntensityAnalyzer()
    ss = sid.polarity_scores(str)
    senti = Sentiments(text = str,compound = ss['compound'],neg = ss['neg'] ,neu = ss['neu'],pos = ss['pos'])
    serializer = mlSerializer(senti)
    return JsonResponse(serializer.data)