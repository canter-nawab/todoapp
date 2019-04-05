from django.shortcuts import render

# Create your views here.

#Create



#Update

#Delete

#List/Search

#Retrieve
def todo_detail_view(request,id=1):
	return render(request, "to_do/detail_view.html",{})


def todo_list_view(request):
	return render(request, "to_do/list_view.html",{})

