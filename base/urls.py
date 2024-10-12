from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.staticfiles.urls import staticfiles_urlpatterns # new

# mainSystem/urls.py

handler404 = 'mainSystem.views.custom_error_view'  # 404 - Sahifa topilmadi
handler500 = 'mainSystem.views.custom_error_view'  # 500 - Serverdagi xato
handler403 = 'mainSystem.views.custom_error_view'  # 403 - Ruxsat yo'q
handler400 = 'mainSystem.views.custom_error_view'  # 400 - Noto‘g‘ri so‘rov


urlpatterns = [
    path('boshqaruv/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('',include("mainSystem.urls"))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)