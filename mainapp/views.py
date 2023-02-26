from django.shortcuts import render

# Create your views here.
# view index page
def viewindexpage(request):
    return render(request,'index.html')
