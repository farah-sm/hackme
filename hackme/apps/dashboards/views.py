from django.views.generic import TemplateView
from apps.common.views import BlankView
from web_project import TemplateLayout


"""
This file is a view controller for multiple pages as a module.
Here you can override the page view layout.
Refer to dashboards/urls.py file for more pages.
"""


class DashboardsView(TemplateView):
    # Predefined function
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        return context


class LandingPageView(BlankView):
    # Predefined function
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
