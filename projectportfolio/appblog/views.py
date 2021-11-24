from django.shortcuts import get_object_or_404
from .models import posts
from django.views import generic

# class based views for posts
class blogposts(generic.ListView):
    queryset = posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'blogposts.html'
    paginate_by = 5

# class based view for each post
class singlepost(generic.DetailView):
    model = posts
    template_name = "singlepost.html"

    # def get_context_data(self, *args, **kwargs):
    #     context = super(singlepost, self).get_context_data()
    #     objs = get_object_or_404(posts, id=self.kwargs['pk'])
    #     context['total_likes'] = objs.total_likes()
    #     return context
