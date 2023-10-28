from django.urls import path

from api import views

app_name = 'api'

urlpatterns = [
    path(
        'api/v1/<str:constructorRef>/',
        views.constructor_api_detail,
        name='api_v1',
    ),
]