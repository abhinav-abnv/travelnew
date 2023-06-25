from django.shortcuts import render
from.models import place , team

# Create your views here.
def demo(request):
    obj=place.objects.all()
    ob = team.objects.all()

    return render(request,'index.html',{'result':obj,'res':ob})


# def nemo(request):
#     ob = team.objects.all()
#
#     return render(request, 'index.html', {'res': ob})

# Create your views here.
