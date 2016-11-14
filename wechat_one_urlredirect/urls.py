from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wechat_one_urlredirect.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/hp/detail/(\d+)$','url_redirect.views.detail'),
    url(r'^api/hp/idlist/(\d+)$','url_redirect.views.idlist'),
    url(r'^api/hp/bymonth/(\d+)$','url_redirect.views.bymonth'),
    url(r'^api/reading/carousel$','url_redirect.views.carousel'),
    url(r'^api/reading/index$','url_redirect.views.reading_index'),
    url(r'^api/essay/(\d+)$','url_redirect.views.essay'),
    url(r'^api/serialcontent/(\d+)$','url_redirect.views.serialcontent'),
    url(r'^api/question/(\d+)$','url_redirect.views.question'),
    url(r'^api/(\d+)/bymonth/(\d+)$','url_redirect.views.bymonthandtype'),

    url(r'^api/music/idlist/(\d+)$','url_redirect.views.music_idlist'),
    url(r'^api/music/bymonth/(\d+)$','url_redirect.views.music_bymonth'),
    url(r'^api/music/detail/(\d+)$','url_redirect.views.music_detail'),

    url(r'^api/movie/list/(\d+)$','url_redirect.views.movie_list'),
)

