from users.models import BannerOther

def banner(request):
	banner_list = BannerOther.objects.all()[:3]
	content = {'banner_list': banner_list}
	return content