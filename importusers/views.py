from django.http import JsonResponse
from django.shortcuts import render

from .models import UserApp


# Create your views here.


def import_user(request):
    try:
        name = request.POST.get('name')
        middlename = request.POST.get('middlename')
        region = request.POST.get('region')
        photoUrl = request.POST.get('photoUrl')
        phoneNumber = request.POST.get('phoneNumber')
        digitsId = request.POST.get('digitsId')

        o = UserApp.objects.create(name=name, middlename=middlename, region=region, photoUrl=photoUrl,
                                   phoneNumber=phoneNumber, digitsId=digitsId)

        o.save()

        return JsonResponse(dict(result="success"))

    except:
        return JsonResponse(dict(result="error"))
