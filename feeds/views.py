from django.http import Http404
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from django.http import HttpResponse
from django.template import loader
from .models import Feed

class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'feed_list'

    # def get_queryset(self):
    #     """Return the last five published questions."""
    #     return Feed.objects.get('-pub_date')[:20]

class DetailView(generic.DetailView):
    model = Feed
    template_name = 'detail.html'

def index(request):
    feed_list = Feed.objects.all().filter()
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

