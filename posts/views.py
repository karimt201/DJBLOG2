from django.shortcuts import render , redirect
from .models import Post
from .forms import PostForm



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

def create_post(request):
    form = PostForm()

    if request.method =='POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            myform = form.save(commit = False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else :
        form = PostForm()

    return render(request,'posts/new.html',{'form' : form })


   
def edit_post(request,pk):
    post = Post.objects.get(id=pk)

    if request.method =='POST':
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            myform = form.save(commit = False)
            myform.author = request.user
            myform.save()
            return redirect('/posts/')
    else :
        form = PostForm(instance=post)

    return render(request,'posts/edit.html',{'form' : form })
    

def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/')
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



    