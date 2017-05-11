from django.conf.urls import url
from . import views
urlpatterns = [

    url(r'^$', views.my_machine, name='dbindex'),
    url(r'^my_machine$', views.my_machine, name='my_machine'),

    url(r'^run_model$', views.run_model, name='run_model'),
    url(r'^ram_status$', views.ram_status, name='ram_status'),
    url(r'^cpu_status$', views.cpu_status, name='cpu_status')
]



