from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
#-------------------------------------ss-
#--------------------------------------
# Create your views here.

def Mila(request):
	
	return render(request, 'Inicio/Mila.html')
