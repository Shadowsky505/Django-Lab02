from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('encuesta/', include('encuesta.urls')),
    path('admin/', admin.site.urls),
    path('operacionnumeros/', include('OperacionNumeros.urls')),
    path('volumencilindro/', include('volumenCilindro.urls')),
]
