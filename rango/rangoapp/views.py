from django.shortcuts import render
from django.http import HttpResponse
from rangoapp.models import Category
from rangoapp.models import Page
from rangoapp.forms import CategoryForm

def index(request):
	category_list = Category.objects.order_by('-likes')[:5]
	context_dict = {'categories': category_list}
	return render(request, 'rangoapp/index.html', context_dict)

def category(request, category_name_slug):
	context_dict = {}
	try:
		category = Category.objects.get(slug=category_name_slug)
		context_dict['category_name'] = category.name
		context_dict['category'] = category
		pages = Page.objects.filter(category=category)
		context_dict['pages'] = pages
	except Category.DoesNotExist:
		pass
	return render(request, 'rangoapp/category.html', context_dict)


def add_category(request):

	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():

			form.save(commit=True)

			return index(request)
		else:
			print (form.errors)
	else:
	
		form = CategoryForm()
	return render(request,'rangoapp/add_category.html',{'form': form})	


