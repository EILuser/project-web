from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.main, name='home_page'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.register_view, name='registration'),
    path('logout/', LogoutView.as_view(next_page='..'), name='logout'),
    path('complaints/<int:id>', views.complaint_view, name="complaints"),
]