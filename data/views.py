from django.shortcuts import render

# Create your views here.

def Home_View(request):
    return render(request, 'index.html')
def Login_View(request):
    return render(request, 'Signup.html')
#def PyListView(request):
 #   return render(request, 'listpage.html')