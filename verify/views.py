from django.shortcuts import render
from .models import Contact

# Create your views here.
def indexxx(request):
    return render(request, 'verif/index1.html')

def contact(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        pwd = request.POST.get("pwd")

        contact.name = name
        contact.email = email
        contact.message = message
        contact.pwd = pwd
        contact.save()
        
    return render(request, 'verif/contact.html')