from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from db_utils import db_wrapper
from django.conf import settings


def main(request):
    context_dict = {}
    conn = db_wrapper(settings.db_path)
    context_dict['results'] = conn.get_users()
    
    return render_to_response('main.html',
                              context_dict,
                              context_instance=RequestContext(request))
    
def heart(request):
    return render_to_response('widget.html',
                              {},
                              context_instance=RequestContext(request))
    
