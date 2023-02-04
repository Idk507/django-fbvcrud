from django.shortcuts import render,redirect
from fbvapp.models import student
from fbvapp.forms import studentform
from django.contrib.auth.decorators import login_required,permission_required

# Create your views here.
@login_required
def studentsdata(request):
    students = student.objects.all()
    context={}
    context['students']= students
    return render(request,'index.html',context)

def logout(request):
    return render(request,';logout.html')

@login_required
def  createstudent(request):
    form = studentform()
    if request.method == 'POST':
        form = studentform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
    return render(request,'create.html',{'form':form})

@login_required    
@permission_required('fbvapp.delete_student')
def deleteid(request,id) :
    students = student.objects.get(id=id)
    students.delete()
    return redirect('/')  

@login_required 
def updateid(request,id):
    students = student.objects.get(id=id)
    form = studentform(instance=students)
    if request.method =='POST':
        form = studentform(request.POST,instance = students)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'update.html',{'form':form})