from django.contrib import admin
from django.urls import path, include

handler404 = 'sharetext.views.handler404'
handler500 = 'sharetext.views.handler500'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('share/', include('sharetext.urls'))
]
