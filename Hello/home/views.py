from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from home.models import Info
from django.contrib import messages

# Create your views here.
prices = {
    'conePack': 450,
    'familyPack': 200,
    'chocobar': 30,
    'cassataCake': 500,
    'cup': 30,
    'teddy': 60,
    'cassata': 90,
    'black': 100
}
def index(request):
    # return HttpResponse("This is home page.")
    return render(request, 'index.html', prices)
def about(request):
    return render(request, 'about.html')
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your feedback has been sent.')
    return render(request, 'contact.html')
def buy1(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pay = request.POST.get('pay')
        info = Info(name=name, email=email, address=address, city=city, state=state, pay=pay, date=datetime.today())
        info.save()
        messages.success(request, 'You successfully bought Cone Pack.')
    return render(request, '1.html', prices)
def buy2(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pay = request.POST.get('pay')
        info = Info(name=name, email=email, address=address, city=city, state=state, pay=pay, date=datetime.today())
        info.save()
        messages.success(request, 'You successfully bought Family Pack.')
    return render(request, '2.html', prices)
def buy3(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pay = request.POST.get('pay')
        info = Info(name=name, email=email, address=address, city=city, state=state, pay=pay, date=datetime.today())
        info.save()
        messages.success(request, 'You successfully bought Chocobar.')
    return render(request, '3.html', prices)
def buy4(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pay = request.POST.get('pay')
        info = Info(name=name, email=email, address=address, city=city, state=state, pay=pay, date=datetime.today())
        info.save()
        messages.success(request, 'You successfully bought Cassata Cake.')
    return render(request, '4.html', prices)
def buy5(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pay = request.POST.get('pay')
        info = Info(name=name, email=email, address=address, city=city, state=state, pay=pay, date=datetime.today())
        info.save()
        messages.success(request, 'You successfully bought Ice Cream Cup.')
    return render(request, '5.html', prices)
def buy6(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pay = request.POST.get('pay')
        info = Info(name=name, email=email, address=address, city=city, state=state, pay=pay, date=datetime.today())
        info.save()
        messages.success(request, 'You successfully bought Teddy Bear Ice Cream.')
    return render(request, '6.html', prices)
def buy7(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pay = request.POST.get('pay')
        info = Info(name=name, email=email, address=address, city=city, state=state, pay=pay, date=datetime.today())
        info.save()
        messages.success(request, 'You successfully bought Cassata.')
    return render(request, '7.html', prices)
def buy8(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        pay = request.POST.get('pay')
        info = Info(name=name, email=email, address=address, city=city, state=state, pay=pay, date=datetime.today())
        info.save()
        messages.success(request, 'You successfully bought Black Currant Ice cream.')
    return render(request, '8.html', prices)
