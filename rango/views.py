from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category

def index(request):
    # Query the database for a list of ALL the categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than five.
    # Place the list in our context_dict dictionary (with our boldmessage!)
    # that will be passed to the template engine.
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories']= category_list
   # context_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Render the response and send it back!
    return render(request, 'rango/index.html', context=context_dict)

    return HttpResponse("Rango says hey there partner! This way to the about page (<a href='/rango/about/'>About</a>)")

def about(request):



    return render(request, 'rango/about.html')

    return HttpResponse("Rango says this here is the about page. This way to go back to the index (<a href='/rango/'>Index</a>)")

