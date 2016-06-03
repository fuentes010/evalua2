from django.conf.urls import url
from restapi import views

urlpatterns = [
    # Categoria Bloom
    url(r'^categoria-bloom/$', views.categorias_bloom_list, name='categorias_bloom_list'),
    url(r'^categoria-bloom/(?P<pk>[0-9]+)$', views.categorias_bloom, name='categorias_bloom'),
    # Categoria Bloom valor
    url(r'^categoria-bloom-valor/$', views.categorias_bloom_valor_list, name='categorias_bloom_valor_list'),
    url(r'^categoria-bloom-valor/(?P<pk>[0-9]+)$', views.categorias_bloom_valor, name='categorias_bloom_valor'),
    # Resultado aprendizaje
    url(r'^resultado-aprendizaje/$', views.resultado_aprendizaje_list, name='categorias_bloom_valor_list'),
    url(r'^resultado-aprendizaje/(?P<pk>[0-9]+)$', views.resultado_aprendizaje, name='categorias_bloom_valor'),
]
