from django.http import HttpResponse, JsonResponse


def home_page(request):
    print("Home page requested")
    friends=[
        'ankit' ,
        'ravi' ,
        'uttam' 
    ]
    return JsonResponse(friends,safe=False)
    # return HttpResponse("<h1>This is your home page<h1>")