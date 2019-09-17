from django.shortcuts import render
#from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post

# Create your views here.

# not used anymore because we connected vacations to MySQL
vacations = [
    {
        'description': 'Turkey Trip with GOOD Offers',
        'date_from': 'Date: from 25/3/2019',
        'date_to': '28/3/2019',
        'time_from': 'Time: from 10:00 AM',
        'time_to': '10:00 AM',
        'duration_of_the_whole_trip': 'Duration of the whole trip is 3 days'
    },
    {
        'description': 'Trip to Paris',
        'date_from': 'Date: from 26/3/2019',
        'date_to': '31/3/2019',
        'time_from': 'Time: from 11:11 AM',
        'time_to': '11:11 AM',
        'duration_of_the_whole_trip': 'Duration of the whole trip is 5 days'
    }
]

# function
def home(request): 
    context = {
        'vacations': Post.objects.all()
    }
    return render(request, 'VAC/home.html', context)
    
class PostListView(ListView):
    model = Post
    template_name = 'VAC/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'vacations' #from above function home
    paginate_by = 2 # how many vacation posts we need to put per page
    
class PostCreateView(CreateView):
    model = Post
    fields = ['description', 'date_from', 'date_to', 'time_from', 'time_to', 'duration_of_the_whole_trip']

    def form_valid(self, form):
        form.instance.who_posted = self.request.user
        # pass in that form a an argument
        return super().form_valid(form)

class PostUpdateView(UpdateView):
    model = Post
    fields = ['description', 'date_from', 'date_to', 'time_from', 'time_to', 'duration_of_the_whole_trip']

    def form_valid(self, form):
        form.instance.who_posted = self.request.user
        # pass in that form a an argument
        return super().form_valid(form)

    # function to test if the user updating is the same as the one who posted the vacation
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.who_posted:
            return True
        return False

class PostDeleteView(DeleteView):
    model = Post
    # taking to the home page in case the employee insisted to delete the post vacation
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.who_posted:
            return True
        return False
        