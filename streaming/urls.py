from django.urls import path

from streaming import views
from streaming.views import ChannelListView, ChannelDetailView

urlpatterns = [
    path('', ChannelListView.as_view(), name='channel-list'),
    path('channel/<slug:slug>/', ChannelDetailView.as_view(), name='channel-detail'),
    path('search/', views.SearchResultsView.as_view(), name='search-results'),
]
