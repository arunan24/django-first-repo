from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import View,TemplateView
from django.http import HttpResponse, request
from . import models
###list view and details view####
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy



def index(request):
    return render(request,'django_first_app/index.html')

class ClassBasedBiewname(View):
    def get(self,request):
        return HttpResponse("Displaying Class based view")

class CBVTemapleView(TemplateView):
    template_name = 'django_first_app/indexcbvt.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['injectme'] = "Welcome ijection"
        return context

class schoolListView(ListView):
    # context_object_name = 'schools'      defining our own object name to pass to html
    model = models.School


class studentDetailView(DetailView):
    context_object_name = 'student_detail'
    model = models.School
    template_name = 'django_first_app/student_details.html'

    # def get_object(self):
    #     return get_object_or_404(User, pk=request.session['user_id'])

class createschool(CreateView):
    fields = ('nameofSchool','nameofPrincipal','locationofSchool')
    model = models.School

class updateschool(UpdateView):
    fields =('nameofSchool','nameofPrincipal','locationofSchool')
    model=models.School


class deleteschool(DeleteView):
    model = models.School
    success_url = reverse_lazy('school')



# Create your views here.
