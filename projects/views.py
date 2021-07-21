from importlib.resources import path

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from projects.forms import AccountCreationForm
from projects.models import NewModel


def hello_world(request):
    if request.user.is_authenticated:
        if request.method == "POST":

            temp = request.POST.get('input_text')

            new_model = NewModel()
            new_model.text = temp
            new_model.save()



            return HttpResponseRedirect(reverse('projects:hello_world'))
        else:
            data_list = NewModel.objects.all()
            return render(request, 'projects/hello_world.html',
                         context={'data_list': data_list})
    else:
        return HttpResponseRedirect(reverse('projects:login'))



class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('projects:hello_world')
    template_name = 'projects/create.html'




class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'projects/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('projects:hello_world')
    template_name = 'projects/update.html'


    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args , **kwargs)
        else:
            return HttpResponseRedirect(reverse('projects:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('projects:login'))




class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'projects/delete.html'



    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args , **kwargs)
        else:
            return HttpResponseRedirect(reverse('projects:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('projects:login'))
