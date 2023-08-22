from django.shortcuts import redirect, render 
from .models import text

message=[]
message.append("")

def index(request):
    context = {'message': message[0]}
    message.pop()
    message.append("")
    return render(request,"Posts/index.html", context)

def saveText(request):
    if request.method == "POST" :
        newText = request.POST['yourThoughts']
        title = request.POST['title']
        yourText = text(inputText = newText, title = title)
        yourText.save()
        message.pop()
        message.append("Your text has been saved, click 'Access the posts' to see the post")
    return redirect('index')

def list(request):
    all_entries = text.objects.all()
    context= {'all_entries': all_entries}
    return render(request, "Posts/list.html", context)

def post(request, id):
    thePostedText = text.objects.get(id = id)
    context = {'thePostedText' : thePostedText}
    return render(request, "Posts/post.html", context)




