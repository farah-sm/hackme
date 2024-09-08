from web_project.template_helpers.theme import TemplateHelper

"""
This is an entry and Bootstrap class for the theme level.
The init() function will be called in web_project/__init__.py
"""

# The TemplateBootstrapSystem class is used to configure the context for system-level pages. These are pages like error pages (e.g., 404, 500) or administrative interfaces.
class TemplateBootstrapSystem:
    # Updates Context: Sets context variables specific to system pages:
    def init(context):
        context.update(
            {
                # Uses a blank layout for system pages, likely providing a minimal design without additional UI components.
                "layout": "blank",
                # Specifies a wide content layout to accommodate system messages or detailed information.
                "content_layout": "wide",
                # Disables any customizer features, which might be unnecessary for system-level pages.
                "display_customizer": False,
            }
        )
        # map_context according to updated context values
        # Updates the context with additional settings based on the provided values, ensuring that the system pages are rendered correctly with the appropriate layout.
        TemplateHelper.map_context(context)

        return context
        # This class helps maintain a consistent layout and styling for pages that handle errors or administrative tasks, providing a unified appearance for system-level content.
