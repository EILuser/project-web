from django.urls import include, path
from . import views
from django.contrib.auth.views import LogoutView


complaints_patterns = [
    path('', views.all_complaints_view, name="complaints"),
    path('my_complaints/', views.my_complaints_view, name="my_complaints"),
]

messages_patterns = [
    path('', views.messages_view, name="messages"),
    path('make_read/<int:message_id>', views.make_read_view, name="make_read"),
    path('delete_message/<int:message_id>', views.delete_message_view, name="delete_message"),
]

urlpatterns = [
    path('', views.main_view, name='home_page'),
    path('login/', views.login_view, name='login'),
    path('registration/', views.register_view, name='registration'),
    path('logout/', LogoutView.as_view(next_page='..'), name='logout'),
    path('add_complaints/', views.add_complaint_view, name="add_complaints"),
    path('complaints/', include(complaints_patterns)),
    path('news/', views.news_view, name="news"),
    path('send_message/', views.send_message_view, name="send_message"),
    path('messages/', include(messages_patterns)),
    path('meter_readings/', views.send_meter_readings_view, name="meter_readings"),
]