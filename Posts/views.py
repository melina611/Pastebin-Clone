from django.urls import reverse
from django.shortcuts import redirect, render 
from .models import Text

def index(request):
    return render(request,"Posts/index.html")

def saveText(request):
    if request.method == "POST" :
        newText = request.POST['yourThoughts']
        title = request.POST['title']
        if not title:
            yourText = Text(inputText = newText)
        else:
            yourText = Text(inputText = newText, title = title)
        yourText.save()
        return redirect(reverse('post', kwargs={"id": yourText.id}))
    return redirect("index")

def list(request):
    all_entries = Text.objects.all()
    context= {'all_entries': all_entries}
    return render(request, "Posts/list.html", context)

def post(request, id):
    thePostedText = Text.objects.get(id = id)
    context = {'thePostedText' : thePostedText}
    return render(request, "Posts/post.html", context)




