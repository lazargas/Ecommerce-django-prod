from django.shortcuts import render



def home_view(request):
    isauthed = False
    issuper= False
    if request.user.is_authenticated:
        isauthed=True
    if request.user.is_superuser:
        issuper=True
    print(isauthed)
    print(issuper)
    context = {
        "isauthed":isauthed,
        "issuper":issuper
    }
    return render(request, "home.html",context)

def auth_view(request):
    return render(request,"auth.html")