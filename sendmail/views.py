import os

from django.core.mail import EmailMessage
from django.template import Context, Template
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from balastanServer.settings import BASE_DIR


def sendMail(request):
    try:

        name = request.POST.get('name')
        number = request.POST.get('number')
        f = open(os.path.join(BASE_DIR, "templates/mail.html"))

        content = f.read()
        f.close()
        context = Context(dict(name=name, number=number))
        template = Template(content)

        email = EmailMessage('Balastan', template.render(context), to=['avaz.abdrasulov@gmail.com'])
        email.content_subtype='html'
        email.send()
        return JsonResponse(dict(result='okay'))

    except:

        return JsonResponse(dict(result='error'))
