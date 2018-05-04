from django.conf.urls import url
from gre import views

app_name = 'gre'

urlpatterns = [
    url(r'^$',views.gre,name='gre_'),
    url(r'^gre_predict',views.gre_predict,name='gre_predict'),
]
