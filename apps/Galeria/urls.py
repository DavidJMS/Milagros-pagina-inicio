from django.conf.urls import url 
from apps.Galeria.views import Mila
urlpatterns = [
    #url(r'^lista/$',listadeusuarios,name='listadeusuarios') , 
    url(r'^$',Mila , name='Mila' ),
]