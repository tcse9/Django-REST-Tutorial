from .views import BlogPostRudView
from django.conf.urls import url


urlpatterns = [
    url(r'^(?P<pk>\d+)/$', BlogPostRudView.as_view(), name='post-rud'),
]

