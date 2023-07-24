from django.urls import path
from django.contrib import admin
from home import views
from django.contrib.auth.views import LogoutView
#import List and Detail voew modal
from .views import NotesList, NotesCreate, NotesUpdate , NotesDelete , signup , NotesView



urlpatterns = [
    path('', views.index, name='home'),
    path('login', views.loginUser, name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup', signup.as_view(), name='signup'),
    path('notes', NotesList.as_view(), name='notes'),
    path('create', NotesCreate.as_view(), name='create'),
    path('view/<int:pk>/', NotesView.as_view(), name='view'),
    path('update/<int:pk>/', NotesUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', NotesDelete.as_view(), name='delete'),
]