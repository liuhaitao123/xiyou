from django.conf.urls import url

from .views import UniversityView, EstimateView, StrategyView

urlpatterns = [
    url(r'^university/$', UniversityView.as_view(), name='university'),
    url(r'^estimate/$', EstimateView.as_view(), name='estimate'),
	url(r'^strategy/$', StrategyView.as_view(), name='strategy'),
]