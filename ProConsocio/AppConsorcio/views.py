from django.shortcuts import render
from django.views import generic
from .models import Personal

# Create your views here.

def index(request):
    num_personal = Personal.objects.all().count()
    
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_personal': num_personal,
        'num_visits': num_visits,
    }

    return render(request, 'index.html', context=context)



class PersonalListView(generic.ListView):
    model = Personal
    template_name = 'AppConsorcio/personal_list.html'
