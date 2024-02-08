from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.

#Representing the String using Funtion Based View

def fbv_string(request):
    return HttpResponse('<h1>String of Function Based View</h1>')


#Representing the String using Funtion Based View

class CbvString(View):
    def get(self,request):
        return HttpResponse('<h1>String of Class Based View</h1>')


#Rendering HTML page using Function Based View

def fbvHtml(request):
    return render(request,'fbvHtml.html')

#Rendering HTML page using Function Based View

class CbvHTML(View):
    def get(self,request):
        return render(request,'CbvHTML.html')
    

#get and post in funtional based view
def insert_school_fbv(request):
    SFO=SchoolForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Inserted successfully')
    return render(request,'insert_school_fbv.html',d)

#Get and post method usage in Class Based Views

class InsertSchoolCbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'InsertSchoolCbv.html',d)

    def post(self,request):
        if request.method=='POST':
            SFDO=SchoolForm(request.POST)
            if SFDO.is_valid():
                SFDO.save()
                return HttpResponse('DATA Inserted Successfully')


#Representing template using TEMPLATEVIEW

class Cbvtemplate(TemplateView):
    template_name='Cbv_template.html'