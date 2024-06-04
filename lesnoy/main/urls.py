from django.urls import include, path
from . import views
from django.contrib.auth.views import LogoutView


complaints_patterns = [
    path('', views.all_complaints, name="complaints"),
    path('my_complaints/<int:user_id>', views.my_complaints, name="my_complaints"),
]

urlpatterns = [
    path('', views.main, name='home_page'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.register_view, name='registration'),
    path('logout/', LogoutView.as_view(next_page='..'), name='logout'),
    path('add_complaints/<int:id>', views.add_complaint_view, name="add_complaints"),
    path('complaints/', include(complaints_patterns)),
]