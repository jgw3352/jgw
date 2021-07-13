from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

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
