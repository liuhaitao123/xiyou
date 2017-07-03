from django.conf.urls import url

from .views import UniversityView, EstimateView, StrategyView, ArticleView, StrategyListView, UniversityDetailView

urlpatterns = [
    url(r'^university/$', UniversityView.as_view(), name='university'),
	url(r'^university/detail/(?P<university_id>\d+)$', UniversityDetailView.as_view(), name='univer-detail'),
    url(r'^estimate/$', EstimateView.as_view(), name='estimate'),
	url(r'^strategy/$', StrategyView.as_view(), name='strategy'),
	url(r'^strategy-list/$', StrategyListView.as_view(), name='strategy-list'),
	url(r'^strategy/article/(?P<article_id>\d+)$', ArticleView.as_view(), name='article'),
]