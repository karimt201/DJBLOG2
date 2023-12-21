from django.contrib.auth.mixins import LoginRequiredMixin
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
    template_name='posts/home.html'
    context_object_name = 'posts'


class postdetail(DetailView):
    model = Post
    template_name = 'posts/post_detail2.html'
    



class AddPost(LoginRequiredMixin,CreateView) :
    model = Post
    template_name='posts/post_create.html'
    fields = ['title','content']
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class EditPost(LoginRequiredMixin,UpdateView) :
    model = Post
    template_name='posts/post_create.html'
    fields = ['title','content']
    success_url = '/posts/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class DeletePost(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/posts/'

