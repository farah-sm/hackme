from django.views.generic import TemplateView
from web_project import TemplateLayout
from web_project.template_helpers.theme import TemplateHelper

# SystemView, which extends TemplateView
class SystemView(TemplateView):
    # template_name: Specifies the template file to be used (pages/system/not-found.html).
    template_name = "pages/system/not-found.html"
    # status: An empty string that can be used to hold status information.
    status = ""

    # get_context_data: This method populates the context data passed to the template.
    def get_context_data(self, **kwargs):
        # A function to init the global layout. It is defined in web_project/__init__.py file
        context = TemplateLayout.init(self, super().get_context_data(**kwargs))

        # Define the layout for this module
        # _templates/layout/system.html
        context.update(
            {
                "layout_path": TemplateHelper.set_layout("system.html", context),
                "status": self.status,
            }
        )

        return context
