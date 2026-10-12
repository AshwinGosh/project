from django.urls import path
from . import views

urlpatterns = [
    path("login/", views.admin_login, name="admin_login"),
    path("panel/", views.admin_panel, name="admin_panel"),
    path("logout/", views.admin_logout, name="admin_logout"),
    path("add_user/", views.add_user, name="add_user"),
    path("edit_user/<int:user_id>/", views.edit_user, name="edit_user"),
    path("delete_user/<int:user_id>/", views.delete_user, name="delete_user"),
    path("announcements/", views.admin_announcements, name="admin_announcements"),
    path("add_announcement/", views.add_announcement, name="add_announcement"),
    path("edit_announcement/<int:id>/", views.edit_announcement, name="edit_announcement"),
    path("delete_announcement/<int:id>/", views.delete_announcement, name="delete_announcement"),
]