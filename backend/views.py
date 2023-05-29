from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.files.base import ContentFile
from .models import Image, UserInfo
from io import BytesIO
import base64
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        uname = request.POST.get("user_name")
        umail = request.POST.get("user_email")
        password = request.POST.get("password")
        file = request.FILES['file']

        img = Image(
            name=file.name,
            mime=file.content_type,
            data=file.read(),
            uname=uname,
            umail=umail,
            password=password,
        )
        img.save()
        userImg = Image.objects.filter(umail=umail).first()

        return render(request, "base.html", {'uname': uname, 'imga': userImg})

    return render(request, "index.html")


def download(request, image_id):
    img = get_object_or_404(Image, pk=image_id)
    response = HttpResponse(img.data, content_type=img.mime)
    response['Content-Disposition'] = 'attachment; filename=' + img.name
    return response


def success(request):
    passinp = request.POST.get("xy")
    tolerance = request.POST.get("tol")
    user = UserInfo(
        umail='siva@gmail.com',
        uspass=passinp
    )
    user.save()
    return render(request, "success.html", {'msg': "Account created"})


def login(request):
    if request.method == 'POST':
        dummy = request.POST.get("ur_email")
        usmail = dummy
        userImg = Image.objects.filter(umail=dummy).first()
        return render(request, "a.html", {'imga': userImg})
    else:
        messages.error(request, 'User doesn\'t exist!')
        return redirect('login')
    return render(request, "login.html")


def authenticate(request):
    ct = 0
    reqUser = UserInfo.objects.filter(umail='siva@gmail.com').first()
    passdata = reqUser.uspass
    coordinates = passdata.split()
    print(coordinates)
    loginuser = request.POST.get("passxy")
    logco = loginuser.split()
    for i in range(len(coordinates)):
        if int(logco[i]) >= int(coordinates[i])-20 and int(logco[i]) <= int(coordinates[i])+20:
            ct = ct+1
    if ct == 6:
        return render(request, "success.html", {'msg': "You are successfully logged in"})
    return render(request, "success.html", {'msg': "Sorry, you're unathenticated"})


def dashboard(request):
    return render(request, 'dashboard.html')