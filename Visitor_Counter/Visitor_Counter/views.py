from django.shortcuts import render


def visitor(request):
    info={
        'name':['raj','jay','shiv'] 
        
        
        }
    
    return render(request, "index.html",info)
    
