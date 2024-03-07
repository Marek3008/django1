from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('skola/', include('skola.urls')),
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls')),
    path('calc/', include('kalkulacka.urls')),
    path('testovac/', include('testovac.urls'))
]
