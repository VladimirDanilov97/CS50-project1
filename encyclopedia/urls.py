from django.urls import path, re_path 

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    re_path(r"^(?P<title>[^$]\w+)$", views.display_content, name='content'),
    path('$createnewpage/', views.create_new_page, name='create_new_page'),
    path('<str:title>/edit', views.editpage, name='editpage'),
    path('$random', views.randompage, name='randompage'),
]
