from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import numpy as np



def index(request):
    context={'a':'Hello user'}
    return render(request, 'index.html',context)
    #return HttpResponse({'a':1})


    
