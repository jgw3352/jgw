from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from projects.models import NewModel


def hello_world(request):
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





class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('projects:hello_world')
    template_name = 'projects/create.html'


class AccountDetailView(DetailView):
    model = User
    contest_object_name = 'target_user'
    template_name = 'projects/detail.html'