from django.contrib import admin
from django.urls import include, path, re_path
from rest_framework import routers, permissions
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from users import views
from users.views import CustomTokenObtainPairView, AccountActivationView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="users_microservice",
        default_version='0.1',
        description="Documentation to out project",
        contact=openapi.Contact(email="gtoll@yandex.ru"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'users/(?P<username>[^/.]+)', views.UserViewSet, basename='user_by_username')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token),
    path('api/jwt-token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/jwt-token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('account_activation/', AccountActivationView.as_view(), name='account_activate'),
    path('api/', include(router.urls)),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc'),
]
