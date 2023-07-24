from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from home.models import Notes
from django.urls import reverse_lazy

from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

# Create your views here.
def index(request):
    return render(request, 'index.html')


class signup(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('notes')
    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(signup, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('notes')
        return super(signup, self).get(*args, *kwargs)




def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            print('pass')
            return redirect("/notes")

        else:
            print('no backend')
            # No backend authenticated the credentials
            return render(request, "index.html")


    return render(request, 'index.html')

class NotesList(LoginRequiredMixin , ListView):
    model = Notes
    context_object_name = 'notes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['notes'] = context['notes'].filter(user=self.request.user)
        return context


class NotesCreate(LoginRequiredMixin, CreateView):
    model = Notes
    fields = ['title','content']
    success_url = reverse_lazy('notes')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NotesCreate, self).form_valid(form)

class NotesView(LoginRequiredMixin, DetailView):
    model = Notes
    fields = ['title', 'content']

class NotesUpdate(LoginRequiredMixin, UpdateView):
    model = Notes
    fields = ['title','content']
    success_url = reverse_lazy('notes')

class NotesDelete(LoginRequiredMixin, DeleteView):
    model = Notes
    context_object_name = 'notes'
    success_url = reverse_lazy('notes')


