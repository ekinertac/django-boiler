from config import settings


def variables(request):
    return {
        'SITE_NAME' : settings.SITE_NAME
        'DESCRIPTION' : settings.DESCRIPTION
        'AUTHOR' : settings.AUTHOR
    }