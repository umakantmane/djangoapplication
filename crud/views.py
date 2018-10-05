from django.shortcuts import render, redirect
from crud.forms import EmpForm,EmpForm2,EmpDucationForm
from crud.models import Employee,EmployeeEducation
from django.contrib.auth.decorators import login_required



def eduIndex(request):

    data = EmployeeEducation.objects.all()
    return  render(request, 'crud/edu_index.html', {'data':data})

def eduCreate(request):

    form = EmpDucationForm()
    if request.method == 'POST':
        form = EmpDucationForm(request.POST)
        if form.is_valid():
            print(request.POST  )
            print(form.cleaned_data['employee'])
            #form.save()
            edu = EmployeeEducation()
            edu.employee = form.cleaned_data['employee']
            edu.edu_name = form.cleaned_data['edu_name']
            edu.edu_uni = form.cleaned_data['edu_uni']
            edu.save()
            form = EmpDucationForm()
            return redirect(eduIndex)

    return render(request, 'crud/create.html', {'form':form})



@login_required(login_url='/home')
def create(request):

    print(request.GET)
    form = EmpForm()

    if request.method == 'POST':
        form = EmpForm(request.POST)
        if form.is_valid():
            #form.save()
            emp = Employee()
            emp.emp_name = form.cleaned_data['name']
            emp.emp_email = form.cleaned_data['email']
            emp.emp_address = form.cleaned_data['address']
            emp.save()
            return redirect(index)
    return  render(request, 'crud/create.html',{'form':form})

def index(request):

    #select * from emp
    resultSet = Employee.objects.raw('select * from emp')

    return render(request, 'crud/index.html', {'data':resultSet})


def update(request):

    #print(request.GET['id'])
    data = Employee.objects.get(emp_email = request.GET['email'])
    #print(data.emp_email)
    form = EmpForm(instance=data)

    if request.method == 'POST':
        form = EmpForm(request.POST, instance=data)
        if form.is_valid():
            #form.save()
            emp = Employee()
            emp.id = data.id
            emp.emp_name = form.cleaned_data['name']
            emp.emp_email = form.cleaned_data['email']
            emp.emp_address = form.cleaned_data['address']
            emp.save()
            return redirect(index)
    return render(request, 'crud/update.html', {'form': form})


def delete(request):

    row = Employee.objects.get(id=request.GET['id'])
    row.delete()
    return redirect(index)


def view(request):

    data = Employee.objects.get(id=request.GET['id'])
    return render(request, 'crud/view.html', {'data':data})



