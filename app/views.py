from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'Chaithanya','age':23}
    return render(request,'data_render.html',context=d)
def ifconditions(request):
    d={'a':10,'b':200,'c':30}
    return render(request,'ifconditions.html',context=d)