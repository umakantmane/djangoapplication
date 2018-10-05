from django import forms

from crud.models import Employee,EmployeeEducation



# class EmpDucationForm(forms.ModelForm):
#
#     class Meta:
#         model = EmployeeEducation
#         fields = '__all__'

class EmpDucationForm(forms.ModelForm):

    email = forms.EmailField()
    class Meta:

        model = EmployeeEducation
        fields = '__all__'


class EmpForm(forms.Form):
    name = forms.CharField(
        min_length=8,
        max_length=20,
        label='Employee name'
    )
    email = forms.EmailField()
    address = forms.CharField()
    # class Meta:
    #     model = Employee
    #     #fields = '__all__'
    #     fields = ('emp_name', 'emp_email', 'emp_address')

    def clean(self):
        form_data = self.cleaned_data
        if 'name' in form_data:

            if form_data['name'].isdigit():
                self.errors['name'] = ['invalid name']

        return form_data


class EmpForm2(forms.Form):

    emp_name = forms.CharField()
    emp_email = forms.EmailField()
    emp_address = forms.CharField()





