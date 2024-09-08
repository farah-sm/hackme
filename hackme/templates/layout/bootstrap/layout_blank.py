from web_project.template_helpers.theme import TemplateHelper


"""
This is an entry and Bootstrap class for the theme level.
The init() function will be called in web_project/__init__.py
"""

# This class, TemplateBootstrapLayoutBlank, is used to set up the context for the blank layout. 
# It configures how pages using this layout should be structured.
class TemplateBootstrapLayoutBlank:
    def init(context):
        # Sets specific context variables such as "layout", "content_layout", and "display_customizer".
        context.update(
            {
                "layout": "blank",
                "content_layout": "wide",
                "display_customizer": False,
            }
        )
        # map_context according to updated context values
        #  Calls the map_context method from TemplateHelper to adjust 
        # the context based on the current layout settings.
        TemplateHelper.map_context(context)

        return context

# This setup ensures that when the blank layout is used, it is correctly initialized with the right context values, making it ready for rendering minimalistic or specialized pages.



