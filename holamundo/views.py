
from django.http import HttpResponse

#utilities
from datetime import datetime
import csv, io, json
def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, hie current server time is {now}'.format(now=now))

def hi(request):
    """Hi"""
    numbers = request.GET['numbers']
    reader = csv.DictReader(io.StringIO(numbers))

    json_data = json.dumps(list(reader))
    
    return HttpResponse(json_data)