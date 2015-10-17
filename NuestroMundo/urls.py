from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^(?P<nombre_pais>[A-Z|a-z]+)/$', views.pais, name='paises'),
    url(r'^ciudades/(?P<id_ciudad>[0-9]+)$', views.ciudad, name='ciudades'),
    url(r'^idiomas/(?P<idioma_nombre>.+)$', views.idioma, name='idiomas'),
]