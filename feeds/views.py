from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from django.http import HttpResponse
from django.template import loader
from .models import Feed

class FeedList(generic.ListView):
    queryset = Feed.objects.all()
    template_name = 'feed_list.html'
    #context_object_name = 'feed_list'
    paginate_by = 3

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Feed.objects.get('-pub_date')[:20]

class FeedDetail(generic.DetailView):
    model = Feed
    template_name = 'post_detail.html'

class FeedDetail(generic.DetailView):
    model = Feed
    template_name = 'detail.html'

def index(request):
    feed_list = Feed.objects.all() #.filter(Category_id = '1')
    paginate_by = 5
    context = {
        'feed_list': feed_list
    }
    return render(request, 'index.html', context=context) #feed_list

def detail(request, feed_id):
    try:
        feed_detail = Feed.objects.get(pk=feed_id)
    except Feed.DoesNotExist:
        raise Http404("Feed does not exist")
    return render(request, 'detail.html', {'feed_detail': feed_detail})

