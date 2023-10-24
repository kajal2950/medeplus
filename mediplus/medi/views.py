from django.shortcuts import render
from. models import Services,Contact
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    service=Services.objects.all
    data={
        
        'service':service
    }
    return  render(request, 'index.html',data)
def contact(request):
    service=Services.objects.all
    data={
        
        'service':service
    }
    if request.method=="POST":
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        subject=request.POST.get('subject','')
        message=request.POST.get('message','')

        print(name)

        contact=Contact(name=name,email=email,phone=phone,subject=subject,message=message)
       
        subject=name
        message=message
        email_from=settings.EMAIL_HOST_USER
        try:
            send_mail(subject,message,email_from ,['payalkasayp2950@gmail.com'])
            contact.save()
            messages.info(request,"Message Sent Successfully")
            return redirect('/')
             
        except Exception as e:
            return redirect('contact')
    return  render(request, 'contact.html',data)

def about(request):
    service=Services.objects.all
    data={
        
        'service':service
    }
    return  render(request, 'about.html',data)

def services(request):
    service=Services.objects.all()
    data={
        'ser':service,

    }
    return  render(request, 'services.html', data)
def service_details(request,slug):
    service=Services.objects.all()
    team=Services.objects.filter(slug=slug)
    team={
        'ser':service,
        'team':team,
        
        
    }
    return render(request,'service_details.html',team)



def gallery(request):
    service=Services.objects.all
    data={
        
        'service':service
    }
    return  render(request, 'gallery.html',data)