from django.urls import include, path
from . import views
from django.contrib.auth.views import LogoutView


complaints_patterns = [
    path('', views.all_complaints_view, name="complaints"),
    path('my_complaints/', views.my_complaints_view, name="my_complaints"),
]

admin_messages_patterns = [
    path('', views.admin_messages_view, name="admin_messages"),
    path('admin_make_read/<int:message_id>', views.make_read_view, name="admin_make_read"),
    path('admin_delete_message/<int:message_id>', views.delete_message_view, name="admin_delete_message"),
    path('reply/<int:message_id>', views.reply_view, name="reply"),
]

user_messages_patterns = [
    path('', views.user_messages_view, name="user_messages"),
    path('delete_message/<int:message_id>', views.delete_message_view, name="delete_message"),
    path('make_read/<int:message_id>', views.make_read_view, name="make_read"),
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
    path('admin_messages/', include(admin_messages_patterns)),
    path('user_messages/', include(user_messages_patterns)),
    path('meter_readings/', views.send_meter_readings_view, name="meter_readings"),
]