from django.contrib import admin
from django.urls import path, include
from chat.views import conversation, gen_title
from payment import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('api/v1/prompts/', include('prompt.urls')),
    path('api/chat/', include('chat.urls')),
    path('api/conversation/', conversation, name='conversation'),
    path('api/gen_title/', gen_title, name='gen_title'),
    path('api/account/', include('account.urls')),
    path('api/packages/', views.get_packages, name='get_packages'),
]
