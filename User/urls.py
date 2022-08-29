from django.urls import path
from . import views

urlpatterns = [
    path('/register', views.register, name='register'),
    path('/login', views.login, name='login'),
    path('/business-login', views.business_login, name="business-login"),
    path('/business-register', views.business_register, name="business-register"),
    path('/logout', views.Logout, name='logout'),
    path('/business-profile/<str:slug>', views.business_profile, name='business-profile'),
    path('/student-profile/<str:slug>', views.student_profile, name='student-profile'),
    path('/student-profile-edit', views.get_student_profile_edit, name='student-profile-edit'),
    path('/business-profile-edit', views.get_business_profile_edit, name='business-profile-edit'),
    path('/student-edit-post', views.post_student_profile_edit, name="student-edit-post"),
    path('/business-edit-post', views.post_business_profile_edit, name="business-edit-post"),
    path('/business-post', views.get_post, name='business-post'),
    path('/business-post-add', views.post_post, name='business-post-add'),
    path('/business-post-list', views.post_list, name='business-post-list'),
    path('/business-post-update/<int:id>', views.get_post_update, name='business-post-update'),
    path('/business-post-updates/<int:id>', views.post_update, name='business-post-updates'),
    path('/business-post-delete/<int:id>', views.delete_post, name='business-post-delete'),
    path('/student-apply/<int:id>', views.student_apply, name='student-apply'),
    path('/student-apply-list', views.student_apply_list, name='student-apply-list'),
    path('/student-profile-detail/<str:slug>', views.student_profile_detail, name='student-profile-detail'),
    path('/business-profile-detail/<str:slug>', views.business_profile_detail, name='business-profile-detail'),
    path('/business-students-list/<int:id>', views.business_list_student, name='business-list-students'),

]
