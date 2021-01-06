from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404,reverse
from django.conf import settings
from mainapp.models import *
from mainapp.forms import *
from django.db.models import Count, Sum , Avg, Max, Min
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory, modelformset_factory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import JsonResponse

class make_dictionary(dict):  
	def __init__(self): 
		self = dict()  
	def add(self, key, value): 
		self[key] = value


def solver(request):
	if request.method == 'POST':
		date1=request.POST['start_date']
		date2=request.POST['end_date']
		q=sales_order.objects.all()
		e=q.filter(order_date__range=[date1,date2]).aggregate(Sum('total_amount'))
		res= e.get('total_amount__sum')
		q2=purchase_order.objects.all()
		f=q2.filter(order_date__range=[date1,date2]).aggregate(Sum('total_amount'))
		res2= f.get('total_amount__sum')
		context1={'res':res, 'res2':res2}
		return JsonResponse(context1)

def home(request):
	context={'title':'Home'}
	return render(request,'mainapp/home.html',context)

def about(request):
	context={'title':'About'}
	return render(request,'mainapp/about.html',context)	

def services(request):
	context={'title':'Services'}
	return render(request,'mainapp/services.html',context)

def contact(request):
	context={'title':'Contact'}
	return render(request,'mainapp/contact.html',context)

@login_required
def add_data(request):
	firm = user_firm.objects.filter(user = request.user)
	if firm.exists():
		context={'title':'Application Home'}
		return render(request, 'mainapp/application.html', context)
	else:
		return redirect('user-firm')

@login_required
def dashboard(request):
	q1=designation.objects.annotate(Count('employee__employee_name')).filter(employee__employee_name__count__gt=0)
	q2=employee.objects.filter(sex='F').values('employee_designation').annotate(Count('employee_designation'))
	q3=employee.objects.filter(sex='M').values('employee_designation').annotate(Count('employee_designation'))
	q4=employee.objects.filter(sex='O').values('employee_designation').annotate(Count('employee_designation'))
	q5=product.objects.annotate(Sum('production_volume__amount')).filter(production_volume__amount__sum__gt=0)
	result=make_dictionary()
	for q in q5:
		k=q.product_category_id
		ky=product_category.objects.get(id=k)
		ky=ky.category_name
		ky=str(ky)
		if ky in result:
			y=int(q.production_volume__amount__sum)+int(result[ky])
			result.add(ky,y)
		else:
			y=int(q.production_volume__amount__sum)
			result.add(ky,y)
	q9=product.objects.annotate(Sum('sales_item__quantity')).filter(sales_item__quantity__sum__gt=0)
	result2=make_dictionary()
	for q in q9:
		k=q.product_category_id
		ky=product_category.objects.get(id=k)
		ky=ky.category_name
		ky=str(ky)
		if ky in result2:
			y=int(q.sales_item__quantity__sum)+int(result2[ky])
			result2.add(ky,y)
		else:
			y=int(q.sales_item__quantity__sum)
			result2.add(ky,y)

	q10=product.objects.annotate(Sum('sales_item__total')).filter(sales_item__total__sum__gt=0)
	result3=make_dictionary()
	for q in q10:
		k=q.product_category_id
		ky=product_category.objects.get(id=k)
		ky=ky.category_name
		ky=str(ky)
		if ky in result3:
			y=int(q.sales_item__total__sum)+int(result3[ky])
			result3.add(ky,y)
		else:
			y=int(q.sales_item__total__sum)
			result3.add(ky,y)
	q11=product.objects.annotate(Sum('purchase_item__quantity')).filter(purchase_item__quantity__sum__gt=0)
	result4=make_dictionary()
	for q in q11:
		k=q.product_category_id
		ky=product_category.objects.get(id=k)
		ky=ky.category_name
		ky=str(ky)
		if ky in result4:
			y=int(q.purchase_item__quantity__sum)+int(result4[ky])
			result4.add(ky,y)
		else:
			y=int(q.purchase_item__quantity__sum)
			result4.add(ky,y)

	q12=product.objects.annotate(Sum('purchase_item__total')).filter(purchase_item__total__sum__gt=0)
	result5=make_dictionary()
	for q in q12:
		k=q.product_category_id
		ky=product_category.objects.get(id=k)
		ky=ky.category_name
		ky=str(ky)
		if ky in result5:
			y=int(q.purchase_item__total__sum)+int(result5[ky])
			result5.add(ky,y)
		else:
			y=int(q.purchase_item__total__sum)
			result5.add(ky,y)
	q6=machines.objects.annotate(Sum('maintenance_cost__cost')).filter(maintenance_cost__cost__sum__gt=0)
	q7=machines.objects.annotate(Sum('maintenance_cost__days_engaged')).filter(maintenance_cost__days_engaged__sum__gt=0)
	q8=machines.objects.all()
	customer_city_wise=customer.objects.values('city').annotate(Count('city'))
	total_customer=customer.objects.all().count()
	vendor_city_wise=vendor.objects.values('city').annotate(Count('city'))
	total_vendor=vendor.objects.all().count()
	total_employee=employee.objects.all().count()
	total_female_employee=employee.objects.filter(sex='F').count()
	total_male_employee=employee.objects.filter(sex='M').count()
	total_other_employee=employee.objects.filter(sex='O').count()
	total_production=production_volume.objects.aggregate(Sum('amount'))
	total_maintenance_cost=maintenance_cost.objects.aggregate(Sum('cost'))
	total_days_engaged=maintenance_cost.objects.aggregate(Sum('days_engaged'))
	total_machines=machines.objects.all().count()
	context={'q1':q1,'q2':q2, 'q3':q3, 'q4':q4, 'result':result,'q6':q6,'q7':q7,'q8':q8,'result2':result2,'result3':result3,'result4':result4,'result5':result5,'vendor_city_wise':vendor_city_wise,'total_vendor':total_vendor, 'total_female_employee':total_female_employee,'total_employee':total_employee,'total_male_employee':total_male_employee,'total_other_employee':total_other_employee,'total_production':total_production,'total_maintenance_cost':total_maintenance_cost,'total_days_engaged':total_days_engaged,'total_machines':total_machines,'customer_city_wise':customer_city_wise,'total_customer':total_customer}
	return render(request, 'mainapp/dashboard.html', context)

