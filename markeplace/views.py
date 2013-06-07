# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View as Controller
from django.shortcuts import render_to_response
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from models import User
from forms import UserForm

class HomeController(Controller):
    def get(self, request):
        return render_to_response("home.html")

class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'user_create.html'
    success_url = reverse_lazy('user_list')

class PerfilController(Controller):
    def get(self, request):
        return render_to_response("home.html")
