from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def helloworld(request):
    logging.error('Hello world DJ4E in the log...')
    print('Hello world DJ4E in a print statement...')
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits 
    if num_visits > 4 : del(request.session['num_visits'])
    return HttpResponse('view count='+str(num_visits))
def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap', None)
    resp = HttpResponse('In a view - the zap cookie value is '+str(oldval))
    if oldval : 
        resp.set_cookie('zap', int(oldval)+1) # No expired date = until browser close
    else : 
        resp.set_cookie('zap', 42) # No expired date = until browser close
        resp.set_cookie('dj4e_cookie', '5cf21ce3', max_age=1000) # seconds until expire
    return resp


  