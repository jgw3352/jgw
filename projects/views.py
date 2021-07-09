from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from projects.models import NewModel


def hello_world(request):
    if request.method == "POST":

        temp = request.POST.get('input_text')

        new_model = NewModel()
        new_model.text = temp
        new_model.save()

        return render(request, 'projects/hello_world.html',
                      context={'new_model': new_model})
    else:
        return render(request, 'projects/hello_world.html',
                      context={'text': 'GET METHOD'})
