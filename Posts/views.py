from django.shortcuts import redirect, render 
from .models import text


def index(request):
    all_entries = text.objects.all()
    context= {'all_entries': all_entries}
    return render(request,"Posts/index.html",context)

def saveText(request):
    if request.method == "POST" :
        newText = request.POST['yourThoughts']
        yourText = text(inputText = newText)
        yourText.save()
    return redirect('/Posts')

def post(request, id):
    thePostedText = text.objects.get(id = id)
    context = {'thePostedText' : thePostedText}
    return render(request, "Posts/post.html", context)




