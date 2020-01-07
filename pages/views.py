from django.http import HttpResponse

from django.shortcuts import render

# views handles our various web pages

# Create your views here.

def homepage_view(request, *args, **kwargs): # contains the main landing page
	#return HttpResponse("<h1>This is the home page!</h1>") # HttpResponse allows passed in html code to be rendered properly
	return render(request, "home.html", {}) # this is a better way to render html, we get it from a django template!

def products_view(request, *args, **kwargs): # contains product info
	return render(request, "products.html", {})

def contact_view(request, *args, **kwargs): # contains contact info
	return render(request, "contact.html", {})

def order_view(request, *args, **kwargs): # contains mission statement
	return render(request, "order.html", {})





