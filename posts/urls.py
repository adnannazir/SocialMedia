from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name="home"),
    path('post/create', views.post_create_view, name="post_create"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
