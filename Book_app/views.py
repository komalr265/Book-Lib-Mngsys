from django.shortcuts import (render, HttpResponseRedirect)
from .forms import Stud_reg
from  .models import User

# Create your views here.


# ...................add all functions and show the atioms using following .......................
def add_show(request):      # INSERT DATA
    if request.method == 'POST':
        obj=Stud_reg(request.POST)
        if obj.is_valid():
            #to access cleaned data
            name=obj.cleaned_data['name']
            email=obj.cleaned_data['email']
            #pw=form_obj.cleaned_data['password']   # no need to store password
            #create obj for model class
            reg=User(name=name, email=email)
            reg.save()
            obj=Stud_reg() 
            
    else:
     obj=Stud_reg()     #fm
    new_obj= User.objects.all()                     # to retrive all data or see all  data

        
    return render(request, 'Book_app/add_and_show.html',{'form' :obj,'stu':new_obj})

#................................  edit Data .....................................................
def edit_data(request,id):
    
    if request.method== "POST":
        edt_obj= User.objects.get(pk=id)
        obj= Stud_reg(request.POST,instance=edt_obj)
        if obj.is_valid():
            obj.save()
            #code for GET
    else:
     edt_obj = User.objects.get(pk=id)   #pi
     obj=Stud_reg(instance=edt_obj)
    return render(request, "Book_app/update_student.html" , {'form':obj})

#....................... delete  .......................

def delete_data(request, id):
    if request.method=="POST":
     del_obj=User.objects.get(pk=id)
     del_obj.delete_data()
    return  HttpResponseRedirect('/')     # redirect on home page


