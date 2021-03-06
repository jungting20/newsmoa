from django.conf.urls import url

from newsproject.home import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^user/', include('newsproject.user.urls')),
    url(r'^news_component/', include('newsproject.news_component.urls')),
    url(r'^news_board/', include('newsproject.news_board.urls')),
]