from django.conf.urls import handler400, handler403, handler404, handler500
from django.urls import path, include

urlpatterns = [
    # path('', include('app.urls')),
    # path('posts/', include('forms.urls')),
    path('upload/', include('upload.urls')),
    # path('download/', include('file_generator.urls')),
    path('api/', include('api.urls')),
    # path('mailer/', include('api.urls')),
    # path('web/', include('web_app.urls')),
    # path('biometric/', include('biometric.urls')),
    path('auth/', include('authentication.urls')),
    # path('update/', include('update.urls')),
    # # path('static/', include('static')),
]


