from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ContactForm

# Create your views here.
def index(request):
	contact_form = ContactForm()

	context = {
		'data_contact':contact_form,
	}
	return render(request,'daftar/index.html',context,)

def get_name(request):
	if request.method == 'POST':
		contact_form = ContactForm(request.POST)
		if contact_form.is_valid():
				return HttpResponseRedirect("/blog/")
	else:
		contact_form = ContactForm()

	return render(request,'daftar/index.html',
		{'contact_form':contact_form})

	
		

	
