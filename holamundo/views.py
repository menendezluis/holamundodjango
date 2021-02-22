
from django.http import HttpResponse

#utilities
from datetime import datetime

def hello_world(request):
    now = datetime.now()
    return HttpResponse('Oh, hie current server time is {now}'.format(now=str(now)))


