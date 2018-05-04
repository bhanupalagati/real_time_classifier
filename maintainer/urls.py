from django.conf.urls import url
from maintainer import views

app_name = 'maintainer'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^titanic/',views.titanic,name='titanic'),
    url(r'^titanic_predict/',views.titanic_predict,name='titanic_predict'),
    url(r'^aboutus/',views.aboutus,name='aboutus')
]
