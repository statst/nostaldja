from django.urls import path
from . import views


urlpatterns = [
    path('', views.decade_list, name="decade_list"),
    path('decade/<int:pk>', views.decade_detail, name="decade_detail"),
    path('decade/new', views.decade_create, name='decade_create'),
    path('decade/<int:pk>/delete', views.decade_delete, name="decade_delete"),

    path('fads/', views.fads_list, name="fads_list"),
    path('fads/<int:id>', views.fads_detail, name="fads_detail"),
    path('fads/new', views.fads_create, name='fads_create'),
    path('fads/<int:id>/delete', views.fads_delete, name='fads_delete'),
]