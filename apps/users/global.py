from __future__ import unicode_literals


from users.models import BannerOther


def banner(request):
    banner_list = BannerOther.objects.all()[:3]
    return {'banner_list': banner_list}
