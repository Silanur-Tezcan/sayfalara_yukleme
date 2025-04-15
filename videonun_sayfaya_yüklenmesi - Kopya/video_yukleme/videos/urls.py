from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('video/', views.video_list, name="video"),
    # Diğer URL desenleriniz burada
]

# Medya dosyalarının doğru şekilde sunulabilmesi için aşağıdaki satırı ekleyin
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
