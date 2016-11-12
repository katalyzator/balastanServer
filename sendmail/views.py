import os

from django.core.mail import EmailMessage
from django.template import Context, Template
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from balastanServer.settings import BASE_DIR


@csrf_exempt
def sendMail(request):
    try:

        name = request.POST.get('name')
        number = request.POST.get('number')
        f = open(os.path.join(BASE_DIR, "templates/mail.html"))

        content = f.read()
        f.close()
        context = Context(dict(name=name, number=number))
        template = Template(content)

<<<<<<< HEAD
        email = EmailMessage('Balastan', template.render(context), to=['abontentter@gmail.com'])
        email.content_subtype = 'html'

=======
        email = EmailMessage('Balastan', template.render(context), to=['avaz.abdrasulov@gmail.com'])
        email.content_subtype = 'html'

        email = EmailMessage('Balastan', template.render(context), to=['abonentter@gmail.com'])
        email.content_subtype = 'html'

        email.send()
        return JsonResponse(dict(result='okay'))

    except:

        return JsonResponse(dict(result='error'))


def sendEmail(request):
    try:

        mail = request.POST.get('email')
        message = request.POST.get('message')
        f = open(os.path.join(BASE_DIR, "templates/email.html"))

        content = f.read()
        f.close()
        context = Context(dict(mail=mail, message=message))
        template = Template(content)

        email = EmailMessage('EasyDo', template.render(context), to=['odaniaro@gmail.com'])
        email.content_subtype = 'html'

>>>>>>> 94c06e85e606e64bf2992fc5b2fffeeeefdaceb6
        email.send()
        return JsonResponse(dict(result='okay'))

    except:

        return JsonResponse(dict(result='error'))
