# myapp/middleware.py
from django.conf import settings
from django.shortcuts import get_object_or_404, render,redirect,HttpResponse
from django.utils.deprecation import MiddlewareMixin
import requests
from sale.models import *

from sale.views import dsamanualId

class AuthMiddleware:
    
    def __init__(self, get_response):
        self.get_response = get_response
        # self.protected_paths = getattr(settings, 'PROTECTED_PATHS', [])

    def __call__(self, request):

        if not request.session.get('verified') and request.path=='/sa/Login' and request.method!='POST':
         
            request.session['indexPage']=True
            return render(request,'dsaLogin.html')

        if request.GET.get('id') and request.path.startswith('/sa/AllLoans'):
            request.session['dsanologin']=True
            return self.get_response(request)
        elif request.path.startswith('/sa/api/'):
           return self.get_response(request)
        
       
       
        
        
        if (request.path.startswith('/sa/') or request.path.startswith('/dsacomisions/')) and not request.session.get('verified') and request.path!='/sa/Login':
           if request.session.get('indexPage'):
               del request.session['indexPage']
           request.session['pageurl']=request.build_absolute_uri()
           return render(request,'dsaLogin.html')
        else:
            
            response = self.get_response(request)
            return response