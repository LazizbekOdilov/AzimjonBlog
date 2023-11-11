from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('about/', about),
    path('blog/', blog),
    path('maqola/', maqola),
    # mashq
    path('t_maqola/<int:son>/', t_maqola)

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

