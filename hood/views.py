from django.shortcuts import render,redirect, get_object_or_404

# Create your views here.
def index(request):
    '''View function to return the index page and all of its data'''
    
    return render(request, 'index.html')
    
