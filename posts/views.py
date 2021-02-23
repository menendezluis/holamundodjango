#Django
from django.http import HttpResponse

def list_posts(request):
    """Lists existing posts."""
    posts = [1, 2 ,4]
    return HttpResponse(str(posts))
# Create your views here.
