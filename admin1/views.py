from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from feedback.models import feedback
from feedback.models import Announcement
from django.shortcuts import render, redirect, get_object_or_404


def admin_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if email == "admin@example.com" and password == "admin123":
            request.session["is_admin"] = True
            return redirect("admin_panel")
        else:
            return render(request, "admin_login.html", {
                "error": "Invalid credentials"
            })

    return render(request, "admin_login.html")


def admin_panel(request):
    if not request.session.get("is_admin"):
        return redirect("admin_login")

    users = feedback.objects.all()

    return render(request, "admin_panel.html", {
        "users": users,
        "total_users": users.count()
    })


def admin_logout(request):
    request.session["is_admin"] = False
    return redirect("admin_login")

def add_user(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        feedback.objects.create(
            name=name,
            email=email,
            phone=phone,
            password=password
        )
        return redirect("admin_panel")

    return render(request, "add_user.html")

def edit_user(request, user_id):
    if not request.session.get('is_admin'):
        return HttpResponse("Not allowed")

    user = feedback.objects.get(id=user_id)

    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        user.save()
        return redirect('admin_panel')

    return render(request, 'edit_user.html', {'user': user})

def delete_user(request, user_id):

    user = feedback.objects.get(id=user_id)

    if request.method == "POST":
        user.delete()
        return redirect("admin_panel")

    return render(request, "delete_confirm.html", {"user": user})

def admin_announcements(request):
    announcements = Announcement.objects.all().order_by("-date")
    return render(request, "admin_announcements.html", {"announcements": announcements})


def add_announcement(request):
    if request.method == "POST":
        title = request.POST.get("title")
        message = request.POST.get("message")

        Announcement.objects.create(title=title, message=message)
        return redirect("admin_announcements")

    return render(request, "add_announcement.html")


def edit_announcement(request, id):
    announcement = get_object_or_404(Announcement, id=id)

    if request.method == "POST":
        announcement.title = request.POST.get("title")
        announcement.message = request.POST.get("message")
        announcement.save()

        return redirect("admin_announcements")

    return render(request, "edit_announcement.html", {"announcement": announcement})


def delete_announcement(request, id):
    announcement = get_object_or_404(Announcement, id=id)

    if request.method == "POST":
        announcement.delete()
        return redirect("admin_announcements")

    return render(request, "delete_announcement.html", {"announcement": announcement})

# Create your views here.
