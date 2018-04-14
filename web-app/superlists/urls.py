from django.conf.urls import include, url

from lists import views as lists_views
from lists import urls as lists_urls


urlpatterns = [
    url(r'^$', lists_views.home_page, name='home'),
    url(r'^list/', include(lists_urls)),
]
