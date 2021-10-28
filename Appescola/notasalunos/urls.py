from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls import url

from . import views 

app_name =  "notasalunos"

urlpatterns = [
    url("notasalunos/", TemplateView.as_view(template_name='notasalunos.html')),

]