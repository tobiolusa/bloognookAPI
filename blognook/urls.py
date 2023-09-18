from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Blognook v1 API",
        default_version= "v1",
        description= "Blognook is a versatile content management system (CMS) and blogging API that empowers users to effortlessly establish their own accounts and manage their personalized blogs within the application. This platform provides users with the ability to seamlessly publish, modify, and remove their content as they see fit.c",
        contact= openapi.Contact(email="olusamiracle@gmail.com")
    ), 
    public = True,
    permission_classes = (permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name="schema-redoc"),
    path('api/v1/', include('accounts.urls')),
]
