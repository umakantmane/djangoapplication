from django.shortcuts import render
from student.forms import StudentForm

# Create your views here.


def createStudent(request):

    #print(request.method)
    #print(request.GET)
    print(request.POST)
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            pass
    return render(request, 'create.html', {'form':form})

def studentExample(request):

    data = {
        'name':'Raj1',
        'email':'raj@gmail.com',
        'phone':9986034800,
        'l1':[1,2,3,4,5],
        'd1':{'a':11, 'b':22}
    }
    print(data['name'])
    return render(request, 'stu.html',data)

#pip install django-cripsy-forms
def student2(request):
    return render(request, 'stu2.html')