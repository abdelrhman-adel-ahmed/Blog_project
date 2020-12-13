from django.shortcuts import render,get_object_or_404
from django.http import  HttpResponse
from django.shortcuts import render ,HttpResponseRedirect,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .models import post
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# posts=[     
#     {
#         "title":"general",
#         "author":"elshe2",
#         "contenet":"لازم ناخد بالنا جامد جدا ",
#         "date":"12-12-12"
#     }
#     ,
#     {
#         "title":"sport",
#         "author":"mohamed",
#         "contenet":"مش لازم ناخد بالنا اوي",
#         "date":"13-41-21"
#     }
# ]

# post1=post(title="oh oh ",content="frist time fomr inside the views",author_id=1)
# post1.save()

#instead of this we ussing listView
# def home(requeset):
#     context={
#         #'posts':posts
#         'posts':post.objects.all()
#     }
#     return render(requeset,'bloging/home.html',context)

def about(requeset):
    return render(requeset,'bloging/about.html')

class postListView(ListView):
    model=post
    #<app>/<model>_<viewtype>.html
    template_name="bloging/home.html"
    context_object_name="posts"
    ordering=['-date']

    """
    from django.core.paginator import Paginator
    posts=['1','2','3','4','5']
    p=Paginator(posts,2) <- create page each page have to posts so we have 3 page in totale
    p.paginator.count() -->return 5 (return how many object associated with the paginator )
    p.num_pages --> 3
    p1=p.page(1)
    p1.number --> 1 mean page num 1
    p1.object_list --> [1,2] mean first two posts in page 1 
    p1.has_next() true
    p1.has_previous() -->false
    p1.next_page_number() --> 2
    p1.previous_page_number() --> error (the page number is less than one) because this is the first page
    p.page_range --> return python range that we can loop over
    for page in p.page_range:
        print(page)
        1,2,3 
    """
    paginate_by=5 # --> meaning every page will have two elements

class UserpostListView(ListView):
    model=post
    template_name="bloging/user_posts.html"
    context_object_name="posts"
    paginate_by=5

    def get_queryset(self):
        #get the user name from the query string
        user=get_object_or_404(User,username=self.kwargs.get('username'))
        return post.objects.filter(author=user).order_by('-date')

class postDetailView(DetailView):
    model=post


#can only access of user is loged in ,if not redirect to the login page
class postCreateView(LoginRequiredMixin,CreateView):
    model=post
    fields=["title","content"]

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

#the owner of the post only can update the post 
#post update_view use the post_form tempalte (also the createPost view use the post_form template)
class postUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=post
    fields=["title","content"]

    #success_url="{%url 'post-detail' post.id%}"
    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    #check if user passes certain condition
    def test_func(self):
        #get the post that we curently open to update
        post=self.get_object()
        if self.request.user ==post.author:
            return True
        else: return False

   
#need a form that will ask if we sure to delete the post
class postDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=post
    def test_func(self):
        post=self.get_object()
        if self.request.user ==post.author:
            return True
        else: return False

    #where to redirect if the deletion succeded
    success_url="/"
    





def detatil(request,ss):
    postt=post.objects.get(pk=ss)
    cont={
        'object':postt
    }
    return render(request,"bloging/post_detail.html",cont)

