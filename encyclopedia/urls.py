from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.display_content, name='content'),
    path('createnewpage/', views.create_new_page, name='create_new_page'),
    path('<str:title>/edit', views.editpage, name='editpage'),
    path('random/random', views.randompage, name='randompage'),
]
