from django.conf.urls import url
from users.views import RegisterView, LoginView, IndexView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'^$', IndexView.as_view(), name='index'),
]