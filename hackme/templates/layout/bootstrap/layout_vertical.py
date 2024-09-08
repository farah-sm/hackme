from web_project.template_helpers.theme import TemplateHelper

"""
This is an entry and Bootstrap class for the theme level.
The init() function will be called in web_project/__init__.py
"""


class TemplateBootstrapLayoutVertical:
    def init(context):
        # All "True" indicates that the key should be present.
        context.update(
            {
                
                "layout": "vertical",
                "content_navbar": True,
                "content_layout": "compact",
                "is_navbar": True,
                "is_menu": True,
                "is_footer": True,
            }
        )

        # map_context according to updated context values
        # Calls the map_context method from TemplateHelper to adjust additional 
        # context values based on the vertical layout settings.
        TemplateHelper.map_context(context)



        return context

# This configuration makes it easy to apply a cohesive vertical layout across different pages, facilitating a uniform look and feel for the sections of your application that use this layout.







