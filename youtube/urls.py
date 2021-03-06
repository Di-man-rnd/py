from django.conf.urls import url, patterns, include
from django.contrib import admin
from django.views.generic import TemplateView

from teach.views import *
from books.views import *
from youtube.views import *
# url:  /bloger/ =>
urlpatterns = [
    # Function
    url(r'^$', all_bloger, name='all_bloger'),
    url(r'^([0-9]+)/$', detail_bloger, name='detail_bloger'),

    # Class
    url(r'^list/$', BlogerList.as_view()),
    url(r'^(?P<pk>.*)/detail/$', BlogerDetail.as_view(), name='bloger_detail'), # pk or a slug.


    url(r'^list/category/$', CategoryList.as_view(), name='category_list'),
    url(r'^([0-9]+)/category/$', CategoryDetailList.as_view(), name='category_detail'),
    url(r'^category/add_func/$', categoryAdd),
    url(r'^category/add/$', CategoryCreate.as_view()),
    url(r'^category/update/(?P<pk>.*)/$', CategoryUpdate.as_view()),
    url(r'^category/delete/(?P<pk>.*)/$', CategoryDelete.as_view()),

    # url(r'^(?P<slug>.*)/detail/$', BlogerDetail.as_view()),  # ЧПУ
    # class ArticleAdmin(admin.ModelAdmin): prepopulated_fields = {"slug": ("title",)}

    # Helper
    # url(r'^about/', TemplateView.as_view(template_name="helper/about.html")), # default
    url(r'^about/', About.as_view()), # from my class


    # js AJAX
    url(r'^setcat/$', set_cat),
]

