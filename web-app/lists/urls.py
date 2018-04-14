from django.conf.urls import url

from lists import views

urlpatterns = [
    url(r'^new$', views.new_list, name='new_list'),
    url(r'^(.+)/$', views.view_list, name='view_list'),
    url(r'^(.+)/new_item$', views.new_item, name='new_item')
]
