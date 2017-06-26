from django.conf.urls import url
#from .models import WriteType, Writer, Visa
from service.views import DocView, VisaView

urlpatterns = [
    url(r'^doc/$', DocView.as_view(), name='doc'),
    url(r'^visa/$', VisaView.as_view(), name='visa'),
]