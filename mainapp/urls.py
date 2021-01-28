from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('home',views.index,name="index"),
    path('maintea',views.maintea),
    path('maintea_update/<int:id>',views.maintea_update),
    path('maintea_delete/<int:id>',views.maintea_delete),
    path('favourite_tea',views.favouriteTea),
    path('favouriteTea_update/<int:id>',views.favouriteTea_update),
    path('favouriteTea_delete/<int:id>',views.favouriteTea_delete),
    path('contact',views.contact),
    path('admin_panel/',views.admin),
    path('admin_mainTea',views.admin_mainTea,name="admin_mainTea"),
    path('admin_favouriteTea',views.admin_favouriteTea,name='admin_favouriteTea'),
    path('admin_blog',views.admin_blog,name='admin_blog'),
    path('blog',views.blog,name="blog"),
    path('single_blog/<int:id>',views.single_blog,name='single_blog'),
    path('post',views.post,name='post'),
    path('blog_update/<int:id>',views.blog_update,name='blog_update'),
    path('blog_delete/<int:id>',views.blog_delete,name='blog_delete'),

]