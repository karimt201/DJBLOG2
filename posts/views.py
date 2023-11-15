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



'''
def post_list (request):
    data = Post.objects.all()                                   : query
    context = {'karim' : data}                                  : context
    return render(request,'posts/post_list.html',context)       : template
'''

from django.views.generic import ListView , DetailView

class postlist(ListView):                   #context : model_list , object_list
    model = Post                            #temolate model_action : post_list


class postdetail(DetailView):
    model = Post