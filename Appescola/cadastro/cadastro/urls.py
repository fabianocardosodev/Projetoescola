from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url

from . import views 

app_name =  "cadastro"

urlpatterns = [
    url("cadastro/", TemplateView.as_view(template_name='cadastro.html')),

]