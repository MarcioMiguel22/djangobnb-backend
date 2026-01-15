from django.http import JsonResponse


def api_root(request):
    """
    API Root endpoint - shows available endpoints
    """
    return JsonResponse({
        'message': 'Welcome to Djangobnb API',
        'version': '1.0.0',
        'endpoints': {
            'admin': '/admin/',
            'authentication': {
                'login': '/api/auth/login/',
                'register': '/api/auth/registration/',
                'logout': '/api/auth/logout/',
                'user': '/api/auth/user/',
                'token_refresh': '/api/auth/token/refresh/',
            },
            'properties': {
                'list': '/api/properties/',
                'detail': '/api/properties/<uuid:pk>/',
                'create': '/api/properties/create/',
            },
            'chat': {
                'conversations': '/api/chat/',
                'messages': '/api/chat/<uuid:pk>/',
            },
        },
        'documentation': 'https://github.com/MarcioMiguel22/djangobnb-backend',
    })
