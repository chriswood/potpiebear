from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def main(request):
    return HttpResponse('heyman')
    
def heart(request):
    return render_to_response('widget.html',
                              {},
                              context_instance=RequestContext(request))
    