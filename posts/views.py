from django.shortcuts import render
from .models import Post



def post_list (request):
    data = Post.objects.all()   #db : all posts --> list [1,2]

    context = {
        'karim' : data
    }



    return render(request,'posts/post_list.html',context)


def post_details(request,post_id):
    data = Post.objects.get(id=post_id)   #db : all posts --> list [1,2]

    context = {
        'ali' : data
    }



    return render(request,'posts/post_details.html',context)
