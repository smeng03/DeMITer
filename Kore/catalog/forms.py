from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProblemsForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProblemsForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            help_text = self.fields[field].help_text
            self.fields[field].help_text = None
            if help_text != '':
                self.fields[field].widget.attrs.update({'class':'has-popover', 'data-content':help_text, 'data-placement':'right', 'data-container':'body'})

    name = forms.CharField(max_length=80, label='Name', help_text='Choose your name')
    kerb = forms.CharField(max_length = 8, label='Kerberos', help_text='Choose your Kerberos ID')
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    SUPERSENIOR = 'SS'
    ALUM = 'AL'
    grad_year_choices = [(FRESHMAN, 'Freshman'), (SOPHOMORE, 'Sophomore'), (JUNIOR, 'Junior'), (SENIOR, 'Senior'), (SUPERSENIOR, 'Super Senior'), (ALUM, 'Alumni')]
    grad_year = forms.CharField(widget=forms.Select(choices=grad_year_choices), help_text='Choose your class', label="Class",)

    s_class_name = forms.CharField(max_length=20, label='Solved Problem Class No.', help_text='Enter the class no. as per catalog.mit.edu (e.g. 6.006)')
    s_assign_name = forms.IntegerField(label='Solved Problem Pset No.', help_text='Enter the problem set number (e.g. 1)')
    s_question_number = forms.IntegerField(label='Solved Problem Question No.', help_text='Enter the question which you have solved (e.g. 1)')

    u_class_name = forms.CharField(max_length=20, label='Unsolved Problem Class No.', help_text='Enter the class no. as per catalog.mit.edu (e.g. 6.006)')
    u_assign_name = forms.IntegerField(label='Unsolved Problem Pset No.', help_text='Enter the problem set number (e.g. 1)')
    u_question_number = forms.IntegerField(label='Unsolved Problem Question No.', help_text='Enter the question which you have solved (e.g. 1)')

    def clean_name(self):
        data = self.cleaned_data['name']
        return data
    def clean_kerb(self):
        data = self.cleaned_data['kerb']
        return data
    def clean_grad_year(self):
        data = self.cleaned_data['grad_year']
        return data
    def clean_s_class_name(self):
        data = self.cleaned_data['s_class_name']
        return data
    def clean_s_assign_name(self):
        data = self.cleaned_data['s_assign_name']
        return data
    def clean_s_question_number(self):
        data = self.cleaned_data['s_question_number']
        return data
    def clean_u_class_name(self):
        data = self.cleaned_data['u_class_name']
        return data
    def clean_u_assign_name(self):
        data = self.cleaned_data['u_assign_name']
        return data
    def clean_u_question_number(self):
        data = self.cleaned_data['u_question_number']
        return data