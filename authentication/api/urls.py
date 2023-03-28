from django.urls import path, include


urlpatterns = [
    path('v1/', include('authentication.api.v1.urls'))
]