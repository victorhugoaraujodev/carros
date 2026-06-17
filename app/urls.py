from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from app.views import HomeView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('', include('accounts.urls')),
    path('', include('cars.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