@login_required
def update_employee(request):
	employees=employee.objects.all()
	context={'employees':employees,'title':'Update Employee'}
	return render(request, 'mainapp/update_employee.html', context)

@login_required
def add_employee(request):
	form=employee_form()
	if request.method == 'POST':
		form=employee_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/update_employee/')
	context={'form':form,'title':'Add Employee'}
	return render(request, 'mainapp/add_employee.html', context)

@login_required
def edit_employee(request, pk):
	m=employee.objects.get(id=pk)
	form=employeeForm(instance=m)
	if request.method == 'POST':
		form=employeeForm(request.POST,instance=m)
		if form.is_valid():
			form.save()
			return redirect('/update_employee/')

	context={'form':form}
	return render(request, 'mainapp/add_employee.html', context)

def signup(request):
	if request.method == 'POST':
		form = user_form(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		form = user_form()
	return render(request,'mainapp/register.html',{'form':form,'title':'Sign Up'})

@login_required
def user_firm_create_form(request):
	form = user_firm_form()
	if request.method == 'POST':
		form = user_firm_form(request.POST)
		if form.is_valid():
			response = form.save(commit=False)
			response.user = request.user
			response.save()
			return redirect('login')
	return render(request,'mainapp/userfirm.html',{'form':form,'title':'Create User Firm'})

@login_required
def sales_order_create_form(request):
	#item_formset = inlineformset_factory(sales_order,sales_item,form=sales_item_form,extra=0)
	if request.method == 'POST':
		order_form = sales_order_form(request.user,request.POST)
		#item_form = item_formset(request.POST,form_kwargs={'user':request.user})
		if order_form.is_valid():
			response = order_form.save(commit=False)
			response.firm = user_firm.objects.get(user=request.user)
			response.save()
			return redirect('sales-order-edit',pk=response.id)
	# HttpResponseRedirect(sales_order.get_absolute_url())
	else:
		order_form = sales_order_form(request.user)
		#item_form = item_formset(form_kwargs={'user':request.user})
	context = {'o_form':order_form,'title':'Sales Order'}#,'i_form':item_form}
	return render(request,'mainapp/sales_order.html',context)

def create_designation(request):
	form=createdesignation()
	if request.method == 'POST':
		form=createdesignation(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/update_employee/')
	context={'form':form}
	return render(request, 'mainapp/create_designation.html', context)

@login_required
def sales_order_edit_form(request,pk):
	sales_order_instance = sales_order.objects.get(id=pk)
	order_formset = modelformset_factory(sales_order,form=sales_order_form,extra=0,can_delete=False,max_num=1)
	item_formset = inlineformset_factory(sales_order,sales_item,form=sales_item_form,extra=1,)
	#remove save button from create order, redirect add item to edit order
	if request.method == 'POST':
		if 'add_item' in request.POST:
			#order_form = order_formset(request.POST,queryset=sales_order.objects.get(pk=order_id),form_kwargs={'user':request.user})
			item_form = item_formset(request.POST,form_kwargs={'user':request.user},instance=sales_order_instance)
			if item_form.is_valid():
				instances = item_form.save(commit=False)
				for instance in instances:
					category = instance.product.product_category
					instance.gst_rate = category.gst_rate
					instance.total = instance.price*instance.quantity*(100+instance.gst_rate)/100
					instance.save()
				sales_item_set = sales_item.objects.filter(sales_order=sales_order_instance)
				sales_order_instance.total_amount=0
				for item in sales_item_set:
					sales_order_instance.total_amount += item.total
				sales_order_instance.save()
				return redirect('sales-order-edit',pk=pk)

		if 'save' in request.POST:
			order_form = order_formset(request.POST,queryset=sales_order.objects.filter(id=pk),form_kwargs={'user':request.user})
			item_form = item_formset(request.POST,form_kwargs={'user':request.user},instance=sales_order_instance)
			if item_form.is_valid() and order_form.is_valid():
				instances = item_form.save(commit=False)
				order_form.save()
				for instance in instances:
					category = instance.product.product_category
					instance.gst_rate = category.gst_rate
					instance.total = instance.price*instance.quantity*(100+instance.gst_rate)/100
					instance.save()
				sales_item_set = sales_item.objects.filter(sales_order=sales_order_instance)
				sales_order_instance.total_amount=0
				for item in sales_item_set:
					sales_order_instance.total_amount += item.total
				sales_order_instance.save()
				return redirect('sales-order-view',user_id=request.user.id)
	# HttpResponseRedirect(sales_order.get_absolute_url())
	else:
		order_form = order_formset(queryset=sales_order.objects.filter(id=pk),form_kwargs={'user':request.user})
		item_form = item_formset(form_kwargs={'user':request.user},instance=sales_order_instance)
	context = {'o_form':order_form,'i_form':item_form,'title':'Sales Order'}
	return render(request,'mainapp/sales_order_edit.html',context)

@login_required
def purchase_order_create_form(request):
	if request.method == 'POST':
		order_form = purchase_order_form(request.user,request.POST)
		#item_form = item_formset(request.POST,form_kwargs={'user':request.user})
		if order_form.is_valid():
			response = order_form.save(commit=False)
			response.firm = user_firm.objects.get(user=request.user)
			response.save()
			return redirect('purchase-order-edit',pk=response.id)
	# HttpResponseRedirect(sales_order.get_absolute_url())
	else:
		order_form = purchase_order_form(request.user)
		#item_form = item_formset(form_kwargs={'user':request.user})
	context = {'o_form':order_form,'title':'Purchase Order'}
	return render(request,'mainapp/sales_order.html',context)

@login_required
def purchase_order_edit_form(request,pk):
	purchase_order_instance = purchase_order.objects.get(id=pk)
	order_formset = modelformset_factory(purchase_order,form=purchase_order_form,extra=0,can_delete=False,max_num=1)
	item_formset = inlineformset_factory(purchase_order,purchase_item,form=purchase_item_form,extra=1,)
	#remove save button from create order, redirect add item to edit order
	if request.method == 'POST':
		if 'add_item' in request.POST:
			#order_form = order_formset(request.POST,queryset=sales_order.objects.get(pk=order_id),form_kwargs={'user':request.user})
			item_form = item_formset(request.POST,form_kwargs={'user':request.user},instance=purchase_order_instance)
			if item_form.is_valid():
				instances = item_form.save(commit=False)
				for instance in instances:
					category = instance.product.product_category
					instance.gst_rate = category.gst_rate
					instance.total = instance.price*instance.quantity*(100+instance.gst_rate)/100
					instance.save()
				purchase_item_set = purchase_item.objects.filter(purchase_order=purchase_order_instance)
				purchase_order_instance.total_amount=0
				for item in purchase_item_set:
					purchase_order_instance.total_amount += item.total
				purchase_order_instance.save()
				return redirect('purchase-order-edit',pk=pk)

		if 'save' in request.POST:
			order_form = order_formset(request.POST,queryset=purchase_order.objects.filter(id=pk),form_kwargs={'user':request.user})
			item_form = item_formset(request.POST,form_kwargs={'user':request.user},instance=purchase_order_instance)
			if item_form.is_valid() and order_form.is_valid():
				instances = item_form.save(commit=False)
				order_form.save()
				for instance in instances:
					category = instance.product.product_category
					instance.gst_rate = category.gst_rate
					instance.total = instance.price*instance.quantity*(100+instance.gst_rate)/100
					instance.save()
				purchase_item_set = purchase_item.objects.filter(purchase_order=purchase_order_instance)
				purchase_order_instance.total_amount=0
				for item in purchase_item_set:
					purchase_order_instance.total_amount += item.total
				purchase_order_instance.save()
				return redirect('purchase-order-view',user_id=request.user.id)
	# HttpResponseRedirect(sales_order.get_absolute_url())
	else:
		order_form = order_formset(queryset=purchase_order.objects.filter(id=pk),form_kwargs={'user':request.user})
		item_form = item_formset(form_kwargs={'user':request.user},instance=purchase_order_instance)
	context = {'o_form':order_form,'i_form':item_form,'title':'Purchase Order'}
	return render(request,'mainapp/sales_order_edit.html',context)

class ProductListView(LoginRequiredMixin, ListView):
	model = product
	template_name = 'mainapp/product_list.html'
	context_object_name = 'item'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'List of Products'
		return context

	def get_queryset(self, *args, **kwargs):
		user = get_object_or_404(User, id=self.kwargs['user_id'])
		firm = user_firm.objects.get(user = user)
		return product.objects.filter(firm=firm).order_by('product_name')

class ProductCreateView(LoginRequiredMixin, CreateView):
	template_name = 'mainapp/create_view.html'
	form_class = items_producedForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Create Product'
		return context

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)
	
	def get_form_kwargs(self):
		kwargs = super(ProductCreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

class ProductDetailView(LoginRequiredMixin,DetailView):
	model = product
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['items'] = sales_item.objects.filter(product=self.object)
		context['purchaseitems'] = purchase_item.objects.filter(product=self.object)
		context['title'] = 'Product Details'
		return context

class ProductionVolumeCreateView(LoginRequiredMixin, CreateView):
	template_name = 'mainapp/create_view.html'
	form_class = production_volumeForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Update Production Volume'
		return context

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)
	
	def get_form_kwargs(self):
		kwargs = super(ProductionVolumeCreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = product
	template_name = 'mainapp/edit_view.html'
	fields = ['product_name','product_description','product_category']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Update Product Details'
		return context

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = product
	template_name = 'mainapp/delete_view.html'

	def get_context_data(self, **kwargs):
			context = super().get_context_data(**kwargs)
			context['title'] = 'Delete Product'
			return context

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

	def get_success_url(self):
		return reverse('products',kwargs={'user_id':self.request.user.id})	

class ProductCategoryListView(LoginRequiredMixin, ListView):
	model = product_category
	template_name = 'mainapp/product_category.html'
	context_object_name = 'item'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'List of Product Categories'
		return context

	def get_queryset(self, *args, **kwargs):
		user = get_object_or_404(User, id=self.kwargs['user_id'])
		firm = user_firm.objects.get(user = user)
		return product_category.objects.filter(firm=firm).order_by('category_name')

class ProductCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = product_category
	template_name = 'mainapp/edit_view.html'
	fields = ['category_name','gst_rate','remarks']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Update Product Category Details'
		return context

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

class ProductCategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = product_category
	template_name = 'mainapp/delete_view.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Delete Product Category'
		return context

	def get_success_url(self):
		return reverse('product-category-view',kwargs={'user_id':self.request.user.id})

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

class ProductCategoryCreateView(LoginRequiredMixin, CreateView):
	model = product_category
	template_name = 'mainapp/create_view.html'
	fields = ['category_name','gst_rate','remarks']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Create New Product category'
		return context

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)

class SalesOrderListView(LoginRequiredMixin, ListView):
	model = sales_order
	template_name = 'mainapp/sales_order_view.html'
	context_object_name = 'item'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Sales Order List'
		return context

	def get_queryset(self, *args, **kwargs):
		user = get_object_or_404(User, id=self.kwargs['user_id'])
		firm = user_firm.objects.get(user = user)
		return sales_order.objects.filter(firm=firm).order_by('-order_date')

class SalesOrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = sales_order
	template_name = 'mainapp/delete_view.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Delete Sales Order'
		return context

	def get_success_url(self):
		return reverse('sales-order-view',kwargs={'user_id':self.request.user.id})

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

class SalesOrderDetailView(LoginRequiredMixin,DetailView):
	model = sales_order
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['items'] = sales_item.objects.filter(sales_order=self.object)
		context['title'] = 'Sales Order Details'
		return context

class PurchaseOrderListView(LoginRequiredMixin, ListView):
	model = purchase_order
	template_name = 'mainapp/purchase_order_view.html'
	context_object_name = 'item'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Purchase Order List'
		return context

	def get_queryset(self, *args, **kwargs):
		user = get_object_or_404(User, id=self.kwargs['user_id'])
		firm = user_firm.objects.get(user = user)
		return purchase_order.objects.filter(firm=firm).order_by('-order_date')

class PurchaseOrderDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = purchase_order
	template_name = 'mainapp/delete_view.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Delete Purchase Order'
		return context

	def get_success_url(self):
		return reverse('purchase-order-view',kwargs={'user_id':self.request.user.id})

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

class PurchaseOrderDetailView(LoginRequiredMixin,DetailView):
	model = purchase_order
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['items'] = purchase_item.objects.filter(purchase_order=self.object)
		context['title'] = 'Purchase Order Details'
		return context

class CustomerListView(LoginRequiredMixin, ListView):
	model = customer
	template_name = 'mainapp/customer_list.html'
	context_object_name = 'item'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Customers'
		return context

	def get_queryset(self, *args, **kwargs):
		user = get_object_or_404(User, id=self.kwargs['user_id'])
		firm = user_firm.objects.get(user = user)
		return customer.objects.filter(firm=firm).order_by('firm_name')

class CustomerCreateView(LoginRequiredMixin, CreateView):
	template_name = 'mainapp/create_view.html'
	form_class = customer_form

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Add New Customer'
		return context

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)

class CustomerUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = customer
	template_name = 'mainapp/edit_view.html'
	fields = ['firm_name','gstin','contact_person','primary_contact_number','secondary_contact_number',
					'email_address','street_address','pin_code','city','district','state','remarks']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Update Customer Details'
		return context

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

class CustomerDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = customer
	template_name = 'mainapp/delete_view.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Delete Customer'
		return context

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

	def get_success_url(self):
		return reverse('customer-list',kwargs={'user_id':self.request.user.id})

class CustomerDetailView(LoginRequiredMixin,DetailView):
	model = customer
		
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['items'] = sales_order.objects.filter(customer=self.object)
		context['title'] = 'Customer Details'
		return context

class VendorListView(LoginRequiredMixin, ListView):
	model = vendor
	template_name = 'mainapp/vendor_list.html'
	context_object_name = 'item'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Vendors'
		return context

	def get_queryset(self, *args, **kwargs):
		user = get_object_or_404(User, id=self.kwargs['user_id'])
		firm = user_firm.objects.get(user = user)
		return vendor.objects.filter(firm=firm).order_by('firm_name')

class VendorCreateView(LoginRequiredMixin, CreateView):
	template_name = 'mainapp/create_view.html'
	form_class = vendor_form

	def get_context_data(self, **kwargs):
			context = super().get_context_data(**kwargs)
			context['title'] = 'Add New Vendor'
			return context

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)

class VendorUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = vendor
	template_name = 'mainapp/edit_view.html'
	fields = ['firm_name','gstin','contact_person','primary_contact_number','secondary_contact_number',
					'email_address','street_address','pin_code','city','district','state','remarks']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Update Vendor Details'
		return context

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

class VendorDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = vendor
	template_name = 'mainapp/delete_view.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Delete Vendor'
		return context

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

	def get_success_url(self):
		return reverse('vendor-list',kwargs={'user_id':self.request.user.id})

class VendorDetailView(LoginRequiredMixin,DetailView):
	model = vendor
		
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['items'] = purchase_order.objects.filter(vendor=self.object)
		context['title'] = 'Vendor Details'
		return context

class MachineListView(LoginRequiredMixin, ListView):
	model = machines
	template_name = 'mainapp/machine_list.html'
	context_object_name = 'item'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Machines'
		return context

	def get_queryset(self, *args, **kwargs):
		user = get_object_or_404(User, id=self.kwargs['user_id'])
		firm = user_firm.objects.get(user = user)
		return machines.objects.filter(firm=firm).order_by('machine_name')

class MachineCreateView(LoginRequiredMixin, CreateView):
	template_name = 'mainapp/create_view.html'
	form_class = machineForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Add New Machine'
		return context

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)

class MachineUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = machines
	template_name = 'mainapp/edit_view.html'
	fields = ['machine_name','machine_count','operator']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Update Machine Details'
		return context

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

class MachineDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = machines
	template_name = 'mainapp/delete_view.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Delete Machine'
		return context

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

	def get_success_url(self):
		return reverse('machine-list',kwargs={'user_id':self.request.user.id})

class MachineDetailView(LoginRequiredMixin,DetailView):
	model = machines
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['items'] = maintenance_cost.objects.filter(machine=self.object)
		context['title'] = 'Machine Details'
		return context

class MaintenanceListView(LoginRequiredMixin, ListView):
	model = maintenance_cost
	template_name = 'mainapp/maintenance_list.html'
	context_object_name = 'item'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Maintenance'
		return context

	def get_queryset(self, *args, **kwargs):
		user = get_object_or_404(User, id=self.kwargs['user_id'])
		firm = user_firm.objects.get(user = user)
		return maintenance_cost.objects.filter(firm=firm).order_by('-date')

class MaintenanceCreateView(LoginRequiredMixin, CreateView):
	template_name = 'mainapp/create_view.html'
	form_class = maintenance_costForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Create Maintenance Record'
		return context

	def get_form_kwargs(self):
		kwargs = super(MaintenanceCreateView, self).get_form_kwargs()
		kwargs['user'] = self.request.user
		return kwargs

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)

class MaintenanceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = maintenance_cost
	template_name = 'mainapp/edit_view.html'
	fields = ['machine','cost','days_engaged']

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Edit Maintenance Record'
		return context

	def form_valid(self,form):
		form.instance.firm = user_firm.objects.get(user=self.request.user)
		return super().form_valid(form)

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

class MaintenanceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = maintenance_cost
	template_name = 'mainapp/delete_view.html'
	
	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Delete Maintenance Record'
		return context

	def test_func(self):
		category = self.get_object()
		if category.firm.user == self.request.user:
			return True
		return False

	def get_success_url(self):
		return reverse('maintenance-list',kwargs={'user_id':self.request.user.id})

#