from django.urls import path
from . import views


urlpatterns = [
    path('', views.note_list, name="note_list"),
    path('note/<int:pk>/',views.note_detail, name="note_detail"),
    path('note/<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('note/new/', views.note_create, name='note_create'),
]