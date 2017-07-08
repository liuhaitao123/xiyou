from django.conf.urls import url
#from .models import WriteType, Writer, Visa
from service.views import DocView, VisaView, DocDetailView

urlpatterns = [
    url(r'^doc/$', DocView.as_view(), name='doc'),
    url(r'^visa/$', VisaView.as_view(), name='visa'),
    url(r'^doc/detail/(?P<doc_id>\d+)$', DocDetailView.as_view(), name='doc-detail'),
]