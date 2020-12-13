from django.shortcuts import render
from django.http import HttpResponse
from random import choice

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    leng = int(request.GET.get('length', 12))
    char = list("abcdefghijklmnopqrstuvwxyz")
    
    if request.GET.get("uppercase"):
        char.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        
    if request.GET.get("Numbers"):
        char.extend(list("0123456789"))
    
    if request.GET.get("Special characters"):
        char.extend(list("!@#$%^&*_)("))
    
    generated_password = ""
    if leng >= 6 and leng <= 14:
        for x in range(leng):
            rand = choice(char)
            generated_password += rand
    else:
        generated_password = "Opps! your password should be between 6 and 14"
        
    return render(request, 'generator/password.html', 
                  dict(password=generated_password))

def about(request):
    return render(request, 'generator/about.html')
