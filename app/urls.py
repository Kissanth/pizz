from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
