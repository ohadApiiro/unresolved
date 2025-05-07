from django.urls import path, include
import crapi.views

urlpatterns = [
    path("api/mechanic/", include("crapi.mechanic.urls", namespace="matoki")),
    path('path1/', admin.site.urls),
    path('good/matoki/', crapi.MatokiView.as_view()),
]
