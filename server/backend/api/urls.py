from django.urls import path
from . import info, classification, tester


urlpatterns = [
    path('tester/', tester.tests, name="tester"),

    path('list/getenrolled/', info.getenrolled, name="getenrolled"),
    path('list/preview/', info.preview, name="preview"),
    path('list/preview2/', info.preview2, name="preview"),

    path('list/user/', info.user, name="preview"),
    path('list/user2/', info.user2, name="preview"),

    path('list/classify/', info.classify, name="enrolled"),
    path('list/classify2/', info.classify2, name="enrolled"),
    path('classify/data/', classification.classify, name="classify"),

]
