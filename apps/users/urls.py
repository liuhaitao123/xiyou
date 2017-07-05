from django.conf.urls import url
from users.views import RegisterView, LoginView, LogoutView, IndexView, HighApplyView, UsercenterView, MyApplyView, MyOrderView, MyAskView, MyQstView, CaseView

urlpatterns = [
    url(r'^register/$', RegisterView.as_view(), name='register'),
    url(r'login/$', LoginView.as_view(), name='login'),
    url(r'logout/$', LogoutView.as_view(), name='logout'),
    url(r'^$', IndexView.as_view(), name='index'),
	url(r'^highapply/$', HighApplyView.as_view(), name='highapply'),
	url(r'^usercenter/$', UsercenterView.as_view(), name='usercenter'),
	url(r'^myapply/$', MyApplyView.as_view(), name='myapply'),
	url(r'^myorder/$', MyOrderView.as_view(), name='myorder'),
	url(r'^myask/$', MyAskView.as_view(), name='myask'),
	url(r'^myquestion/$', MyQstView.as_view(), name='myquestion'),
	url(r'^wincase/(?P<case_id>\d+)$', CaseView.as_view(), name='wincase'),
]