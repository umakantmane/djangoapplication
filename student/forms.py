from django import forms
from django.core.validators import ValidationError

#
# def validateEmail(email_address):
#
#     if email_address.find('mytectra.com') <0:
#         raise ValidationError("please provide mytectra.com email only!")
#
# def validateName(name):
#
#     if name.isdigit():
#         raise ValidationError("Invalid name!")


class StudentForm(forms.Form):

    city = (
        ('a', '--Select option--'),
        ('cn','Chennai'),
        ('hyd', 'Hyderabad'),
        ('bnc', 'Banagalore')
    )
    gn = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    stu_name = forms.CharField(
        min_length=8,
        max_length=20,
        required=True,
        label="Username"
    )
    email = forms.EmailField(help_text="Please give valie name")
    stu_city = forms.ChoiceField(choices=city)
    gender = forms.ChoiceField(choices=gn, widget=forms.RadioSelect)
    address = forms.CharField(max_length=250, widget=forms.Textarea)
    is_active = forms.CharField(widget=forms.CheckboxInput, required=True)
    multi = forms.MultipleChoiceField(help_text="some message",choices=city, widget=forms.CheckboxSelectMultiple)
    file = forms.FileField()

    def clean(self):

        form_data = self.cleaned_data

        if 'stu_name' in form_data:

            if form_data['stu_name'].isdigit():
                self.errors['stu_name'] = ['Invalid given user name!']

        if 'email' in form_data:
            if form_data['email'].find('mytectra.com')<0:
                self.errors['email'] = ['Invalid Email(Hint=>myteract.com)']

        return  form_data