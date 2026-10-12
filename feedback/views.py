from django.shortcuts import redirect, render
from django.http import HttpResponse
from . models import feedback
from feedback import models
from .models import feedback
from .models import Announcement


def admin_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if email == "admin@example.com" and password == "admin123":
            request.session['is_admin'] = True
            return redirect('admin_panel')
        else:
            return render(request, 'admin_login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'admin_login.html')

def admin_panel(request):
    if not request.session.get('is_admin'):
        return redirect('admin_login')
    
    all_users = feedback.objects.all()
    
    context = {
        'users': all_users,
        'total_users': all_users.count()
    }
    return render(request, 'admin_panel.html', context)

def admin_logout(request):

    request.session['is_admin'] = False
    return redirect('admin_login')
def house(request):
    return render(request, 'house.html',)
def home(request):
    return render(request, 'home.html',)
def login(request):
    next_url = request.GET.get("next", "house")

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        next_url = request.POST.get("next", "house")

        user = feedback.objects.filter(
            email=email,
            password=password
        ).first()

        if user:
            request.session["user"] = user.email

            if next_url == "home":
                return redirect("home")   # 🔥 feedback page
            else:
                return redirect("house")  # normal login

        return render(request, "login.html", {
            "error": "Invalid email or password",
            "next": next_url
        })

    return render(request, "login.html", {"next": next_url})
def register(request):
    if request.method == "POST":
        print("POST DATA =", request.POST)
        print("EMAIL =", request.POST.get("email"))

        email = request.POST.get("email")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        feedback.objects.create(
            email=email,
            name=name,
            phone=phone,
            password=password
        )

        return redirect("login")   

    return render(request, "register.html")
def feedback_home(request):
    if 'user' not in request.session:
        return redirect('/login/?next=home')   

    return render(request, 'home.html')  

def announcements_page(request):
    announcements = Announcement.objects.all().order_by("-date")
    return render(request, "announcements.html", {"announcements": announcements})