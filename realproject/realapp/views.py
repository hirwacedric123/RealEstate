from django.shortcuts import render, redirect
from realapp.models import House
from django.contrib import messages
from django.core.mail import send_mail
from django.http import JsonResponse
from math import ceil
# Create your views here.
def index(request):
    current_user = request.user
    print(current_user)
    allAssts = []
    catassts = House.objects.values('use','id')
    cats = {item['use'] for item in catassts}
    for cat in cats:
        asst = House.objects.filter(use=cat) 
        n = len(asst)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allAssts.append([asst,range(1,nSlides),nSlides])
    params = {'allAssts':allAssts}
    return render(request,'index.html',params)


def send_message(request):
    if request.method == 'POST':
        # Retrieve form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        # Send email
        send_mail(
            'Subject here',  # subject of the email
            message,  # message body
            email,  # sender's email
            ['hirwacedr12@gmail.com'],  # recipient's email
            fail_silently=False,
        )
        messages.success(request, 'Email sent successfully!')
        return redirect('index.html')  # Replace 'index' with the appropriate URL name for your index page

    return render(request, 'index.html')