# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView


class DashboardView(TemplateView):
    template_name = 'frontend/dashboard/index.html'
