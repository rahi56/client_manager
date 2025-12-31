from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # ---------------- Client Pages ----------------
    path('', views.client_list, name='client_list'),  # Home / Client list
    path('add/', views.client_form, name='client_create'),
    path('edit/<int:pk>/', views.client_form, name='client_edit'),
    path('delete/<int:pk>/', views.client_delete, name='client_delete'),
    path('restore/<int:pk>/', views.restore_client, name='client_restore'),

    # ---------------- Company Pages ----------------
    path('companies/', views.company_list, name='company_list'),
    path('companies/<str:company_name>/', views.company_detail, name='company_detail'),

    # ---------------- Client Actions ----------------
    path('client/action/<int:pk>/', views.client_action, name='client_action'),

    # ---------------- Status Pages ----------------
    path('approved/', views.approved_clients, name='approved_clients'),
    path('issued/', views.issued_clients, name='issued_clients'),
    path('denied/', views.denied_clients, name='denied_clients'),

    # ---------------- Export ----------------
    path('export-excel/', views.export_excel, name='export_excel'),

    # ---------------- Authentication ----------------
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='login'),
        name='logout'
    ),
]
