from django.views.generic import ListView , DetailView , CreateView , UpdateView , DeleteView
from .models import Post

'''
def post_list (request):
    data = Post.objects.all()                                   : query
    context = {'karim' : data}                                  : context
    return render(request,'posts/post_list.html',context)       : template
'''

class postlist(ListView):                   #context : model_list , object_list
    model = Post                            #temolate model_action : post_list


class postdetail(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'



class AddPost(CreateView) :
    model = Post
    fields = '__all__'
    success_url = '/posts/'

class EditPost(UpdateView) :
    model = Post
    fields = '__all__'
    success_url = '/posts/'
    template_name = 'posts/edit.html'

class DeletePost(DeleteView):
    model = Post
    success_url = '/posts/'

