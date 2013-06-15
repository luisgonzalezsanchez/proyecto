from django.conf.urls import patterns, include, url
from markeplace.views import HomeController, PerfilController, UserCreate

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     #url(r'^$', HomeController.as_view(), name='home'),
     url(r'user/add/$', UserCreate.as_view(), name='nuevo'),
     url(r'user/add/$', 'markeplace.views.ingresar'),
     url(r'^$','markeplace.views.ingresar'),
     url(r'^privado/$','markeplace.views.privado'),
     url(r'^cerrar/$', 'markeplace.views.cerrar'),
    # url(r'^proyecto/', include('proyecto.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admini:
     url(r'^admin/', include(admin.site.urls)),
)
