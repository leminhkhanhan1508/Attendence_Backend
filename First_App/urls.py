from django.conf.urls.static import static
from django.urls import path

from UIT_Roll_UP import settings
from . import views

urlpatterns = [
    path('courses/', views.get_courses.as_view()),
    path('attend/', views.image.as_view()),
    path('join/', views.join.as_view()),
    path('register/', views.register.as_view()),
    path('login/', views.login.as_view()),
    path('course/lesson/', views.create_lesson.as_view()),
    # url create lesson with mac address (lap trinh ung dung mang)
    path('course/lesson/mac/', views.create_lesson_mac_address.as_view()),
    # url attandance with mac address (lap trinh ung dung mang)
    path('course/lesson/attendance/', views.attendance_mac_address.as_view()),

    path('courses/newcourse/', views.create_new_course.as_view()),
    path('attend/<int:pk>/', views.AttendentDetail.as_view()),
    path('course/lesson/information/', views.infolesson.as_view()),
    path('course/information/', views.infocourse.as_view()),
    path('attend/report/<int:pk>/', views.AttendentReport.as_view()),
    path('information/account/', views.get_inf_account.as_view()),
    path('attend/information/change/<int:pk>/', views.Set_Info_RollUp.as_view()),
    path('user/avatar/change/', views.change_avatar_account.as_view()),
    path('attend/rfid/', views.check_id_rfid.as_view()),
    path('register/rfid/', views.register_card_rfid.as_view()),
    path('account/password/change/', views.change_password.as_view()),
    path('account/password/forgot/', views.forgot_password.as_view())
    # path('courses/<int:pk>/', views.SnippetDetail.as_view()),

]
