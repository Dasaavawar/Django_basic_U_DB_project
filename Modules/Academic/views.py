from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def contactform(request):
    return render(request, "contact_form.html")

def contact(request):
    if request.method == "POST":
        title = request.POST["txttitle"]
        message = request.POST["txtmessage"] + " / Email:" + request.POST["txtemail"]
        email_from = settings.EMAIL_HOST_USER
        email_to = ["dasaavawar@gmail.com"]
        send_mail(title, message, email_from, email_to, fail_silently=False)
        return render(request, "sucess_contact.html")
    return render(request, "contact_form.html")