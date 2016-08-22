from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.

def sendMail(request):
    try:
        email = EmailMessage('title', 'body', to=['aibek.widgets@gmail.com'])
        email.send()
        return JsonResponse(dict(result='okay'))

    except:

        return JsonResponse(dict(result='error'))
