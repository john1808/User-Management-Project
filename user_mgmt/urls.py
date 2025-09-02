from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/', include('tasks.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),


        # ---- Frontend pages ----
    path('', TemplateView.as_view(template_name="index.html")),            # login
    path('register/', TemplateView.as_view(template_name="register.html")),
    path('profile/', TemplateView.as_view(template_name="profile.html")),
    path('tasks/', TemplateView.as_view(template_name="tasks.html")),

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

