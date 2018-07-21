from django.shortcuts import render

# Create your views here.


def main_view(request):
    print(request)
    print(request.body)
    return render(request, "main.xml")
