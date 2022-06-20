from django.shortcuts import render

# Create your views here.
def index(request):
    '''View function to return the index page and all of its data'''
    
    return render(request, 'index.html')
    
