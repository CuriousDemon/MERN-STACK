from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

def homePage(request):
    if request.method == "POST":
        if "signup-form" in request.POST :
            username = request.POST.get("username")
            email = request.POST.get("email")
            password1 = request.POST.get("password")
            password2 = request.POST.get("Cpassword")

            if password1 != password2 :
               msg = "Please make sure your password & confirm password same !!" 
               messages.error(request,msg)
               return HttpResponseRedirect(request.path)    

    return render(request,"index.html")