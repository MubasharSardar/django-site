from django.urls import path

#from .views import Home_View
from .models import pydata

#urlpatterns = [
 #   path('', Home_View, name='home')
#]


from django.views.generic import ListView, DetailView
from django.conf.urls import url
#urlpatterns = [
 #   path('', Blog_view)
#]

urlpatterns = [
    url(r'^$',ListView.as_view(queryset=pydata.objects.all().order_by("-date")[:25],template_name="listpage.html"), name='python'),
    url(r'(?P<pk>\d+)$',DetailView.as_view(model=pydata, template_name="detailpage.html")),
]