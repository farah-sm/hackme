from django.conf import settings

# Custom context processors to add variables to your template context.
def my_setting(request):
    return {'MY_SETTING': settings}


# Add the 'ENVIRONMENT' setting to the template context
def environment(request):
    return {'ENVIRONMENT': settings.ENVIRONMENT}
