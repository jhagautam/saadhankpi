from django.forms import ModelForm
from .models import *
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.forms.widgets import SplitDateTimeWidget
from django import forms
from django.contrib.auth.forms import UserCreationForm

#designation creation form
class createmessage(ModelForm):
	class Meta:
		model=contactus
		fields='__all__'

class createdesignation(ModelForm):
	class Meta:
		model=designation
		fields='__all__'
		# exclude= ('firm',)

#machine creation form
class machineForm(ModelForm):
	class Meta:
		model=machines
		exclude= ('firm',)

#employee creation form
class employee_form(ModelForm):
	class Meta:
		model = employee
		exclude= ()

#product creation form
class items_producedForm(ModelForm):
	class Meta:
		model=product
		exclude= ('firm',)

	def __init__(self, user, *args, **kwargs):
		super(items_producedForm, self).__init__(*args, **kwargs)
		current_firm = user_firm.objects.get(user=user)
		self.fields['product_category'].queryset = product_category.objects.filter(firm=current_firm)

#production volume addition form
class production_volumeForm(ModelForm):
	class Meta:
		model=production_volume
		exclude = ('firm',)

	def __init__(self, user, *args, **kwargs):
		super(production_volumeForm, self).__init__(*args, **kwargs)
		current_firm = user_firm.objects.get(user=user)
		self.fields['item'].queryset = product.objects.filter(firm=current_firm)

#maintenance cost addition form
class maintenance_costForm(ModelForm):
	class Meta:
		model=maintenance_cost
		exclude= ('firm',)

	def __init__(self, user, *args, **kwargs):
		super(maintenance_costForm, self).__init__(*args, **kwargs)
		current_firm = user_firm.objects.get(user=user)
		self.fields['machine'].queryset = machines.objects.filter(firm=current_firm)

#product category creation form
class product_category_form(ModelForm):
	class Meta:
		model = product_category
		exclude = ('firm',)

#user registration form
class user_form(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password1','password2']

#customer creation form
class customer_form(ModelForm):
	class Meta:
		model = customer
		fields = ['firm_name','gstin','contact_person','primary_contact_number','secondary_contact_number',
					'email_address','street_address','pin_code','city','district','state','remarks']

#vendor creation form
class vendor_form(ModelForm):
	class Meta:
		model = vendor
		fields = ['firm_name','gstin','contact_person','primary_contact_number','secondary_contact_number',
					'email_address','street_address','pin_code','city','district','state','remarks']

#user firm creation form
class user_firm_form(ModelForm):
	class Meta:
		model = user_firm
		fields = ['firm_name','gstin','contact_person','primary_contact_number','secondary_contact_number',
					'email_address','street_address','pin_code','city','district','state',]

#sales order creation form
class sales_order_form(ModelForm):
	order_date = forms.SplitDateTimeField(initial=timezone.now())
	
	class Meta:
		model = sales_order
		fields = ['customer','order_date','freight','remarks']
		widgets = {'order_date':SplitDateTimeWidget(date_attrs={'type':'date'},time_attrs={'type':'time'})}

	def __init__(self, user, *args, **kwargs):
		super(sales_order_form, self).__init__(*args, **kwargs)
		current_firm = user_firm.objects.get(user=user)
		self.fields['customer'].queryset = customer.objects.filter(firm=current_firm)

#sales item creation form
class sales_item_form(ModelForm):
	class Meta:
		model = sales_item
		exclude = ('sales_order','gst_rate','total',)
	
	def __init__(self, user, *args, **kwargs):
		super(sales_item_form, self).__init__(*args, **kwargs)
		current_firm = user_firm.objects.get(user=user)
		self.fields['product'].queryset = product.objects.filter(firm=current_firm)

#purchase order creation form
class purchase_order_form(ModelForm):
	order_date = forms.SplitDateTimeField(initial=timezone.now())
	
	class Meta:
		model = purchase_order
		fields = ['vendor','order_date','freight','remarks']
		widgets = {'order_date':SplitDateTimeWidget(date_attrs={'type':'date'},time_attrs={'type':'time'})}

	def __init__(self, user, *args, **kwargs):
		super(purchase_order_form, self).__init__(*args, **kwargs)
		current_firm = user_firm.objects.get(user=user)
		self.fields['vendor'].queryset = vendor.objects.filter(firm=current_firm)

#purchase item creation form
class purchase_item_form(ModelForm):
	class Meta:
		model = purchase_item
		exclude = ('purchase_order','gst_rate','total',)
	
	def __init__(self, user, *args, **kwargs):
		super(purchase_item_form, self).__init__(*args, **kwargs)
		current_firm = user_firm.objects.get(user=user)
		self.fields['product'].queryset = product.objects.filter(firm=current_firm)