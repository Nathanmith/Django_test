from django.shortcuts import render

def index(request):
    return render(request, 'Home/home.html')

def contact(request):
	return render(request, 'Home/basic.html', {'stuff':['If you would to contact us, please email:','test@test.com']}) 