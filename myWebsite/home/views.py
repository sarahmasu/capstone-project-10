from django.shortcuts import render

# Create your views here.
def index(request):
    """Renders the view onto the home webpage.

        :param HttpResponse request: Used to process the HttpResponse request
        :return: Renders the view onto the home.html page
        :rtype: HttpResponse
    """
    return render(request, "home.html")