
from django.http import HttpResponse
from django.http import JsonResponse

#utilities
from datetime import datetime
import csv, io, json
def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hie current server time is {now}'.format(now=now))

def hi(request):
    """Hi"""
    numbers = request.GET['numbers']
    
    json_data = json.dumps(list(numbers))
    
    return JsonResponse(json_data, content_type="application/json")