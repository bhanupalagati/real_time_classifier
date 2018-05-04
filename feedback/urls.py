from django.conf.urls import url
from feedback import views

app_name = 'feedback'

urlpatterns = [
    url(r'^$',views.feedback,name='feedback'),
]
