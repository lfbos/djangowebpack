from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    url(r'^test_view/$', TemplateView.as_view(template_name='frontend/test_view/index.html'))
]
