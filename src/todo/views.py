from django.shortcuts import render

#retrieve
#GET-- templates home.html
def home(request):
	return render(request, "home.html", {})