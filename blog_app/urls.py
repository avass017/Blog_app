from django.urls import path

from blog_app import views, adminviews, userview

urlpatterns = [
 path('', views.index, name='index'),
 path('dashboard', views.dashboard, name='dashboard'),
 path('login_page', views.login_page, name='login_page'),
 path('users', views.users, name='users'),
 path('admin', views.admin, name='admin'),
 path('users_add', views.users_add, name='users_add'),
 path('login_view', views.login_view, name='login_view'),
 path('users_view',adminviews.users_view, name='users_view'),
 path('user_delete/<int:id>',adminviews.user_delete, name='user_delete'),
 path('my_profile',userview.my_profile, name='my_profile'),
 path('user_edit',userview.user_edit, name='user_edit'),
 path('Log_out',userview.Log_out, name='Log_out'),
 path('blog_add',userview.blog_add, name='blog_add'),
 path('blog_view',userview.blog_view, name='blog_view'),
 path('blog_list',userview.blog_list, name='blog_list'),
 path('blog_list_admin',adminviews.blog_list_admin, name='blog_list_admin'),
 path('blog_update/<int:id>',userview.blog_update, name='blog_update'),
 path('blog_delete/<int:id>',userview.blog_delete, name='blog_delete'),
 path('Log_out',userview.Log_out, name='Log_out'),

]
