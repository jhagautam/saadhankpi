from django import template
register = template.Library()
from datetime import date
from mainapp.models import sales_order
from django.db.models import Count, Sum , Avg, Max, Min
from django.http import HttpResponse
from django.template.defaulttags import register
import dateutil
from dateutil import parser
...
@register.filter
def get_item(dictionary, key):
    for a in dictionary:
    	if a.get('employee_designation')==key:
    		return a.get('employee_designation__count')
    return 0

@register.filter
def get_item2(dictionary, key):
    return dictionary[key]

@register.filter
def get_item4(dictionary, key):
    return dictionary.get('city')

@register.filter
def get_item5(dictionary, key):
    return dictionary.get('city__count')

@register.filter
def get_itemss(dictionary):
	ans=10
	if dictionary:
		print('print......',dictionary, type(dictionary))
		ans= dictionary['total_amount__sum']
	print('ans is ', ans)
	return ans



@register.simple_tag()
def solve ():
	# print('start date', date1)
	# if len(date1) == 0 and len(date2)==0:
	# 	return 100000
	# else:
	# date1='gautam'
	if request.method == 'POST':
		date1=request.POST['start_date']
		date2=request.POST['end_date']
	print('start date', date1)
		# date1=parser.parse(date1)
		# date2=parser.parse(date2)
		# q9=sales_order.objects.all()
		# e=q9.filter(order_date__range=[date1,date2]).aggregate(Sum('total_amount'))
		# return e.get('total_amount__sum')
	return 2000
	
@register.simple_tag
def function(a):
	return a