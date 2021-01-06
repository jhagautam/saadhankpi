from django.db import models
from django.utils import timezone
from django.utils.encoding import smart_text
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.urls import reverse

class User(AbstractUser):
	is_admin = models.BooleanField(default=True)

class user_firm(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	firm_name = models.CharField(max_length=100)
	gstin = models.CharField(max_length=15,unique=True,null=True)
	contact_person = models.CharField(max_length=50)
	primary_contact_number = models.BigIntegerField(unique=True)
	secondary_contact_number = models.BigIntegerField(null=True,unique=True)
	email_address = models.EmailField(unique=True,null=True)
	street_address = models.TextField(max_length=250)
	pin_code = models.IntegerField()
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	remarks = models.TextField(max_length=250,null=True,blank=True)
	
	def __str__(self):
		return self.firm_name

class designation(models.Model):
	firm = models.ForeignKey(user_firm,blank=True,on_delete=models.CASCADE)
	designation_name=models.CharField(max_length=50)
	def __str__(self):
		return self.designation_name

class employee(models.Model):
	SEX=(
	('M','Male'),
	('F','Female'),('O','Other')
	)
	# user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
	employee_name=models.CharField(max_length=10)
	firm = models.ForeignKey(user_firm,blank=True,on_delete=models.CASCADE)
	employee_designation=models.ForeignKey('designation',null=True, on_delete=models.SET_NULL)
	sex=models.CharField(max_length=6, choices=SEX, null=True)
	
	class Meta:
		permissions = []

	def __str__(self):
		return self.employee_name

class product_category(models.Model):
	firm = models.ForeignKey(user_firm,blank=True,on_delete=models.CASCADE)
	category_name = models.CharField(max_length=50)
	gst_rate = models.PositiveSmallIntegerField()
	remarks = models.CharField(max_length=50)

	def __str__(self):
		return f'{self.category_name} ({self.gst_rate}% - GST)'

	def get_absolute_url(self):
		return reverse('product-category-view',kwargs={'user_id':self.firm.user.id},)

class product(models.Model):
	firm = models.ForeignKey(user_firm,blank=True,on_delete=models.CASCADE)
	product_name=models.CharField(max_length=50,help_text='Product name here')
	product_description = models.CharField(max_length=150,help_text='Write something about the product here')
	product_category = models.ForeignKey(product_category,on_delete=models.CASCADE)
	
	def __str__(self):
		return self.product_name

	def get_absolute_url(self):
		return reverse('products',kwargs={'user_id':self.firm.user.id},)

class KPIList(models.Model):
	firm = models.ForeignKey(user_firm,blank=True,on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	target=models.IntegerField()
	def __str__(self):
		return self.name

class production_volume(models.Model):
	firm = models.ForeignKey(user_firm,blank=True,on_delete=models.CASCADE)
	item=models.ForeignKey(product,null=True, on_delete=models.CASCADE)
	amount=models.IntegerField()
	data_updated=models.DateField(auto_now_add=True, null=True)
	def __str__(self):
		return self.item.item_name

class machines(models.Model):
	firm = models.ForeignKey(user_firm,blank=True,on_delete=models.CASCADE)
	machine_name=models.CharField(max_length=50)
	machine_count=models.IntegerField()
	operator=models.ForeignKey(employee,null=True,on_delete=models.SET_NULL,blank=True)
	
	def get_absolute_url(self):
		return reverse('machine-list',kwargs={'user_id':self.firm.user.id},)

	def __str__(self):
		return self.machine_name
		
class maintenance_cost(models.Model):
	firm = models.ForeignKey(user_firm,blank=True,on_delete=models.CASCADE)
	machine=models.ForeignKey(machines,null=False, on_delete=models.CASCADE)
	cost=models.IntegerField()
	days_engaged=models.IntegerField()
	date=models.DateTimeField(auto_now_add=True, null=True)
	
	def get_absolute_url(self):
		return reverse('maintenance-list',kwargs={'user_id':self.firm.user.id},)

	def __str__(self):
		return f"{self.machine.machine_name}'s Maintenance Record"

class customer(models.Model):
	firm = models.ForeignKey(user_firm,blank=True,on_delete=models.CASCADE)
	firm_name = models.CharField(max_length=100)
	gstin = models.CharField(max_length=15,unique=True,null=True)
	contact_person = models.CharField(max_length=50)
	primary_contact_number = models.BigIntegerField(unique=True)
	secondary_contact_number = models.BigIntegerField(null=True,unique=True)
	email_address = models.EmailField(unique=True,null=True)
	street_address = models.TextField(max_length=250)
	pin_code = models.IntegerField()
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	remarks = models.TextField(max_length=250,null=True,blank=True)

	def get_absolute_url(self):
		return reverse('customer-list',kwargs={'user_id':self.firm.user.id},)
	
	def __str__(self):
		return self.firm_name

class vendor(models.Model):
	firm = models.ForeignKey(user_firm,blank=True,on_delete=models.CASCADE)
	firm_name = models.CharField(max_length=100)
	gstin = models.CharField(max_length=15,unique=True,null=True)
	contact_person = models.CharField(max_length=50)
	primary_contact_number = models.BigIntegerField(unique=True)
	secondary_contact_number = models.BigIntegerField(null=True,unique=True)
	email_address = models.EmailField(unique=True,null=True)
	street_address = models.TextField(max_length=250)
	pin_code = models.IntegerField()
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	remarks = models.TextField(max_length=250,null=True,blank=True)

	def get_absolute_url(self):
		return reverse('vendor-list',kwargs={'user_id':self.firm.user.id},)

	def __str__(self):
		return self.firm_name

class sales_order(models.Model):
	customer = models.ForeignKey(customer,on_delete=models.CASCADE)
	order_date = models.DateTimeField(default=timezone.now)
	firm = models.ForeignKey(user_firm,blank=True,on_delete=models.CASCADE)
	freight = models.PositiveIntegerField()
	remarks = models.CharField(max_length=100, default='N/A')
	total_amount = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.customer}'s Order"
	
	def get_absolute_url(self):
		return reverse('sales-order-view',kwargs={'user_id':self.firm.user.id})

class purchase_order(models.Model):
	vendor = models.ForeignKey(vendor,on_delete=models.CASCADE)
	order_date = models.DateTimeField(default=timezone.now)
	firm = models.ForeignKey(user_firm,blank=True,on_delete=models.CASCADE)
	freight = models.PositiveIntegerField()
	remarks = models.CharField(max_length=100, default='N/A')
	total_amount = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.vendor}'s Order"

class sales_item(models.Model):
	sales_order = models.ForeignKey(sales_order,on_delete=models.CASCADE)
	product = models.ForeignKey(product,on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()
	price = models.PositiveIntegerField()
	gst_rate = models.PositiveSmallIntegerField(default = 0)
	total = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f'{self.sales_order} - Item - {self.product}'

class purchase_item(models.Model):
	purchase_order = models.ForeignKey(purchase_order,on_delete=models.CASCADE)
	product = models.ForeignKey(product,on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField()
	price = models.PositiveIntegerField()
	gst_rate = models.PositiveSmallIntegerField(default = 0)
	total = models.PositiveIntegerField(default=0)
	
	def __str__(self):
		return f'{self.sales_order} - Item - {self.product}'

# not to be used; not deleting it as it causes some error
class items_produced(models.Model):
	item_name=models.CharField(max_length=50)
	def __str__(self):
		return self.item_name
