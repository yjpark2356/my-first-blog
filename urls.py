from django.conf.urls import include, url
from django.contrib import admin
from mysite2.view import HomeView
#from django.views.generic import ListView, DetailView
#from bookmark.models import Bookmar

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bookmark/', include('bookmark.urls', namespace='bookmark')),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    url(r'$', HomeView.as_view(), name='home'),

    #url(r'^bookmarks/$', ListView.as_view(model=Bookmark), name='index'),
    #url(r'^bookmarks/(?P<pk>\d+)/$', DetailView.as_view(model=Bookmark), name='detail'),  # 추가
]
