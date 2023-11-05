from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Channel


class ChannelListView(ListView):
    model = Channel
    template_name = 'streaming/channel_list.html'  # Specify the template to be used
    context_object_name = 'channels'  # Define the context variable name


class ChannelDetailView(DetailView):
    model = Channel
    template_name = 'streaming/channel_detail.html'  # Specify the template to be used
    context_object_name = 'channel'  # Define the context variable name

class SearchResultsView(ListView):
    model = Channel
    template_name = 'streaming/search_results.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Channel.objects.filter(name__icontains=query)
