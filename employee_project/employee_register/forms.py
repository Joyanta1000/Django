from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
	
	class Meta:
		model = Employee
		#fields = '__all__'
		#if you want individual field
		fields = ('fullname','mobile','emp_code','position')
		labels = {'fullname':'Full Name','mobile':'Mobile Number','emp_code':'EMP. Code','position':'Emp. Position'}

	def __init__(self, *args, **kwargs):
		super(EmployeeForm,self).__init__(*args, **kwargs)
		self.fields['position'].empty_label = "Select"
		self.fields['emp_code'].required = False